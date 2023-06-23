# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "Product no valuation ",
    'summary': """is hiding the valuation of products
    """,
    'category': 'Inventory/Inventory',
    'sequence': 300,
    'version': '16.0.1.0.0',
    "website": "https://cbssolutions.ro",
    "author": "dev@cbssolutions.ro",
    "maintainers": ["dev@cbssolutions.ro"],
    "license": "OPL-1",
    "development_status": "Mature",
    'depends': ['stock_account'],
    'data': [
        'views/stock_valuation_layer_views.xml',
    ],
    'installable': True,
    'application': False,
    'assets': {
    }
}
