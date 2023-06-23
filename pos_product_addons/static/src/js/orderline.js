odoo.define('pos_product_addons.orderline', function(require) {
    'use strict';

    const Orderline = require('point_of_sale.Orderline');
    const Registries = require('point_of_sale.Registries');

    const PosOrderLineAddons = Orderline =>
        class extends Orderline {
            /**
             * @override
             */
            selectLine() {
                const line = this.props.line; // the orderline
                this.trigger('select-line', { orderline: line });
                this.env.pos.get_addon_list(line.product.id);
                super.selectLine();
            }
        };

    Registries.Component.extend(Orderline, PosOrderLineAddons);
    return Orderline;
});
