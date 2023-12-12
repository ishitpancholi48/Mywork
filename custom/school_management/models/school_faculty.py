from odoo import models, fields, api, _


class SchoolFaculty(models.Model):
    _name = 'school.faculty'
    _description = 'School faculty Information'
    _rec_name = 'faculty_name'

    faculty_id_no = fields.Char(string='Faculty ID No', readonly=True, index=True, required=True, copy=False,
                                default=lambda self: _('New'))
    faculty_name = fields.Char(string="Faculty Name", help='Faculty Name')
    faculty_image = fields.Binary(string='Passport Size Photos')
    faculty_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', help='Enter your Gender')
    faculty_mobile_number = fields.Char(string='Mobile Number', help='Faculty Contact Number')
    faculty_subject_tags = fields.Many2many('subject.tags', string='Subject')

    # facult id sequence create fucntion
    @api.model
    def create(self, vals):
        if vals.get('faculty_id_no', _('New')) == _('New'):
            vals['faculty_id_no'] = self.env['ir.sequence'].next_by_code('school.faculty.sequence') or _('New')
        res = super(SchoolFaculty, self).create(vals)
        return res


class SubjectTags(models.Model):
    _name = 'subject.tags'
    _description = 'Subject Tags'
    _rec_name = 'faculty_subject'

    faculty_subject = fields.Selection([
        ('english', 'English'),
        ('gujarati', 'Gujarati'),
        ('hindi', 'Hindi'),
        ('social science', 'Social Science'),
        ('science', 'Science'),
        ('general knowledge', 'General Knowledge'),
        ('sanskrit', 'Sanskrit'),
    ])
