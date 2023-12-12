from odoo import models,fields,api



class StockPicking(models.Model):
    _inherit = 'stock.picking'


    course_id = fields.Many2one('academy.course', ondelete='cascade', string="Course Name", required=True)
    course_description = fields.Text(string='Course Description', related='course_id.course_description',help='Course Descriptions')



