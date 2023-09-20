# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
{
    'name': "if you do not use product.product(variants) and only product template",
    'summary': """
    if you do not use product variants ( colors/size of products)
    this module is giving you a link to product_template from product_product.
    is used because all your modification will be set on product.template.
    the product.product menu is invisible, but you can get to it from other objectj
v 1.1.0 ok just with product dependency & auto install
v 1.2.0 product_product tree view group by product_template
        """,
    'category': 'Technical',
    'sequence': 300,
    'version': '16.0.1.2.0',
    "website": "https://cbssolutions.ro",
    "author": "dev@cbssolutions.ro",
    "maintainers": ["dev@cbssolutions.ro"],
    "license": "OPL-1",
    "development_status": "Mature",
    'depends': ['product'],
    'data': [
        'views/product_product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'assets': {
    }
}
