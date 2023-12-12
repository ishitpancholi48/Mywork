from odoo import models,fields

class StudentList(models.Model):
    _name= 'student.list'
    _description='this model use for check student records list'

    student_id = fields.Many2one('student.record',string='Student Name')
    student_gender = fields.Selection(string='Gender',related='student_id.student_gender')
    student_contact_number = fields.Char(string='Contact Number', related='student_id.student_contact_number')
    student_class = fields.Selection(string='Class',related='student_id.student_class')
