# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PosConfig(models.Model):
    _inherit = 'pos.config'
    allow_qty = fields.Boolean(default=True)
    allow_discount = fields.Boolean(default=True)
    allow_price = fields.Boolean(default=True)
    allow_customer = fields.Boolean(default=True)
    allow_delete = fields.Boolean(default=True)
    allow_payment = fields.Boolean(default=True)
    allow_add_product = fields.Boolean(default=True)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    allow_qty = fields.Boolean(related='pos_config_id.allow_qty',readonly=False)
    allow_price = fields.Boolean(related='pos_config_id.allow_price', readonly=False)
    allow_customer = fields.Boolean(related='pos_config_id.allow_customer', readonly=False)
    allow_discount = fields.Boolean(related='pos_config_id.allow_discount', readonly=False)
    allow_delete = fields.Boolean(related='pos_config_id.allow_delete', readonly=False)
    allow_payment = fields.Boolean(related='pos_config_id.allow_payment', readonly=False)
    allow_add_product = fields.Boolean(related='pos_config_id.allow_add_product', readonly=False)
    