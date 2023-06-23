# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "No more Link tracker menul campains",
    'summary': """is hiding (sets active=false) to the link tracker menu from utm module ( campain tracker)
    """,
    'category': 'Technical',
    'sequence': 300,
    'version': '16.0.1.0.0',
    "website": "https://cbssolutions.ro",
    "author": "dev@cbssolutions.ro",
    "maintainers": ["dev@cbssolutions.ro"],
    "license": "OPL-1",
    "development_status": "Mature",
    'depends': ['utm'],
    'data': [
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': False,
    'assets': {
    }
}
