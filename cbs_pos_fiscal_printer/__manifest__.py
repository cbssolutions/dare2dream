# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "cbs POS fiscal printer",
    'summary': """
With this module, you are going to be able to use in Point_of_sale a Romainan ( and also other countries) Fiscal Printner.

The hardware printer must be connected to a device (windows/linux/android) thru lan/usb.. that runs ZFPLAB Server

This module is functioning with Tremol Fiscal cash registers/ fiscal printers.

You must configure per POS the ip and port of the ZFPLAB Server.

Modul pentru interconectare case de marcat fiscale/ imprimate fiscale la POS.
Edit added fields: Point of Sale/ Dashboard/Point of sale / Edit

If the amount is negative, will print a non fiscal receipt with what was received

For this module to work, the fisca printer must be accessed from the odoo server ( it must have a domain/port accesible by odoo server).

1.0.1 able to print at fiscal printer also from backend ( if somehow not prited from pos); and if no cbs_fiscal_receipt_number
1.1.0 also test print in config
1.2.0 if you make a storno, and also sell other products and the amount is positive will print a receipt only with
    difference (the products must have same vat not viefied by this module). The stono line price will be with -.
    Now exist also Operator Password for fiscal printer/casher.
    Option in setting to PrintDailyRepot  Z ot X.
1.2.1 better error at pos test; and also fucntiong with any ip for tremol server

Future:
- to make also to work directly from javascript ( or other version for javascript, when the server is installed locally and also the printer, and odoo server can not access them)
- to make it work only from some ip/or the ip where is the fiscal printer
    """,
    'category': 'Sales/Point of Sale',
    'sequence': 300,
    'version': '16.0.1.2.1',
    "website": "https://cbssolutions.ro",
    "author": "dev@cbssolutions.ro",
    "maintainers": ["dev@cbssolutions.ro"],
    "license": "OPL-1",
    "development_status": "Mature",
    'depends': ['point_of_sale', ],
    'data': [
             'views/pos_config_views.xml',
             'views/pos_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'external_dependencies': {
       'python': ['unidecode'],
    },
    'assets': {
        'point_of_sale.assets': [
            'cbs_pos_fiscal_printer/static/src/js/*.js']
    },
}
