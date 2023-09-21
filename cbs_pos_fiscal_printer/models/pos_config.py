# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
import socket
from .FP_core import ServerException, SErrorType
from .FP import FP, Enums
from urllib.parse import urlparse
import logging
import traceback


from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
_logger = logging.getLogger(__name__)


class PosConfig(models.Model):
    _inherit = ['pos.config', 'mail.thread']
    _name = 'pos.config'

    cbs_fiscal_printer_server_ip = fields.Char(tracking=1, default="127.0.0.1:4444", help='The hostname or '
                                               'IP address of the ZPF server/driver for fiscal printer; '
                                               'if not empty will use cbssolutions.ro module for printing recipts'
                                               ' It can be like 127.0.0.1:4444. If is set will use it, and not serial.'
                                               'If not set will be like without module installed')

    cbs_fiscal_printer_ip = fields.Char(default="192.168.1.68",
                                        help='Ip address of fiscal printer, if not set will try to use serial')
    cbs_fiscal_printer_port = fields.Integer(default=8000,
                                             help='tcp port where is listening the fiscal printer')

    cbs_fiscal_printer_password = fields.Char(default="aA12345",
                                              help='password required by zfp server on a lan connection')
    cbs_fiscal_printer_serial_port = fields.Char(tracking=1, default="COM3",
                                                 help='Serial port that can be write/read by server; where is '
                                                 'conected the fiscal device to server.')
    cbs_fiscal_printer_serial_speed = fields.Integer(tracking=1, default=115200,
                                                     help='Serial speed for port where the fiscal device is '
                                                     'connected to the server.')

    cbs_operator_password = fields.Char(default='0', help="Is the parameter OperPass that is default '0' for fiscal "
                                        "casher and '0000' for fiscal printers. We are using the operator 1.")
    cbs_print_non_fiscal_receipt = fields.Boolean(default=1, help='All receipts will be non fiscal.')
    cbs_barcode_to_print = fields.Boolean()
    cbs_cut_after_print = fields.Boolean(help="works only at fisacal printers")
    cbs_cash_drawer_open = fields.Boolean(default=1,
                                          help="If checked, will give command. Works if you have a cash drawer "
                                          "connected to fiscal device, and when is something about cash.")
    cbs_print_logo = fields.Boolean()
    cbs_no_zero_value_on_fiscal_receipt = fields.Boolean(
        help="If True, will not print on fiscal receipt lines with value 0;"
        " will print them on non fiscal recipts (can be the case of kitchen components).")
    cbs_after_fiscal_receipt_print_non_fiscal = fields.Boolean(
        help="If True, after printing of a fiscal receipt(or if fiscal, at next prints) will print also the non fiscal one.")

    cbs_fiscal_printer_line_symbols = fields.Integer(default=32, help="Max nr of characters per printed line. "
                                                     "Used to split on more lines for example the product name.")
    cbs_receipt_product_name_max_lines = fields.Integer(default=3, help="Max lines what a long product name can have.")

    cbs_no_vat_class = fields.Selection(
        [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], require=1,
        help='If you sell without vat, what vat to put from tremol VAT rates.', default="E")
    cbs_odoo_tax_id_to_tremol_vat_json = fields.Char(
        default='{}', help='A json mapping the id of tax to tremol vat class '
        'like for example {"3":"A", "30":"B"} will map the tax with id=3 from odoo '
        'to VAT rateA from tremol that is usualy 19.00; If mapping does not match will take the configured A VAT rate.')

# existing fileds just for tracking
    receipt_header = fields.Text(tracking=1, default="")
    receipt_footer = fields.Text(tracking=1, default="")

    def cbs_test_print_at_fiscal_server(self):
        if not self.cbs_fiscal_printer_server_ip:
            raise ValidationError("You do not have configured in pos config the cbs_fiscal_printer_server_ip."
                                  " Support at dev@cbssolutions.ro.")
        cbs_fiscal_printer_server_ip = self.cbs_fiscal_printer_server_ip
        if "//" not in cbs_fiscal_printer_server_ip:
            cbs_fiscal_printer_server_ip = f"//{cbs_fiscal_printer_server_ip}"  # wihout // is not spliting
        url = urlparse(cbs_fiscal_printer_server_ip)
        hostname = url.hostname
        port = url.port
        if not port:
            port = 4444
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((hostname, port))
        if result == 0:
            pass  # port is open
        else:
            raise ValidationError(
                f"The Driver/Print Server with cbs_fiscal_printer_server_ip="
                f"{self.cbs_fiscal_printer_server_ip} {hostname=} {port=} is not reachable. "
                "Support at dev@cbssolutions.ro."
                )
        if self.cbs_fiscal_printer_ip:
            settings_param = (self.cbs_fiscal_printer_ip, self.cbs_fiscal_printer_port,
                              self.cbs_fiscal_printer_password)
        elif self.cbs_fiscal_printer_serial_port:
            settings_param = (self.cbs_fiscal_printer_serial_port,
                              self.cbs_fiscal_printer_serial_speed)
        else:
            raise ValidationError(
                "You did not configure ip or port for fiscal printer. "
                "Support at dev@cbssolutions.ro.")
        try:
            ex_open_non_fiscal_receipt, ex_close_non_fiscal = '', ''
            # here is the connection of the ZFPLABserver with fiscal device
            fp = FP()
            column_position = self.cbs_fiscal_printer_server_ip.find(":")
            cbs_fiscal_printer_server_ip_ip = self.cbs_fiscal_printer_server_ip[:column_position]
            if column_position != -1:
                cbs_fiscal_printer_server_ip_port = int(self.cbs_fiscal_printer_server_ip[column_position+1:])
            else:
                cbs_fiscal_printer_server_ip_port = 4444
            fp.serverSetSettings(cbs_fiscal_printer_server_ip_ip, cbs_fiscal_printer_server_ip_port)
            fp.serverSetDeviceTcpSettings(*settings_param)
            if not fp.isCompatible():
                raise ValidationError("Server definitions and client code have different versions!")
            # test server can reach ip/port of fiscal device
            if self.cbs_fiscal_printer_ip:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.cbs_fiscal_printer_ip, self.cbs_fiscal_printer_port))
                if result == 0:
                    pass  # exist connection between ZFPLABserver and Fiscal Device
                else:
                    raise ValidationError(
                        "The Driver/Fiscal Pritner Server can not connect to Fiscal Device with ip="
                        f"{self.cbs_fiscal_printer_ip} on port:{self.cbs_fiscal_printer_port}."
                        " If the fiscal printer is on, and it has internet, and the route from server is ok, "
                        "and is not a fiscal printer, it  must be in Sale Menu to show 0.00 (Mode/Reg oper/0/Total)."
                        " Support at dev@cbssolutions.ro."
                        )
            try:
                # opening a nor fiscal receipt
                fp.OpenNonFiscalReceipt(1, self.cbs_operator_password, 0)  # last parameter 0 step by step printint, 1 postponed printing
            except Exception as ex1:
                ex_open_non_fiscal_receipt = ex1
                try:  # if it was blocked and showing STL
                    fp.CancelReceipt()   # comand i
                    raise ValidationError(f'Bon fiscal anterior ramas deschiis {ex1=}. L-am inchis. '
                                          'Mai printeaza o data.')
                except Exception as ex2:
                    ex_close_non_fiscal = ex2
                    # no fiscal recipt was left open
                    # we can only be in case of a opened non fiscal receipt and we are closing it
                    fp.CloseNonFiscalReceipt()
                    raise ValidationError(f"We closed a non fiscal recipt that was open. Before_error:{ex2}")
            fp.PrintText("SUPPORT: https://cbssolutions.ro")
            fp.CloseNonFiscalReceipt()
            if self.cbs_cut_after_print:
                fp.PaperFeed()
                fp.CutPaper()
            _logger.warning('!!!!!!!!!!!Fiscal Printer test succeded. !!!!!!!!!!!Support at dev@cbssolutions.ro!!!!!')
        except Exception as ex3:
            raise ValidationError(f"{ex_open_non_fiscal_receipt=}\n{ex_close_non_fiscal=}\n{ex3=}\n\n{traceback.format_exc()=}")

    def cbs_report_z(self):
        self.cbs_report_x(OptionZeroing='Z')

    def cbs_report_x(self, OptionZeroing='X'):
        if not self.cbs_fiscal_printer_server_ip:
            raise ValidationError("You do not have configured in pos config the cbs_fiscal_printer_server_ip."
                                  " Support at dev@cbssolutions.ro.")
        cbs_fiscal_printer_server_ip = self.cbs_fiscal_printer_server_ip
        if "//" not in cbs_fiscal_printer_server_ip:
            cbs_fiscal_printer_server_ip = f"//{cbs_fiscal_printer_server_ip}"  # wihout // is not spliting
        url = urlparse(cbs_fiscal_printer_server_ip)
        hostname = url.hostname
        port = url.port
        if not port:
            port = 4444
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((hostname, port))
        if result == 0:
            pass  # port is open
        else:
            raise ValidationError(
                f"The Driver/Print Server with cbs_fiscal_printer_server_ip="
                f"{self.cbs_fiscal_printer_server_ip} {hostname=} {port=} is not reachable. "
                "Support at dev@cbssolutions.ro."
                )
        if self.cbs_fiscal_printer_ip:
            settings_param = (self.cbs_fiscal_printer_ip, self.cbs_fiscal_printer_port,
                              self.cbs_fiscal_printer_password)
        elif self.cbs_fiscal_printer_serial_port:
            settings_param = (self.cbs_fiscal_printer_serial_port,
                              self.cbs_fiscal_printer_serial_speed)
        else:
            raise ValidationError(
                "You did not configure ip or port for fiscal printer. "
                "Support at dev@cbssolutions.ro.")
        try:
            # here is the connection of the ZFPLABserver with fiscal device
            fp = FP()
            fp.serverSetSettings(hostname, port)
            fp.serverSetDeviceTcpSettings(*settings_param)
            if not fp.isCompatible():
                raise ValidationError("Server definitions and client code have different versions!")
            # test server can reach ip/port of fiscal device
            if self.cbs_fiscal_printer_ip:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.cbs_fiscal_printer_ip, self.cbs_fiscal_printer_port))
                if result == 0:
                    pass  # exist connection between ZFPLABserver and Fiscal Device
                else:
                    raise ValidationError(
                        "The Driver/Fiscal Pritner Server can not connect to Fiscal Device with ip="
                        f"{self.cbs_fiscal_printer_ip} on port:{self.cbs_fiscal_printer_port}."
                        " If the fiscal printer is on, and it has internet, and the route from server is ok, "
                        "and is not a fiscal printer, it  must be in Sale Menu to show 0.00 (Mode/Reg oper/0/Total)."
                        " Support at dev@cbssolutions.ro."
                        )
            try:
                fp.PrintDailyReport(OptionZeroing=OptionZeroing)
            except Exception as ex:
                raise ValidationError(f"Error for report={OptionZeroing}; {ex=}; suport at dev@cbssolutions.ro.")
            if self.cbs_cut_after_print:
                fp.PaperFeed()
                fp.CutPaper()
            _logger.warning('!!!!!!!!!!!Fiscal Printer test succeded. !!!!!!!!!!!Support at dev@cbssolutions.ro!!!!!')
        except Exception as ex:
            raise ValidationError(ex)
