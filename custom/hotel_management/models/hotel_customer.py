from odoo import models, fields
from odoo.exceptions import ValidationError


class HotelCustomerForm(models.Model):
    _name = 'hotel.customer'
    _description = 'This model for customer details'
    _rec_name = 'customer_name'

    customer_name = fields.Char(string='Customer Name', help='Enter Full Name')
    customer_age = fields.Integer(string='Age')
    customer_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    customer_mobile_number = fields.Char(string='Mobile Number',
                                         help='please use code example +91 before enter your mobile number')
    customer_city = fields.Char(string='City')
    customer_verification_id = fields.Selection([
        ('aadhar card','Aadhar Card'),
        ('pancard','Pancard'),
        ('voterid','VoterId'),
        ('driving license','Driving License'),
        ('passport','Passport'),
    ],string='Verification Doucuments',help='Select your verfication id which you have available now')
    customer_room_detail_ids = fields.One2many('customer.room.detail.lines', 'customer_id', string='Room Details')
    customer_payment_detail_ids = fields.One2many('payment.detail.lines','customer_id',string='Payment Details')


class CustomerRoomDetailLines(models.Model):
    _name = 'customer.room.detail.lines'
    _description = 'Customer Room Detai lLines'

    room_no = fields.Char(string='Room No')
    checkin = fields.Date(string='CheckIn')
    checkout = fields.Date(string='CheckOut')
    customer_id = fields.Many2one('hotel.customer',string='Customer Name')

class PaymentDetailLines(models.Model):
    _name = 'payment.detail.lines'
    _description = 'Payment Detail Line'

    customer_payment = fields.Integer(string='Payment')
    payment_type = fields.Selection([
        ('cash','Cash'),
        ('debit card','Debit Card'),
        ('credit card','Credit Card'),
        ('upi','UPI'),
        ('paytm','Paytm')
    ],string='Type')
    customer_id= fields.Many2one('hotel.customer',string='Customer Name')
