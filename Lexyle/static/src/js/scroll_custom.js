odoo.define('Lexyle.phone_validation', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.websiteForm.include({
        /**
         * Override the _onSubmit to add custom phone number validation
         */
        _onSubmit: function (ev) {
            const phoneInput = this.$target.find('input[name="phone"]');
            const phoneNumber = phoneInput.val().replace(/\D/g, ''); // Remove non-digits

            // Check if phone number is exactly 10 digits
            if (phoneInput.length && phoneNumber.length !== 10) {
                ev.preventDefault();
                phoneInput.addClass('is-invalid');
                alert("Phone number must be exactly 10 digits.");
                return false;
            } else {
                phoneInput.removeClass('is-invalid');
            }

            // Call the original submit method
            this._super.apply(this, arguments);
        }
    });
});
