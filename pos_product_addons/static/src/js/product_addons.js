odoo.define('pos_product_addons.product_addons', function (require) {
    "use strict";

  const NumberBuffer = require('point_of_sale.NumberBuffer');
  const Registries = require('point_of_sale.Registries');
  var utils = require('web.utils');
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
  };

   Registries.Component.extend(ProductScreen, PosProductAddons);
   return ProductScreen;
});