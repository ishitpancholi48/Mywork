from odoo import models,fields

class ShopifyPaymentGateway(models.Model):
    _name= 'shopify.payment.gateway'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Payment Gateway'

    name = fields.Char(string='Name',help='Enter Name',copy=False,tracking=True)
    code = fields.Char(string='Code',help='Enter Code',copy=False,tracking=True)
    instance_id = fields.Many2one('shopify.instance.integration',string='Instance',copy=False,tracking=True)
    company_id = fields.Many2one('res.company',string='Compamy',help='Select company',copy=False,tracking=True)



