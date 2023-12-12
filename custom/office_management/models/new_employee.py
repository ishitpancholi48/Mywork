from odoo import models, fields, api


class NewEmployee(models.Model):
    _name = 'new.employee'

    employee_name = fields.Many2one('office.staff', string='Employee Name')
    course_name = fields.Many2one('company.service', string='Course Name')
    details = fields.Char(string='Details')
    partner_ids = fields.Many2one('res.partner', string='Customer')
    sale_order = fields.Many2one('sale.order', string='Sale Order')
    partner = fields.One2many(
        comodel_name='office.staff',
        inverse_name='partner_id',
        string='Employee'
    )








