from odoo import models, fields, api


class HotelLaundary(models.Model):
    _name = 'hotel.laundary'
    _description = 'Hotel Laundary'

    customer_id = fields.Many2one('res.partner', string='Customer Name')
    cloth_type = fields.Selection([
        ('shirt', 'Shirt'),
        ('pant', 'Pant'),
        ('sareee', 'Saree'),
        ('jeans', 'Jeans'),
        ('blazzer', 'Blazzer'),
        ('other', 'other')
    ], string='Cloth type')
    price = fields.Integer(string='Price')

    @api.onchange('cloth_type', 'price')
    def laundary_price(self):
        for rec in self:
            if rec.cloth_type == 'shirt':
                rec.price = 20
            if rec.cloth_type == 'pant':
                rec.price = 15
            if rec.cloth_type == 'sareee':
                rec.price = 30
            if rec.cloth_type == 'jeans':
                rec.price = 18
            if rec.cloth_type == 'blazzer':
                rec.price = 100
            if rec.cloth_type == 'other':
                rec.price == 10
