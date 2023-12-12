from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    country = fields.Many2one(
        comodel_name = 'res.partner',
        string = 'Country',
    )