from erpnext.crm.doctype.appointment.appointment import Appointment
import frappe


class CustomAppointment(Appointment):

    def find_lead_by_mobile(self):
        pass

    def find_customer_by_mobile(self):
        pass

    def before_insert(self):
        # Your custom logic
        super().before_insert()

    def after_insert(self):
        # Replace the standard behavior
        if self.party:
            self.auto_assign()
            self.create_calendar_event()
        else:
            self.create_lead_and_link()
            self.status = "Open"
            self.auto_assign()
            self.create_calendar_event()