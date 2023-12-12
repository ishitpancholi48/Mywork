from odoo import models, fields


class CollegeUniversityWizard(models.TransientModel):
    _name = "college.university.wizard"
    _description = "this is wizard for update college university"

    studentname = fields.Char(string="Studentname", size=50, help="Enter Student Full Name")
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

    ], string='Stream')

    def update_info_fun(self):
        print("updated...........")
        self.env['college.university'].browse(self._context.get('active_ids')).update(
            {'studentname': self.studentname, 'age': self.age, 'dob': self.dob, 'gender_student': self.gender_student,
             'mobile': self.mobile, 'email': self.email, 'city': self.city, 'diploma_field': self.diploma_field})
        return True


class CollegeUniversityWizardLine(models.TransientModel):
    _name = 'college.university.wizard.line'

    connecting_field = fields.Many2one('college.university', string="Staff Id")
    name = fields.Char(string="Name", required=True)
