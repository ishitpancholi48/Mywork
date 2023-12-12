from odoo import models, fields, api, _


class StudentFees(models.Model):
    _name = 'student.fees'
    _description = 'Student Fees'

    receipt_seq = fields.Char(string="Receipt Sequence", required=True, readonly=True, copy=False, index=True,
                                  default=lambda self: _('New'))
    student_id = fields.Many2one('student.record', string='Student Name')
    student_fees = fields.Integer(string='School Fees')
    student_tution_fees = fields.Integer(string='School Tution Fees')
    total_fees = fields.Integer(string='Total Fees Amount', compute='_total_fees')
    fees_status = fields.Selection([
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ], string='Fees Status')

    def action_paid(self):
        self.fees_status = 'paid'
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Thankyou Your Fees is Paid !',
                'type': 'rainbow_man',

            }
        }


    def action_unpaid(self):
        self.fees_status = 'unpaid'

    @api.depends('student_fees', 'student_tution_fees')
    def _total_fees(self):
        for rec in self:
            rec.total_fees = rec.student_fees + rec.student_tution_fees


    @api.model
    def create(self, vals):
        if vals.get('receipt_seq', 'New') == 'New':
            vals['receipt_seq'] = self.env['ir.sequence'].next_by_code(
                'student.fees.sequence') or 'New'
            result = super(StudentFees, self).create(vals)
            return result

