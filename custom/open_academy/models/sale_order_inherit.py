from odoo import models,fields, api



class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    course_id = fields.Many2one('academy.course', ondelete='cascade', string="Course Name"  )
    course_description = fields.Text(string='Course Description', related='course_id.course_description',help='Course Descriptions')


    def action_confirm(self):
        res = super(SaleOrderInherit, self).action_confirm()
        for rec in self:
            for pick_rec in rec.picking_ids:
                pick_rec.write({
                    'course_id': rec.course_id
                })
                return res




