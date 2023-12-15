from odoo import models, fields


class HotelRestaurantOrder(models.Model):
    _name = 'hotel.customer.order'
    _description = 'Hotel Restaurant Order'

    customer_name = fields.Many2one('hotel.customer',string='Customer Name')
    food_menu = fields.Many2many('hotel.restaurant',string="Food Item")
    food_price = fields.Integer(string='Price',related='food_menu.food_price')

