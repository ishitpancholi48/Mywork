from odoo import models, fields, api, _


class StudentRecord(models.Model):
    _name = 'student.record'
    _description = 'This model use for Management of Students Record'
    _rec_name='student_name'

    student_record_number = fields.Char(string='Student Record Number', required=True, readonly=True, copy=False,
                                        index=True, default=lambda self: _('New'))
    student_name = fields.Char(string='Student Name', help='Enter Full Name')
    student_age = fields.Integer(string='Age', help='Enter Proper Age')
    student_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', help='Select Your Gender')
    student_dob = fields.Date(string='Date of Birth', help='Enter Your Birth Date')
    student_contact_number = fields.Char(string='Contact Number', help='Enter Parents Contact Number')
    student_address = fields.Text(string='Address', help='Enter Your Address')
    student_city = fields.Char(string='City', help='Enter Your City')
    student_class = fields.Selection([
        ('1st standard', '1st Standard'),
        ('2nd standard', '2nd Standard'),
        ('3rd standard', '3rd Standard'),
        ('4th standard', '4th Standard'),
        ('5th standard', '5th Standard'),
        ('6th standard', '6th Standard'),
        ('7th standard', '7th Standard'),
        ('8th standard', '8th Standard'),
        ('9th standard', '9th Standard'),
        ('10th standard', '10th Standard'),
    ], string='Class', help='Enter Your Class')


    # This function use for Student Record Number Sequence
    @api.model
    def create(self,vals):
        if vals.get('student_record_number',_('New')) == _('New'):
            vals['student_record_number']=self.env['ir.sequence'].next_by_code('student.record.sequence') or _('New')
            res = super(StudentRecord,self).create(vals)
            return res

