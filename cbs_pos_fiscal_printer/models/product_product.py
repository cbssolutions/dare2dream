# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = ['product.product']

    def text_list_for_pos_fiscal_recipt(self):
        """ function to be inherited if you extend it and need also other info
        each text from list is going to be trunckated in conformity with fiscal printer
        """
        self.ensure_one()
        return [self.name]
