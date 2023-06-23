# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "stock show more details ",
    'summary': """this module is showing you the id and state of stock_moves, stock_move_lines
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
        "views/stock_move_views.xml",
        "views/stock_move_line_views.xml",
        "views/stock_quant_views.xml",
    ],
    'installable': True,
    'application': False,
    'assets': {
    }
}
