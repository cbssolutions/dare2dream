# Copyright 2023 cbssolutions.ro
# License OPL-1.0 or later (Odoo Proprietary License)
# (https://www.odoo.com/documentation/16.0/legal/licenses.html#odoo-apps).

from odoo.exceptions import ValidationError
from odoo import api,models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.constrains('groups_id')
    def _check_only_admin_in_group_system(self):
        group_system = self.env.ref('base.group_system')
        for rec in self.filtered(lambda r: r.id != 2):
            if group_system in rec.groups_id:
                raise ValidationError(f'CBS: for user ({rec.id}, {rec.name}) that is not admin you '
                                      'can not have system rights')


class ResGroups(models.Model):
    _inherit = "res.groups"

    @api.constrains('users')
    def _check_only_admin_in_group_system(self):
        group_system = self.env.ref('base.group_system')
        for rec in self.filtered(lambda r: r == group_system):
            if len(rec.users.ids) != 1 or rec.users.id != 2:
                raise ValidationError(f'CBS: for group ({rec.id}, {rec.name}) that you can only have one '
                                      f'user that is the admin; not more not less {rec.users=}')
