from odoo import models, fields


class ShopifyInstanceIntegrations(models.Model):
    _name = 'shopify.instance.integration'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Shopify Instance Integartion'

    name = fields.Char(string='Name', help='Enter The Name', copy=False, tracking=True)
    active = fields.Boolean(string='Active', help='Click the active checkbox', copy=False,tracking=True)
    company_id = fields.Many2one('res.company', string='Company', help='Select Company', copy=False, tracking=True)
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse Name')
    shopify_url = fields.Char(string='Shopify Url',help='Enter Shopify Url',copy=False,tracking=True)
    shopify_api_key = fields.Char(string='Api Key',help='Enter Shopify Api Key',copy=False,tracking=True)
    shopify_pwd = fields.Char(string='Shopify Password',help='Shopify Password',copy=False,tracking=True)
    shopify_secret_key = fields.Char(string='Shopify Secrect Key',help='Shopify Secret Key',copy=False,tracking=True)


    def action_test_connection(self):
        pass

    def action_log(self):
        pass

    def action_products(self):
        pass

    def action_customers(self):
        pass

    def action_orders(self):
        pass

    def action_queue(self):
        pass

    def action_locations(self):
        pass