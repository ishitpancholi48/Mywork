from odoo import models, fields


class DeliveryCarrier(models.Model):

    _inherit = 'delivery.carrier'

    custom_rules_ids = fields.One2many(
        comodel_name='custom.shipping.rules',
        inverse_name='carrier_id',
        string="CustomId"
    )


