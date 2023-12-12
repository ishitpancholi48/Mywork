from odoo import models, fields, api


class College_Course(models.Model):
    _name = "college.course"
    _description = "Students data with student stream"

    student_data = fields.Many2one('college.university', string='Data of Students')
    student_stream = fields.Char(string='Stream Of Student', compute="_compute_student")


    @api.depends('student_data')
    def _compute_student(self):
        for rec in self:
            rec.student_stream = rec.student_data.diploma_field






        # @api.onchange('student_data')
        # def _onchange_name(self):
        #     self.student_stream = self.student_data
