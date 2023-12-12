from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CustomShipping(models.Model):
    _name = 'custom.shipping.rules'
    _description = 'This is Custom shipping model'

    customer_name = fields.Char(string='Customer',required='customer')
    customer_email = fields.Char(string="Email")
    customer_city = fields.Char(string='City')
    customer_zip = fields.Char(string='Zipcode')
    customer_country_id = fields.Many2one('res.country', string='Country')
    customer_state_id = fields.Many2one('res.country.state', string='State')
    custom_rate = fields.Float(string="Rate", default=0)
    carrier_id = fields.Many2one('delivery.carrier', string='Carrier')

    def save(self):
        if self.email:
            raise ValidationError(_("You cannot change email id"))
        return

    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'US')]
            , limit=1)
        return country

    country_id = fields.Many2one('res.country', string='Country', default=_get_default_country)

