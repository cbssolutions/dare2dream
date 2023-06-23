from odoo import fields, models


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    origin = fields.Char(required=1)
