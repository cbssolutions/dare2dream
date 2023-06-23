/** @odoo-module **/
import Registries from "point_of_sale.Registries";
import NumpadWidget from "point_of_sale.NumpadWidget";
import ActionpadWidget from "point_of_sale.ActionpadWidget";
import ProductScreen from "point_of_sale.ProductScreen";
const { onMounted } = owl;

const toggleButton = (button, config, configField, removeSelectedMode = false) => {
    if (button && !config[configField]) {
        button.classList.add("disabled-mode");
        button.setAttribute("disabled", true);
        if (removeSelectedMode) button.classList.remove("selected-mode");
    }
};

const PosDisableAddProduct = (ProductScreen) =>
    class extends ProductScreen {
        _clickProduct(product) {
            if (this.env.pos.config.allow_add_product) {
                super._clickProduct(product);
            }
        }
        _setValue(val) {
            if (this.currentOrder.get_selected_orderline()) {
                if (this.env.pos.numpadMode === 'quantity' && this.env.pos.config.allow_qty) {
                    const result = this.currentOrder.get_selected_orderline().set_quantity(val);
                    if (!result) NumberBuffer.reset();
                } else if (this.env.pos.numpadMode === 'discount' && this.env.pos.config.allow_discount) {
                    this.currentOrder.get_selected_orderline().set_discount(val);
                } else if (this.env.pos.numpadMode === 'price' && this.env.pos.config.allow_price) {
                    var selected_orderline = this.currentOrder.get_selected_orderline();
                    selected_orderline.price_manually_set = true;
                    selected_orderline.set_unit_price(val);
                }
            }
        }
    };

Registries.Component.extend(ProductScreen, PosDisableAddProduct);


const PosDisableOrderEditNumpadWidget = (NumpadWidget) =>
    class extends NumpadWidget {
        setup() {
            super.setup();
            onMounted(() => this._onMounted());
        }

        getButtons() {
            return [
                { selector: ".mode-button:nth-child(4)", configField: "allow_qty", position: 4 },
                { selector: ".mode-button:nth-child(8)", configField: "allow_discount", position: 8 },
                { selector: ".mode-button:nth-child(12)", configField: "allow_price", position: 12 },
                { selector: ".input-button.numpad-backspace", configField: "allow_delete", position: 0 },
            ];
        }

        sendInput(key) {
            const numpadEl = document.querySelector(".numpad");
            const selectedModeEl = numpadEl.querySelector(".selected-mode");
        
            if (!selectedModeEl) return;
        
            const selectedModeIndex = Array.from(numpadEl.children).indexOf(selectedModeEl) + 1;
            const button = this.getButtons().find((element) => element.position === selectedModeIndex);
        
            if (button && this.env.pos.config[button.configField]) {
                this.trigger("numpad-click-input", { key });
            }
        }
        
        _onMounted() {
            this.getButtons().forEach(({ selector, configField }) => {
                const button = this.el?.querySelector(selector);
                toggleButton(button, this.env.pos.config, configField, true);
            });
        }
    };

Registries.Component.extend(NumpadWidget, PosDisableOrderEditNumpadWidget);

const PosDisableOrderEditActionWidget = (ActionpadWidget) =>
    class extends ActionpadWidget {
        setup() {
            super.setup();
            onMounted(() => this._onMounted());
        }

        _onMounted() {
            const buttons = [
                { selector: ".set-partner", configField: "allow_customer" },
                { selector: ".pay", configField: "allow_payment" },
            ];

            buttons.forEach(({ selector, configField }) => {
                const button = this.el?.querySelector(selector);
                toggleButton(button, this.env.pos.config, configField);
            });
        }
    };

Registries.Component.extend(ActionpadWidget, PosDisableOrderEditActionWidget);
