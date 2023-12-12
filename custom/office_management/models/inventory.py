from odoo import models, fields


class Inventory_view(models.Model):
    _inherit = 'stock.picking'

    country = fields.Selection([
        ('america', 'America'),
        ('brasil', 'Brasil'),
        ('australia', 'Australia'),
        ('London', 'London'),
    ], string='Country')
