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
import psycopg2
from odoo import api, models, tools, _

_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    """To write the product addons to backend """
    _inherit = 'pos.order'

    # added by cbs to order the addons under product
    @api.model
    def _order_fields(self, ui_order):
        order_fields = super(PosOrder, self)._order_fields(ui_order)
        order_fields['table_id'] = ui_order.get('table_id', False)
        order_fields['customer_count'] = ui_order.get('customer_count', 0)
        order_fields['multiprint_resume'] = ui_order.get('multiprint_resume', False)
        return order_fields


    @api.model
    def _process_order(self, order, draft, existing_order):
        """Create or update an pos.order from a given dictionary.

        :param dict order: dictionary representing the order.
        :param bool draft: Indicate that the pos_order is not validated yet.
        :param existing_order: order to be updated or False.
        :type existing_order: pos.order.
        :returns: id of created/updated pos.order
        :rtype: int
        """
        order = order['data']
        pos_session = self.env['pos.session'].browse(order['pos_session_id'])
        if pos_session.state == 'closing_control' or pos_session.state == 'closed':
            order['pos_session_id'] = self._get_valid_session(order).id

        addons = self.add_addons(order)  # adding the addons to the order
        if not existing_order:
            for nr, line_to_add in enumerate(order['lines']):
                line_to_add[2]['cbs_prod_nr'] = nr
            pos_order = self.create(self._order_fields(order))
            for cbs_prod_nr, rec in enumerate(addons):
                new_addon = rec[2]
                x = new_addon['tax_ids'][0]
                y = x[2]
                if y:
                    pos_taxes = self.env['account.tax'].browse(y[0])
                    if pos_taxes.price_include:
                        vals = [(0, 0, {
                            'full_product_name': new_addon['full_product_name'],
                            'price_unit': new_addon['price_unit'],
                            'product_id': new_addon['product_id'],
                            'product_uom_id': new_addon['product_uom_id'],
                            'price_subtotal': new_addon[
                                'total_without_including'],
                            'price_subtotal_incl': new_addon[
                                'price_subtotal_incl'],
                            'tax_ids': pos_taxes
                        })]
                        pos_order.write({'lines': vals})
                    else:
                        vals = [(0, 0, {
                            'qty': new_addon['qty'],
                            'full_product_name': new_addon['full_product_name'],
                            'price_unit': new_addon['price_unit'],
                            'product_id': new_addon['product_id'],
                            'product_uom_id': new_addon['product_uom_id'],
                            'price_subtotal': new_addon['price_subtotal'],
                            'price_subtotal_incl': new_addon[
                                'price_subtotal_incl'],
                            'tax_ids': pos_taxes
                        })]
                        pos_order.write({'lines': vals})
                else:
                    pos_order.write({
                        'lines': [rec],
                    })

        else:
            pos_order = existing_order
            pos_order.lines.unlink()
            order['user_id'] = pos_order.user_id.id
            pos_order.write(self._order_fields(order))

        pos_order = pos_order.with_company(pos_order.company_id)
        self = self.with_company(pos_order.company_id)
        # till here we have added the addon lines
        self._process_payment_lines(order, pos_order, pos_session, draft)

        if not draft:
            try:
                pos_order.action_pos_order_paid()
            except psycopg2.DatabaseError:
                # do not hide transactional errors, the order(s) won't be saved
                raise
            except Exception as e:
                _logger.error('Could not fully process the POS Order: %s',
                              tools.ustr(e))
            pos_order._create_order_picking()

        if pos_order.to_invoice and pos_order.state == 'paid':
            pos_order.action_pos_order_invoice()

        return pos_order.id

    def add_addons(self, order):
        """ Return addon products details.
        :param order: dictionary representing the order.
        :returns: Product details.
        :rtype: list
        """
        addon_list = [rec[2] for rec in order.get('lines')]  # here are the product_lines what can have or not have in them addon_items
        main = []
        final_adds = []
        for cbs_prod_nr, adds in enumerate(addon_list):
            if adds.get('addon_items'):
                for items in adds['addon_items']:
                    final_adds.append((0, 0, {
                        'cbs_prod_nr': cbs_prod_nr,  # used to know for what product is
                        'cbs_is_addon': True,
                        'qty': items['addon_count'],
                        'full_product_name': items['addon_name'],
                        'price_unit': items['addon_price_without'],
                        'product_id': items['addon_id'],
                        'product_uom_id': items['addon_uom'],
                        'price_subtotal': items['total_without'],
                        'price_subtotal_incl': items['total_with'],
                        'total_without_including': items[
                            'total_without_including'],
                        'tax_ids': [
                            [6, False,
                             [items['tax']] if items.get('tax') else []]]
                    }))
                main.append(final_adds)
        return final_adds
