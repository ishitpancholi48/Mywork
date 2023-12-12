from odoo import models, fields


class OfficeStaffWizard(models.TransientModel):
    _name = "office.staff.wizard"
    _description = "This wizard is update for name change of employee management"

    name = fields.Char(string="Employee Name")



    def update_info_funs(self):
        print("Updated.....")
        self.env['office.staff'].browse(self._context.get('active_ids')).update({"name": self.name})

        return True