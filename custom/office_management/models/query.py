from odoo import models, fields

class CompanyService(models.Model):
    _name = "company.service"
    _description = "This is the query related"
    _rec_name = "detail"

    detail = fields.Char(string="Detail", size=50)
    query = fields.Char(string="Query", size=500)
    partner_ids = fields.One2many(
        comodel_name='office.staff',
        inverse_name='partner_id',
        string='Employee'
    )
    many2many= fields.Many2many(
        comodel_name='office.staff',
        string='Selection'
    )


