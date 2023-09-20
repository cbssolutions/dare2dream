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
import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_addon_include = fields.Boolean(string='Has Add-ons',
                                      help="Check if the product has addons")
    is_addons = fields.Boolean(string='Is Add-ons',
                               help="Check if the product is addon")
    product_ids = fields.Many2many('product.product', string='Addons',
                                   domain="[('is_addons', '=', True)]")

    @api.onchange('is_addons', 'is_addon_include')
    def _onchange_is_addons(self):
        """The function makes the corresponding product as 'Available In POS'
        if either 'is_addon' or 'is_addon_include' fields are true'"""
        if self.is_addons or self.is_addon_include:
            self.available_in_pos = True

