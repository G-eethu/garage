
frappe.ui.form.on('Appointment', {
    refresh: function(frm) {
        frm.set_df_property('customer_email', 'reqd', 0);
        frm.set_df_property('customer_phone_number', 'reqd', 1);
    }
});