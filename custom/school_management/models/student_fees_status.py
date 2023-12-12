from odoo import models,fields

class StudentFeesStatus(models.Model):
    _name = 'student.fees.status'
    _description = 'Check Student Fees Paid Or Not Paid'

    student_id = fields.Many2one('student.fees',string='Student Name')
    fees_status = fields.Char(string='Fees Status',required='student_id.fees_status')

