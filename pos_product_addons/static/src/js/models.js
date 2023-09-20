odoo.define('pos_product_addons.models', function(require) {
    "use strict";

    var {Order,
        Orderline,
        PosGlobalState
    } = require('point_of_sale.models');
    var utils = require('web.utils');
    var round_pr = utils.round_precision;
    const Registries = require('point_of_sale.Registries');


    const PosAddonsOrderline = (Orderline) => class PosSaleOrderline extends Orderline {

        // Initializes the object and adds an empty addon_items array property.
        constructor(obj, options) {
            super(...arguments);
            this.addon_items = this.addon_items || [];
        }
        // Overrides the export_as_JSON() method of the Orderline class to add the addon_items array to the exported JSON object.
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.addon_items = this.addon_items || [];
            return json;
        }
        // Overrides the can_be_merged_with() method of the Orderline class to prevent merging with an order line that has an add-on item.
        can_be_merged_with(orderline) {
            if (orderline.product.is_addon_include) {
                return false;
            } else {
                return super.can_be_merged_with(...arguments);
            }
        }

        // Overrides the export_for_printing() method of the Orderline class to add more properties to the exported object for printing receipts.
        export_for_printing() {
            return {
                id: this.id,
                quantity: this.get_quantity(),
                unit_name: this.get_unit().name,
                price: this.get_unit_display_price(),
                discount: this.get_discount(),
                product_name: this.get_product().display_name,
                product_name_wrapped: this.generate_wrapped_product_name(),
                price_lst: this.get_lst_price(),
                display_discount_policy: this.display_discount_policy(),
                price_display_one: this.get_display_price_one(),
                price_display: this.get_display_price(),
                price_with_tax: this.get_price_with_tax(),
                price_without_tax: this.get_price_without_tax(),
                price_with_tax_before_discount: this.get_price_with_tax_before_discount(),
                tax: this.get_tax(),
                product_description: this.get_product().description,
                product_description_sale: this.get_product().description_sale,
                orderline_id: this.id,
            };
        }

        //Computes the base price of the order line, including the prices of all add-on items.
        get_base_price() {
            var rounding = this.pos.currency.rounding;
            var total_addon_price = 0.0;
            if (this.addon_items.length) {
                _(this.addon_items).each(function(addon) {
                    total_addon_price += addon.addon_count * addon.addon_price_without
                });
            }
            return round_pr(((this.get_unit_price() * this.get_quantity()) + total_addon_price) * (1 - this.get_discount() / 100), rounding);
        }

        //Computes the total price of the order line, including tax and the prices of add-on items.
        get_price_with_tax() {
            var rounding = this.pos.currency.rounding;
            var total_addon_price = 0.0;
            if (this.addon_items.length) {
                _(this.addon_items).each(function(addon) {
                    total_addon_price += addon.addon_count * addon.addon_price_with
                });
            }
            var base_price_with_tax = this.get_all_prices().priceWithTax;
            var total_price_with_tax = base_price_with_tax + total_addon_price;
            return total_price_with_tax;
            //    return this.get_all_prices().priceWithTax;
        }

        get_display_price() {
            if (this.pos.config.iface_tax_included === 'total') {
                return this.get_price_with_tax();
            } else {
                return this.get_base_price();
            }
        }

        //Private method that maps the taxes of an order line to the taxes defined in the fiscal position of the order or the POS configuration.
        _map_tax_fiscal_position(tax, order = false) {
            var self = this;
            var current_order = order || this.pos.get_order();
            var order_fiscal_position = current_order && current_order.fiscal_position;
            var taxes = [];
            if (order_fiscal_position) {
                var tax_mappings = _.filter(order_fiscal_position.fiscal_position_taxes_by_id, function(fiscal_position_tax) {
                    return fiscal_position_tax.tax_src_id[0] === tax.id;
                });
                if (tax_mappings && tax_mappings.length) {
                    _.each(tax_mappings, function(tm) {
                        if (tm.tax_dest_id) {
                            var taxe = self.pos.taxes_by_id[tm.tax_dest_id[0]];
                            if (taxe) {
                                taxes.push(taxe);
                            }
                        }
                    });
                } else {
                    taxes.push(tax);
                }
            } else {
                taxes.push(tax);
            }
            return taxes;
        }

        //Computes the prices and taxes of the order line, including the prices of all add-on items.
        get_all_prices() {
            var self = this;
            var price_unit = this.get_unit_price() * (1.0 - (this.get_discount() / 100.0));
            var taxtotal = 0;
            var product = this.get_product();
            var taxes_ids = this.tax_ids || product.taxes_id;
            taxes_ids = _.filter(taxes_ids, t => t in this.pos.taxes_by_id);
            var taxes = this.pos.taxes;
            var taxdetail = {};
            var product_taxes = [];
            _(taxes_ids).each(function(el) {
                var tax = _.detect(taxes, function(t) {
                    return t.id === el;
                });
                product_taxes.push.apply(product_taxes, self._map_tax_fiscal_position(tax, self.order));
            });
            product_taxes = _.uniq(product_taxes, function(tax) {
                return tax.id;
            });
            var all_taxes = this.compute_all(product_taxes, price_unit, this.get_quantity(), this.pos.currency.rounding);
            var all_taxes_before_discount = this.compute_all(product_taxes, this.get_unit_price(), this.get_quantity(), this.pos.currency.rounding);
            _(all_taxes.taxes).each(function(tax) {
                taxtotal += tax.amount;
                taxdetail[tax.id] = tax.amount;
            });
            if (self.addon_items && self.addon_items.length != 0) {
                var tax_amount = 0.0
                var receipttax = {}
                var tax_compute = this.compute_all(product_taxes, self.product.lst_price, this.get_quantity(), this.pos.currency.rounding);
                _(tax_compute.taxes).each(function(tax) {
                    tax_amount += tax.amount;
                    receipttax[tax.id] = tax.amount;
                });
                var difference = taxtotal - tax_amount;
                taxtotal = taxtotal - difference
                var total_addon_tax = 0.0
                _(self.addon_items).each(function(addon) {
                    if (addon.tax) {
                        var addon_taxes = addon.tax
                        var tax_index = 0;
                        taxes.forEach(function(item, index) {
                            if (item.id == addon_taxes) {
                                tax_index = index;
                            }
                        });
                        var is_include = taxes[tax_index].include_base_amount;
                        if (is_include == true) {
                            var addon_tax = addon.total_without - addon.total_without_including;
                        } else {
                            var addon_tax = addon.total_with - addon.total_without;
                        }
                        total_addon_tax += addon_tax;
                        receipttax[addon.tax] = round_pr(addon_tax, self.pos.currency.rounding);
                    }
                });
                _(tax_compute.taxes).each(function(tax) {
                    receipttax[tax.id] += tax.amount;
                });
                taxtotal += round_pr(total_addon_tax, self.pos.currency.rounding)
                taxdetail = receipttax
            }
            return {
                "priceWithTax": all_taxes.total_included,
                "priceWithoutTax": all_taxes.total_excluded,
                "priceSumTaxVoid": all_taxes.total_void,
                "priceWithTaxBeforeDiscount": all_taxes_before_discount.total_included,
                "tax": taxtotal,
                "taxDetails": taxdetail,
            };
        }
        //Show the unit of measure of add-on items.
        get_addon_uom(id) {
            for (var i = 0; i <= this.addon_items.length; i++) {
                if (this.addon_items[i]['addon_id'] == id) {
                    return this.addon_items[i]['addon_uom']
                }
            }
        }
    }
    Registries.Model.extend(Orderline, PosAddonsOrderline);

     /**
     * Extends the PosGlobalState class to manage add-ons in a point of sale (POS) system.
     * @param {Class} PosGlobalState - The base class to extend from.
     * @returns {Class} - The extended class with additional methods for add-on management.
     */
    const PosAddonExtends = (PosGlobalState) => class PosAddonExtends extends PosGlobalState {
        /**
        * Retrieves a list of add-ons for a given product ID and displays them in the UI.
        * @param {number} product_id - The ID of the product to get the add-ons for.
        */
        get_addon_list(product_id) {
            var self = this;
            $('.addon-contents').empty();
            var product = self.env.pos.db.get_product_by_id(product_id);
            var element = [];
            if (product.product_ids.length) {
                var $addonpane = $('.addonpane');
                if (this.env.isMobile) {
                    $('.product-list-container').css("width", "70%");
                    $addonpane.css("visibility", "visible");
                    $addonpane.css("width", "30%");
                } else {
                    $('.product-list-container').css("width", "80%");
                    $addonpane.css("visibility", "visible");
                    $addonpane.css("width", "13.1%");
                }
                var display_name = '(' + product.display_name + ')'
                $('.sub-head').text(display_name).show('fast');
                for (var item = 0; item < product.product_ids.length; item++) {
                    var product_obj = self.env.pos.db.get_product_by_id([product.product_ids[item]]);
                    if (product_obj) {
                        element = product_obj.display_name;
                        var addonRow = $('<tr class="addon-contents row" style="width: 100%;">' +
                            '<td class="addons-item" style="width: 100%;" data-addon-id=' + product_obj.id + '>' +
                            '<div class="addons-product" style="display: inline-block; width: 50%;">' + element + '</div>' +
                            '<button class="add-button">+</button><button class="remove-button">-</button></td>' +
                            '</tr>');
                        // Add button click event handler
                        addonRow.find('.add-button').click(function(event) {
                            if (event.target.className == 'add-button') {
                                var order = self.env.pos.get_order();
                                var rounding = self.env.pos.currency.rounding;
                                if (event.target.className == 'add-button') {
                                    var addon_id = event.target.offsetParent.dataset.addonId;
                                } else {
                                    var addon_id = event.target.dataset.addonId;
                                }
                                var addon_obj = self.env.pos.db.get_product_by_id([addon_id]);
                                if (addon_obj.taxes_id.length > 0) {
                                    if (self.env.pos.taxes_by_id[addon_obj.taxes_id[0]].include_base_amount == true) { //checks the tax included or excluded product
                                        var addon_obj_tax = 0;
                                        var tax_amt = self.env.pos.taxes_by_id[addon_obj.taxes_id[0]].amount;
                                    } else {
                                        var addon_obj_tax = self.env.pos.taxes_by_id[addon_obj.taxes_id[0]].amount;
                                        var tax_amt = 0
                                    }
                                } else {
                                    var addon_obj_tax = 0;
                                    var tax_amt = 0
                                }
                                var selected_line = order.selected_orderline;
                                if (!selected_line) {
                                    alert('You have to select the corresponding product fist');
                                } else {
                                    var total_price = 0.00;
                                    for (var i = 0; i < selected_line.product.product_ids.length; i++) {
                                        if (addon_obj.id == selected_line.product.product_ids[i]) {
                                            total_price += parseFloat(addon_obj.lst_price); // Change the value of the price
                                        }
                                    }
                                    var addons = order.selected_orderline.addon_items;
                                    var has_already = false;
                                    var add_prod_id = []
                                    for (var i = 0; i < addons.length; i++) {
                                        add_prod_id.push(addons[i]['addon_id'])
                                        if (addons[i]['addon_id'] == addon_obj.id) {
                                            has_already = true;
                                            addons[i]['addon_count'] += 1
                                            addons[i]['total_without'] += addon_obj.lst_price
                                            addons[i]['total_without_including'] += round_pr((addon_obj.lst_price) / (1 + (tax_amt / 100)), rounding)
                                            addons[i]['total_with'] += parseFloat(addon_obj.lst_price) + parseFloat(parseFloat(((parseFloat(addon_obj.lst_price) * parseFloat(addon_obj_tax)) / 100)))
                                        }
                                    }
                                    if (add_prod_id.includes(addon_obj.id) == false) {
                                        addons.push({
                                            'addon_id': addon_obj.id,
                                            'addon_name': addon_obj.display_name,
                                            'addon_price_without': addon_obj.lst_price,
                                            'addon_price_with': round_pr((addon_obj.lst_price) + (((addon_obj.lst_price) * addon_obj_tax) / 100), rounding),
                                            'addon_price_without_including': round_pr((addon_obj.lst_price) / (1 + (tax_amt / 100)), rounding),
                                            'addon_uom': addon_obj.uom_id[1],
                                            'addon_count': addon_obj.uom_id[0],
                                            'total_without': addon_obj.lst_price * addon_obj.uom_id[0],
                                            'total_without_including': round_pr((((addon_obj.lst_price) / (1 + (tax_amt / 100))) * (addon_obj.uom_id[0])), rounding),
                                            'total_with': (parseFloat(addon_obj.lst_price) + parseFloat(parseFloat(((parseFloat(addon_obj.lst_price) * parseFloat(addon_obj_tax)) / 100)))) * addon_obj.uom_id[0],
                                            'tax': addon_obj.taxes_id[0],
                                        });
                                    }
                                }
                            }
                        });
                        // Remove button click event handler
                        addonRow.find('.remove-button').click(function(event) {
                            if (event.target.className == 'remove-button') {
                                var addonId = $(this).closest('.addons-item').data('addon-id');
                                var order = self.env.pos.get_order();
                                var selectedLine = order.selected_orderline;

                                if (selectedLine) {
                                    var addons = selectedLine.addon_items;
                                    for (var i = 0; i < addons.length; i++) {
                                        if (addons[i]['addon_id'] == addonId) {
                                            if (addons[i]['addon_count'] > 1) {
                                                addons[i]['addon_count'] -= 1; // Decrease the addon count by 1
                                                addons[i]['total_without'] -= addons[i]['addon_price_without'];
                                                addons[i]['total_without_including'] -= addons[i]['addon_price_without_including'];
                                                addons[i]['total_with'] -= addons[i]['addon_price_with'];
                                            } else {
                                                addons.splice(i, 1); // Remove the addon from the addons array if count becomes 0
                                            }
                                            break;
                                        }
                                    }
                                }
                            }
                        });
                        $('.addons-table').append(addonRow);
                    }
                }
            } else {
                self.hide_addons()
            }
        }

        // Method to hide the add-on
        hide_addons() {
            var $layout_table = $('.product-list-container');
            $layout_table.removeAttr("width");
            $layout_table.css("width", "100%");
            $('.addonpane').css("visibility", "hidden");
        }
    }
    Registries.Model.extend(PosGlobalState, PosAddonExtends);

    // Define a new model that extends the existing Order model, with additional functionality for calculating total without tax.
    const PosAddonOrderModel = (Order) => class PosAddonOrderModel extends Order {
        // Override the get_total_without_tax method to calculate the total amount without tax, including any addons.
        get_total_without_tax() {
            return round_pr(this.orderlines.reduce((function(sum, orderLine) {
                var total_addon_price = 0.0;
                // If the orderline has any addons, iterate over each one and calculate the total addon price.
                if (orderLine.addon_items.length) {
                    _(orderLine.addon_items).each(function(addon) {
                        // Find the tax index for the addon.
                        var taxes_list = self.posmodel.taxes;
                        var addon_tax_list = addon.tax
                        var tax_indexs = 0;
                        taxes_list.forEach(function(items, index) {
                            if (items.id == addon_tax_list) {
                                tax_indexs = index;
                            }
                        });
                        // Determine if the tax is included in the base amount or not.
                        var is_includes = taxes_list[tax_indexs].include_base_amount;
                        if (is_includes == true) {
                            var addon_price_withouts = addon.addon_price_without_including;
                        } else {
                            var addon_price_withouts = addon.addon_price_without;
                        }
                        // Add the total addon price to the existing total.
                        total_addon_price += addon.addon_count * addon_price_withouts
                    });
                }
                // Return the sum of the total addon price and the orderline price without tax.
                return sum + total_addon_price + orderLine.get_price_without_tax();
            }), 0), this.pos.currency.rounding);
        }
    }

    Registries.Model.extend(Order, PosAddonOrderModel);
});