# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).
from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = ['product.product']

    def text_after_ok_scan(self, location_id=False, location_dest_id=False):
        """ after scan add also the eee category if is the case
        """
        before_after_scan_text_list = super().text_after_ok_scan(location_id, location_dest_id)
        eee = "NO EEE cateogry"
        if self.eee_category_id:  # and location_id.usage == "supplier":
            eee = (f"EEE: {self.eee_category_id.categorie_eee}_{self.eee_category_id.name}; "
                   f"TAX={self.eee_tax}; ")
        before_after_scan_text_list.append(eee)
        return before_after_scan_text_list
