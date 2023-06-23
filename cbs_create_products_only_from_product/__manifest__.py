# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "let you create products only with add in product ",
    'summary': """this module disables the create button from transfers
    at stock_move from picking many2many, you can not create products
      """,
    'category': 'Inventory/Inventory',
    'sequence': 300,
    'version': '16.0.1.0.0',
    "website": "https://cbssolutions.ro",
    "author": "dev@cbssolutions.ro",
    "maintainers": ["dev@cbssolutions.ro"],
    "license": "OPL-1",
    "development_status": "Mature",
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'assets': {
    }
}
