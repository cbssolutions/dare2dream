// we are modification the printReceipt function to work with our module

// to replace/modify a function
//import {formatFloat as originalFormatFloat} from 'web/static/src/views/fields/formatters.js';
//export function formatFloat(value, options = {}) { 
//    // Your custom code here 
//    // You can call the original function using originalFormatFloat() 
//    }

odoo.define('cbs_pos_fiscal_printer.CBS_Print_fiscal_device', function (require) {
    'use strict';
    const Registries = require('point_of_sale.Registries');

    var point_of_sale_ReceiptScreen = require('point_of_sale.ReceiptScreen');

    var cbs_modification_print_fiscal = (point_of_sale_ReceiptScreen) => class cbs_modification_print_fiscal extends point_of_sale_ReceiptScreen {
        async printReceipt() {
//             alert("zzzz")
            const order = this.currentOrder;
//            const partner = order.get_partner();
            const orderName = order.get_name();
//            const orderPartner = { email: this.orderUiState.inputEmail, name: partner ? partner.name : this.orderUiState.inputEmail };
            const order_server_id = this.env.pos.validated_orders_name_server_id_map[orderName];
            if (!order_server_id ){
                this.showPopup('ErrorPopup', {
                    title: this.env._t('Unsynced order'),
                    body: this.env._t('This order is not yet synced to server. We can not print it; .'),
                });
                return
            }
            
             let self = this;
             let x = this.rpc({
                    model: 'pos.order',
                    method: 'cbs_print_at_fiscal_server',
                    args: [[order_server_id], orderName],
                }).then((value) => {
                    if (value.error) {
                        this.showPopup('ErrorPopup', {
                            title: this.env._t('Returned error from print function from server:'),
                            body: this.env._t(value.error),
                        });
                    } else {
                      //  alert('done'+value); // here all is ok, the recipt was printed
                        this.currentOrder._printed = true;
                        }
                }).catch((error)=> {
                    this.showPopup('ErrorPopup', {
                        title: 'Error from server at print:',
                        body: error.message +';'+ error.message.data.message,
                    });
                });

        };
    }
//             async printReceipt() {
//                 alert("will print receipt");
//                 const isPrinted = await this._printReceipt();
//                 if (isPrinted) {
//                     this.currentOrder._printed = true;
//                 }
//             }
    
Registries.Component.extend(point_of_sale_ReceiptScreen, cbs_modification_print_fiscal); 
// the class can be also in other registries like  ( you must see where is created )
//Registries.Model.extend(PosGlobalState, PosEpsonPosGlobalState);
})
