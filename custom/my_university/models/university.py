import datetime
from odoo import models, fields, api


class CollegeUniversity(models.Model):
    _name = "college.university"
    _description = "Information of college university"
    _rec_name = "studentname"

    studentname = fields.Char(string="Studentname", size=50, help="Enter Student Full Name",)
    age = fields.Integer(string="age")
    dob = fields.Date(string="DOB")
    gender_student = fields.Selection([
        ("male", 'Male'),
        ("female", 'Female')
    ])
    mobile = fields.Char(string="mobile")
    email = fields.Char(string="Email", default="example@gmail.com")
    city = fields.Selection([
        ("rajkot", "Rajkot"),
        ("ahmedabad", "Ahmedabad"),
        ("surat", "Surat"),
        ("gandhinagar", "Gandhinagar"),
        ('vadodara', 'Vadodara'),
    ], string="City")
    diploma_field = fields.Selection([
        ("informationtechnology", 'Information Technology'),
        ("electrical", 'Electrical'),
        ("Mechanical", 'mechanical'),
        ("automobile", 'Automobile'),
        ("computerengineering", 'Computer Engineering')

    ], string='Stream', help="Select your field")
    state = fields.Selection([
        ('draft', 'Draft'), ('confirm', 'Confirm'),
        ('done', 'Done'), ('cancel', 'Cancel'),
    ], default='draft', string='State')

    def main_method(self):
        student_name = "Mithilesh"
        age = "28"
        mobile = "1234567/"
        gender = "male"
        self.other_method(student_name, age, mobile, gender)

    def other_method(self, student_name, age, mobile, gender):
        self.studentname = student_name
        self.age = age
        self.mobile = mobile
        self.gender = gender

    def test_record(self):
        partner = self.env['office.staff'].search([])
        for rec in partner:
            partner_mapped = rec.mapped(lambda partnerinfo: {'name': partnerinfo.name, 'mobile': partnerinfo.mobile,'email': partnerinfo.email})
            print(partner_mapped)

        search_val = self.env['office.staff'].search([("boolean_checkbox", '=', True)])
        for rec in search_val:
            print("name is...", rec.name, )

        filter_val = self.env['office.staff'].search([])
        filter_vals = filter_val.filtered(lambda o: o.name)
        print("filter_vals is ....", filter_vals)

        sort_val = self.env['office.staff'].search([])
        for rec in sort_val:
            sort_vals = rec.sorted(lambda o: o.name, reverse=True)
            print("sort_vals is....", sort_vals)

    # Wizard Function
    def wiz_open(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'college.university.wizard',
                'view_mode': 'form',
                'target': 'new'}

    def action_confirm(self):
        self.state = 'confirm'

    def action_draft(self):
        self.state = 'draft'

    def action_done(self):
        self.state = 'done'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Everything is done...',
                'type': 'rainbow_man',
            }
        }

    def action_cancel(self):
        self.state = 'cancel'
