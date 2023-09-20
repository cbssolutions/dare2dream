    # -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Sayanth M K (odoo@cybrosys.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0
#    (OPL-1) It is forbidden to publish, distribute, sublicense, or
#    sell copies of the Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
#    OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
#    THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
###############################################################################
{
    'name': "Product Add-ons in POS",
    'version': '16.0.1.1.0',
    'category': 'Point of Sale',
    'summary': """ Add product addons(flavour) to the product in POS.""",
    'description': """This module brings an option to add/remove
                      addon(extension) cost of the products in the
                      point of sale. You can configure the addon as 
                      a product, so it brings all the product features
                      to the add-on. It is simple to handle by choosing
                      the add-on from the side bar menu which doesn't
                      affect your product screen.It adds the cost of the
                      add-on to the product price and displays the add-on cost
                      on the receipt.""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'images': ['static/description/banner.png'],
    'depends': ['pos_restaurant', 'point_of_sale', 'web'],
    'data': [
        'views/product_template_views.xml',
        'views/pos_order_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_product_addons/static/src/js/models.js',
            'pos_product_addons/static/src/js/orderline.js',
            'pos_product_addons/static/src/js/product_addons.js',
            'pos_product_addons/static/src/css/product_addons_style.css',
            'pos_product_addons/static/src/screens/addon_product.xml',
            'pos_product_addons/static/src/screens/addon_product_details.xml',
            'pos_product_addons/static/src/screens/addon_product_receipt.xml',
            'https://riversun.github.io/jsframe/jsframe.js'
        ]
    },
    'license': 'OPL-1',
    'price': 19.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False
}
