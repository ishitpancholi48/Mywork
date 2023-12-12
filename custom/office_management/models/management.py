import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date
from odoo.exceptions import ValidationError



class OfficeStaff(models.Model):
    _name = "office.staff"
    _description = "This is management of office"

    name = fields.Char(string="Name", size=50)
    partner_id = fields.Many2one(
        comodel_name='new.employee',
        string='Partner_Id',
        help="this is sale order partner id"
    )
    country_id = fields.Many2one('res.country', string="Country_id")
    age = fields.Integer(string="Age", compute="_compute_age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    gender = fields.Selection([
        ('other', 'Other'),
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='other')
    city = fields.Selection([
        ('rajkot', 'Rajkot'),
        ('ahmedabad', 'Ahmedabad'),
        ('vadodara', 'Vadodara'),
        ('surat', 'Surat'),
    ], string="City")
    country = fields.Char(string="Country")
    boolean_checkbox = fields.Boolean(string="checkbox", default=False)
    state = fields.Selection([
        ('draft', 'Draft'), ('confirm', 'Confirm'),
        ('done', 'Done'), ('cancel', 'Cancel'),
    ], default='draft', string='State')
    many2many = fields.Many2many(
        comodel_name='company.service',
        string='Selection'
    )

    # Wizard Function
    def wiz_open(self):
        return {'type': 'ir.actions.act_window',
                'res_model': 'office.staff.wizard',
                'view_mode': 'form',
                'target': 'new'}
    # search method()

    def check_orm(self):
        create_val = self.env['college.university'].create({
            'studentname': 'vidhi',
            'email': 'vidhi@gmail.com',
            'mobile': '701695631',
            'city': 'rajkot',

        })
        print('create_val....', create_val.id)

        search_val = self.env['college.university'].search([('city', '=', 'gandhinagar')])
        print("search count..........", search_val)
        for rec in search_val:
            print("name is...", rec.studentname, "gender is...", rec.gender, "city is...", rec.city, "dob", rec.dob,
                  "Stream is...", rec.diploma_field)

    def main_method(self):
        employee_name = "Aniket Pancholi"
        employee_age = "25"
        employee_dob = datetime.datetime(1997, 8, 4)
        employee_mobile = "9824874668"
        employee_email = "aniket@gmail.com"
        employee_gender = "male"
        self.other_method(employee_name, employee_age, employee_dob, employee_mobile, employee_email, employee_gender)

    def other_method(self, employee_name, employee_age, employee_dob, employee_mobile, employee_email, employee_gender):
        self.name = employee_name
        self.age = employee_age
        self.dob = employee_dob
        self.mobile = employee_mobile
        self.email = employee_email
        self.gender = employee_gender

    # =======================================================================
    # browse method()
    #     search_val = self.env['office.staff'].browse([92,95,89,116,96])
    #     for rec in search_val:
    #         print('full name.....',rec.name,'gender.....',rec.gender)
    #     search_val = self.env.ref('office_management.office_staff_form')
    #     print('search_val......',search_val)

    # @api.constrains('email')
    # def Email(self):
    #     if not self.email:
    #         raise ValidationError(_("Enter the Email id"))

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    def button_action(self):
        self.boolean_checkbox = True

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

    @api.onchange('country_id')
    def _onchange_name(self):
        self.country = self.country_id.name
