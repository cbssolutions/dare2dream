odoo.define('pos_product_addons.product_addons', function (require) {
    "use strict";

      const{ useListener } = require("@web/core/utils/hooks");
      const NumberBuffer = require('point_of_sale.NumberBuffer');
      const PosComponent = require('point_of_sale.PosComponent');
      const Registries = require('point_of_sale.Registries');
      const { onChangeOrder, useBarcodeReader } = require('point_of_sale.custom_hooks');
      const { useState } = owl;
      var utils = require('web.utils');
      var round_pr = utils.round_precision;
      const ProductScreen = require('point_of_sale.ProductScreen');


      const PosProductAddons = ProductScreen => class extends ProductScreen {
         async _clickProduct(event) {
            if (!this.currentOrder) {
                this.env.pos.add_new_order();
            }

            const product = event.detail;

            const options = await this._getAddProductOptions(product);

            if (product){
                this.env.pos.get_addon_list(product.id);
            }
            // Do not add product if options is undefined.
            if (!options) return;
            // Add the product after having the extra information.
            this.currentOrder.add_product(product, options);
            NumberBuffer.reset();

        }



         _add_to_orderline(event) {

            if (event.target.className == 'addons-product' || event.target.className == 'addons-item'){
                    var order = this.env.pos.get_order();
                    var rounding = this.env.pos.currency.rounding;
                    if (event.target.className == 'addons-product'){
                        var addon_id = event.target.offsetParent.dataset.addonId;
                    }else{
                        var addon_id = event.target.dataset.addonId;
                    }
                    var addon_obj = this.env.pos.db.get_product_by_id([addon_id]);

                    if (addon_obj.taxes_id.length > 0){
                        if (this.env.pos.taxes_by_id[addon_obj.taxes_id[0]].include_base_amount == true){ //checks the tax included or excluded product
                            var addon_obj_tax = 0;
                            var tax_amt = this.env.pos.taxes_by_id[addon_obj.taxes_id[0]].amount;
                        }else{
                            var addon_obj_tax = this.env.pos.taxes_by_id[addon_obj.taxes_id[0]].amount;
                            var tax_amt = 0
                        }
                    }else{
                        var addon_obj_tax = 0;
                        var tax_amt = 0
                    }


                    var selected_line = order.selected_orderline;
                    if (!selected_line) {

                        alert('You have to select the corresponding product fist');

                    } else {

                        var total_price = 0.00;
                        for (var i = 0; i < selected_line.product.addon_ids.length; i++) {
                            if (addon_obj.id == selected_line.product.addon_ids[i]) {
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
                                addons[i]['total_without_including'] += round_pr((addon_obj.lst_price)/(1+(tax_amt/100)),rounding)
                                addons[i]['total_with'] += parseFloat(addon_obj.lst_price) + parseFloat(parseFloat(((parseFloat(addon_obj.lst_price)*parseFloat(addon_obj_tax))/100)))
                            }
                        }

                     if (add_prod_id.includes(addon_obj.id) == false){
                            addons.push({
                                    'addon_id': addon_obj.id,
                                    'addon_name': addon_obj.display_name,
                                    'addon_price_without': addon_obj.lst_price,
                                    'addon_price_with': round_pr((addon_obj.lst_price)+(((addon_obj.lst_price)*addon_obj_tax)/100),rounding),
                                    'addon_price_without_including':round_pr((addon_obj.lst_price)/(1+(tax_amt/100)),rounding),
                                    'addon_uom': addon_obj.uom_id[1],
                                    'addon_count': addon_obj.uom_id[0],
                                    'total_without': addon_obj.lst_price * addon_obj.uom_id[0],
                                    'total_without_including':round_pr((((addon_obj.lst_price)/(1+(tax_amt/100))) * (addon_obj.uom_id[0])),rounding),
                                    'total_with': (parseFloat(addon_obj.lst_price) + parseFloat(parseFloat(((parseFloat(addon_obj.lst_price)*parseFloat(addon_obj_tax))/100)))) * addon_obj.uom_id[0],
                                    'tax': addon_obj.taxes_id[0],
                                });
                            }
                    }
            }
        }

        };
       Registries.Component.extend(ProductScreen, PosProductAddons);
       return ProductScreen;


});