{
    'name': 'POS Disable Options',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Enable or disable specific POS functionalities for better access control',
    'depends': ['point_of_sale'],
    'author': 'Dustin Mimbela',
    "data"  :  ['views/pos_disable_options_view.xml'],
    'assets': {
        'point_of_sale.assets': [
            'pos_disable_options/static/src/js/pos_disable_options.js',
            'pos_disable_options/static/src/css/disable.css',
        ],
    },
    "license": "LGPL-3",
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
