# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
import socket
from .FP_core import ServerException, SErrorType
from .FP import FP, Enums
from datetime import datetime
import json
from unidecode import unidecode
import logging

from urllib.parse import urlparse
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
_logger = logging.getLogger(__name__)

def handle_exception(sx):
    msg = sx
    if hasattr(sx, 'message'):
        msg = sx.message
    text_err = []

    if isinstance(sx, ServerException):
        text_err.append("ZfpLab library exception!")
        if sx.isFiscalPrinterError:
            # Possible reasons:
            # sx.STE1 =                                       sx.STE2 =
            #       0x30 OK                                          0x30 OK
            #       0x31 Out of paper, printer failure               0x31 Invalid command
            #       0x32 Registers overflow                          0x32 Illegal command
            #       0x33 Clock failure or incorrect date&time        0x33 Z daily report is not zero
            #       0x34 Opened fiscal receipt                       0x34 Syntax error
            #       0x35 Payment residue account                     0x35 Input registers overflow
            #       0x36 Opened non-fiscal receipt                   0x36 Zero input registers
            #       0x37 Payment is done but receipt is not closed   0x37 Unavailable transaction for correction
            #       0x38 Fiscal memory failure                       0x38 Insufficient amount on hand
            #       0x39 Incorrect password                          0x3A No access
            #       0x3a Missing external display
            #       0x3b 24hours block - missing Z report
            #       0x3c Overheated printer thermal head.
            #       0x3d Interrupt power supply in fiscal receipt (one time until status is read)
            #       0x3e Overflow EJ
            #       0x3f Insufficient conditions
            #
            if sx.ste1 == 0x30 and sx.ste2 == 0x32:
                text_err.append("sx.STE1 == 0x30 - command is OK AND sx.STE2 == 0x32"
                                "- command is Illegal in current context")
            elif sx.ste1 == 0x30 and sx.ste2 == 0x33:
                text_err.append("sx.STE1 == 0x30 - command is OK AND sx.STE2 == 0x33"
                                " - make Z report")
            elif sx.ste1 == 0x34 and sx.ste2 == 0x32:
                text_err.append("sx.STE1 == 0x34 - Opened fiscal receipt AND sx.STE2 == 0x32"
                                " - command Illegal in current context")
            else:
                text_err.append((sx.message if hasattr(sx, 'message') else str(sx.args)) + " STE1=" + str(sx.ste1) +
                                " STE2=" + str(sx.ste2))
        elif sx.code == SErrorType.ServerDefsMismatch:
            text_err.append("The current library version and server definitions version do not match")
        elif sx.code == SErrorType.ServMismatchBetweenDefinitionAndFPResult:
            text_err.append("The current library version and the fiscal device firmware is not matching")
        elif sx.code == SErrorType.ServerAddressNotSet:
            text_err.append("Specify server ServerAddress property")
        elif sx.code == SErrorType.ServerConnectionError:
            text_err.append("Connection from this app to the server is not established")
        elif sx.code == SErrorType.ServSockConnectionFailed:
            text_err.append("When the server can not connect to the fiscal device; "
                            "See if the fiscal printer is On, and connected to internet. "
                            "If is not a fiscal printer, it  must be in Sale Menu and"
                            " to show 0.00 (Mode/Reg oper/0/Total).")
        elif sx.code == SErrorType.ServTCPAuth:
            text_err.append("Wrong device TCP password")
        elif sx.code == SErrorType.ServWaitOtherClientCmdProcessingTimeOut:
            text_err.append("Processing of other clients command is taking too long")
        else:
            text_err.append(msg)
    else:
        text_err.append(msg)
    return text_err


def split_product_name_in_printer_lines(name, line_len):
    lines = [name[i:i+line_len] for i in range(0, len(name), line_len)]
    return lines


class PosOrder(models.Model):
    _inherit = ['pos.order']

    cbs_fiscal_receipt_number = fields.Char(help="number that was printed by fiscal printer on recipt", readonly=1)
    cbs_ReadLastAndTotalReceiptNum = fields.Char(readonly=1, help="taken when printing form fiscal device")
    cbs_before_ReadLastAndTotalReceiptNum = fields.Char(readonly=1, help="taken before printing form fiscal device")

    def sanitise_txt_for_fiscal_print(self, txt):
        ascii_txt = unidecode(txt)  # unaccent unidecode('北亰') 'Bei Jing 'unidecode('François') 'Francois'
        return ascii_txt

    def cbs_print_at_fiscal_server_backend(self, *a):
        "used from backend like from pos, but will raise error"
        res = self.cbs_print_at_fiscal_server(a)
        error = res.get('error')
        if error:
            raise ValidationError(error)

    def cbs_print_at_fiscal_server(self, *a):
        if not self.config_id.cbs_fiscal_printer_server_ip:
            return {}
        if len(self) != 1:
            return {'error': f"we can only print one fiscal receipt; but received {self=}"}
        # test not th have refound and sale in same recipt
        is_return = self.lines.filtered(lambda r: r.refunded_orderline_id)
        is_sale = self.lines.filtered(lambda r: not r.refunded_orderline_id)
        # if self.amount_total is negative must be a is_return
        # storno must have same VAT type as lines; storno lines must be the last ones
        # if we have self.amount_total, we can have storno lines on fiscal receipt
        has_negative_amount = self.amount_total <= 0.01

        # this was before was posible to have storno and sale in same receipt
        # if is_sale and is_return:
        #    return {'error': "Nu poti avea si linii de vanzare si de retur in acelsi bon. Prima data faceti retur cu "
        #            "liniile necesare apoi faceti alt bon cu ce se vinde."}

        if self.cbs_fiscal_receipt_number:
            return {'error': "This recipt is already printed and it has the follwoing "
                    f"{self.cbs_fiscal_receipt_number=}"}
        if not self.config_id.cbs_fiscal_printer_server_ip:
            return {'error': "You do not have configured in pos config the cbs_fiscal_printer_server_ip."
                    " Support at dev@cbssolutions.ro."
                    }
        cbs_fiscal_printer_server_ip = self.config_id.cbs_fiscal_printer_server_ip
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
            return {'error': f"The Driver/Print Server with cbs_fiscal_printer_server_ip="
                    f"{self.config_id.cbs_fiscal_printer_server_ip} {hostname=} {port=} is not reachable. "
                    "Support at dev@cbssolutions.ro."}

        if self.config_id.cbs_fiscal_printer_ip:
            settings_param = (self.config_id.cbs_fiscal_printer_ip, self.config_id.cbs_fiscal_printer_port,
                              self.config_id.cbs_fiscal_printer_password)
        elif self.config_id.cbs_fiscal_printer_serial_port:
            settings_param = (self.config_id.cbs_fiscal_printer_serial_port,
                              self.config_id.cbs_fiscal_printer_serial_speed)
        else:
            return {'error': "You did not configure ip or port for fiscal printer. "
                    "Support at dev@cbssolutions.ro."}
        try:
            # here is the connection of the ZFPLABserver with fiscal device
            fp = FP()
            fp.serverSetDeviceTcpSettings(*settings_param)
            if not fp.isCompatible():
                return {'error': "Server definitions and client code have different versions!"}
            # test server can reach ip/port of fiscal device
            if self.config_id.cbs_fiscal_printer_ip:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.config_id.cbs_fiscal_printer_ip, self.config_id.cbs_fiscal_printer_port))
                if result == 0:
                    pass  # exist connection between ZFPLABserver and Fiscal Device
                else:
                    return {'error': "The ZFPLABserver can not connect to Fiscal Device with ip="
                            f"{self.config_id.cbs_fiscal_printer_ip} on port:{self.config_id.cbs_fiscal_printer_port}."
                            " If the fiscal printer is on, and it has internet, and the route from server is ok, and"
                            " is not a fiscal printer, it  must be in Sale Menu to show 0.00 (Mode/Reg oper/0/Total)."
                            "Support at dev@cbssolutions.ro."
                            }
            # from here is comunicating with the fiscal device
            before = fp.ReadLastAndTotalReceiptNum()
            b_last_nr = str(before.LastReceiptNum)
            b_last_total = str(before.TotalReceiptCounter)

            try:
                # opening a fiscal receipt or nor fiscal
                if self.config_id.cbs_print_non_fiscal_receipt or has_negative_amount:
                    # for fiscal printer must be "0000", for fiscal cascher must be "0" (operator 1 password)
                    # fp.OpenNonFiscalReceipt(1, "0", 0)  # OperPass
                    # fp.OpenNonFiscalReceipt(1, "0000", 0) 
                    fp.OpenNonFiscalReceipt(1, self.config_id.cbs_operator_password, 0)
                else:
                    fp.OpenReceipt(1, self.config_id.cbs_operator_password, 0)
            except Exception as ex:
                try:  # if it was blocked and showing STL
                    fp.CancelReceipt()   # comand i
                    return {'error': f'Bon fiscal anterior ramas deschiis {ex=}. L-am inchis. Mai printeaza o data.'}
                except Exception as ex:
                    # no fiscal recipt was left open; or we are in payment
                    try:
                        fp.CashPayCloseReceipt()  # if i'm in payment I can not cancel it with normal cancel
                    except Exception as ex:
                        # we can only be in case of a opened non fiscal receipt and we are closing it
                        fp.CloseNonFiscalReceipt()
                    return {'error': f"We closed a non fiscal recipt that was open. Before_error:{ex}"}

            if self.config_id.cbs_print_non_fiscal_receipt or has_negative_amount:
                # ******************** NON fiscal bill *************************
                if is_return:
                    fp.PrintText(f"RETUR AL: {is_return.ids}")
                for line in self.lines:
                    # we just write some info like a recipt
                    to_print_for_product = line.product_id.text_list_for_pos_fiscal_recipt()
                    prod_name = to_print_for_product[0]
                    all_prod_list = split_product_name_in_printer_lines(
                        prod_name, self.config_id.cbs_fiscal_printer_line_symbols if
                        self.config_id.cbs_fiscal_printer_line_symbols > 30 else 30)
                    prod_list = all_prod_list[:(self.config_id.cbs_receipt_product_name_max_lines if
                                                self.config_id.cbs_receipt_product_name_max_lines > 1 else 1)]
                    prod_list.extend(to_print_for_product[1:])
                    if len(prod_list) > 1:
                        for name in prod_list[:-1]:
                            fp.PrintText(f"{self.sanitise_txt_for_fiscal_print(name)}")
                    fp.PrintText(f"{self.sanitise_txt_for_fiscal_print(prod_list[-1])}")
                    fp.PrintText(f"{line.qty:0.1f}X{line.price_unit:0.2f}X tax={line.price_subtotal_incl:0.2f}")
                fp.PrintText(f"TOTAL: {self.amount_total:0.2f}")
                for payment in self.payment_ids:
                    if payment.payment_method_id.journal_id.type == 'cash':
                        fp.PrintText(f"PLATA prin casa: {payment.amount}lei")
                        if self.config_id.cbs_cash_drawer_open:
                            fp.CashDrawerOpen()
                    else:
                        fp.PrintText(f"PLATA NU prin casa: {payment.amount}lei")
            else:
                # ******************** fiscal bill *************************
                # ******** here the amount is at least 0.01
                first_sale_lines_after_storno = [x for x in is_sale]
                first_sale_lines_after_storno.extend([x for x in is_return])
                for line in first_sale_lines_after_storno:
                    # we can have more lines of product name, we are going to wirte this, and last one like a product
                    to_print_for_product = line.product_id.text_list_for_pos_fiscal_recipt()
                    prod_name = to_print_for_product[0]
                    all_prod_list = split_product_name_in_printer_lines(
                        prod_name, self.config_id.cbs_fiscal_printer_line_symbols if
                        self.config_id.cbs_fiscal_printer_line_symbols > 30 else 30)
                    prod_list = all_prod_list[:(self.config_id.cbs_receipt_product_name_max_lines if
                                                self.config_id.cbs_receipt_product_name_max_lines > 1 else 1)]
                    prod_list.extend(to_print_for_product[1:])
                    if len(prod_list) > 1:
                        for name in prod_list[:-1]:
                            fp.PrintText(f"{self.sanitise_txt_for_fiscal_print(name)}")
                    # the efective sale line
                    if line in is_sale:
                        # fp.SellPLUwithSpecifiedVAT("Article", Enums.OptionVATClass.VAT_Class_A, 0.01, 1)
                        # 0.01  =  unit price including vat
                        # 1 = quantity
                        fp.SellPLUwithSpecifiedVAT(prod_list[-1],
                                                   Enums.OptionVATClass.VAT_Class_A, line.price_unit,
                                                   line.qty)
                    else:  # is STORNO STORNO ( some + values and some - values with sum > 0.01) #    line in is_return
                        # the fiscal printer will write a storno before
                        # *******************   I must put storno *************************************
                        # StornoPLU(NamePLU=,OptionVATClass=,Price=,Quantity=,DiscAddP=,DiscAddV=,DiscNamed=,Category=,NamePLUextension=,AdditionalNamePLU=)                
                        # you are not allowd to have less than 0.01
                        # first time the + lines than the - ones, here we are the -, where given qty must be>1 and price <0
                        fp.StornoPLU(prod_list[-1],
                                     Enums.OptionVATClass.VAT_Class_A, (-1) * line.price_unit,
                                     line.qty * (-1))
                # cash payment:
                cash_payments = self.payment_ids.filtered(lambda r: r.payment_method_id.journal_id.type == 'cash')
                non_cash_payments = self.payment_ids.filtered(lambda r: r.payment_method_id.journal_id.type != 'cash')
                if len(cash_payments) > 1:
                    # the fiscal pirnter does only know the amont that was paid ( not also the rest)
                    for cash_payment in cash_payments:
                        fp.PrintText(f"Numerar:{cash_payment.amount}")
                if cash_payments:
                    cash_payment_amount = sum(cash_payments.mapped("amount"))
                    if cash_payment_amount < 0:
                        _logger.error("fiscal printer should give erorr because is a negative amount"
                                      f"{self=} {cash_payments=} {cash_payment_amount=}")
                    OptionPaymentType = 0
                    if self.config_id.cbs_cash_drawer_open:
                        fp.CashDrawerOpen()
                    fp.Payment(OptionPaymentType, cash_payment_amount)
                for payment in non_cash_payments:
                    # OptionPaymentType: 2 thichete 4 bonuri 5 voucher  6 credit 7 moderne 8 aletele 9 euro
                    OptionPaymentType = 1  # card  bank or what is defined
                    fp.Payment(OptionPaymentType, payment.amount)

            # print footer text for fiscal or not fiscal
            if self.config_id.receipt_footer:
                footer_line = split_product_name_in_printer_lines(
                    self.config_id.receipt_footer, self.config_id.cbs_fiscal_printer_line_symbols
                    if self.config_id.cbs_fiscal_printer_line_symbols > 30 else 30)
            else:
                footer_line = []
            for f_line in footer_line:
                fp.PrintText(self.sanitise_txt_for_fiscal_print(f_line))

            # barcode
            barcode_to_print = self.pos_reference.split()[-1]
            if self.config_id.cbs_barcode_to_print:
                fp.PrintBarcode("4", len(barcode_to_print), barcode_to_print)  # 4=CODE 39 thre resta re not working
#  - '0' - UPC A
#  - '1' - UPC E
#  - '2' - EAN 13
#  - '3' - EAN 8
#  - '4' - CODE 39
#  - '5' - ITF
#  - '6' - CODABAR
#  - 'H' - CODE 93
#  - 'I' - CODE 128
#            fp.CashPayCloseReceipt()
#            fp.PaperFeed()
# z                 fp.PrintDailyReport(Enums.OptionZeroing.Zeroing)
#                     print("fp.RawWrite GS I")
#                     fp.RawWrite(bytearray([0x1D, 0x49]))
#                     LF = bytearray([0x0A]).decode('utf-8')
#                     print("fp.RawRead")
#                     RES_ARR = fp.RawRead(0, LF)
#                     GS_INFO = RES_ARR.decode('utf-8').replace(LF, "")
#                     print("GS info: " + str(GS_INFO))
            fp.PrintText(barcode_to_print)

            if self.config_id.cbs_print_non_fiscal_receipt or has_negative_amount:
                fp.CloseNonFiscalReceipt()
            else:
                fp.CloseReceipt()

            this_receipt = fp.ReadLastAndTotalReceiptNum()
            last_nr = str(this_receipt.LastReceiptNum)
            last_total = str(this_receipt.TotalReceiptCounter)
            self.write({'cbs_fiscal_receipt_number': last_nr,
                        "cbs_before_ReadLastAndTotalReceiptNum": json.dumps(
                            {"last_nr": b_last_nr, "last_total": b_last_total}),
                        'cbs_ReadLastAndTotalReceiptNum': json.dumps({"last_nr": last_nr, "last_total": last_total})})
            if self.config_id.cbs_cut_after_print:
                fp.PaperFeed()
                fp.CutPaper()
            _logger.info(f'ok_printed_pos_order_id: ({self.id=}, {self.name=}, {barcode_to_print=})')
            return {'ok_printed_pos_order_id': (self.id, self.name, barcode_to_print)}
        except Exception as ex:
            _logger.error(f'error at fiscal_printer: {handle_exception(ex)}')
            return {'error': handle_exception(ex)}
