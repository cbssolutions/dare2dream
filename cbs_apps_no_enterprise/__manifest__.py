# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "No more enterpriese app or shop ",
    'summary': """is hiding the buttons becuase they can destory the database if used
    all app menu is hiden for nor uid=2, for uid=2 is in group settings base.group_system

1.1.0 also apps menu not visible to not administator settings
    """,
    'category': 'Technical',
    'sequence': 300,
    'version': '16.0.1.1.0',
    "website": "https://cbssolutions.ro",
    "author": "dev@cbssolutions.ro",
    "maintainers": ["dev@cbssolutions.ro"],
    "license": "OPL-1",
    "development_status": "Mature",
    'depends': ['base'],
    'data': [
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': False,
    'assets': {
    }
}
