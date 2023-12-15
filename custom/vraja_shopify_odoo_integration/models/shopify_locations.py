from odoo import models, fields


class ShopifyLocations(models.Model):
    _name = 'shopify.location'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Shopify Loactions'

    name = fields.Char(string='Name', help='Enter Name', copy=False, tracking=True)
    shopify_location_id = fields.Char(string='Shopify Location', help='Location ID', copy=False, tracking=True)
    instance_id = fields.Many2one('shopify.instance.integration', string='Instance', help='Select Instance Id',
                                  copy=False, tracking=True)
    company_id = fields.Many2one('res.company', string='Company', help='Select Company', copy=False, tracking=True)
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse', help='Select Warehouse', copy=False,
                                   tracking=True)
    is_primary_location = fields.Boolean(string='Is Primary Location',help='tick primary location',copy=False,tracking=True)
    is_import_export_stock = fields.Boolean(string='Stock',help='Import Export Stock',copy=False,tracking=True)
    location_id = fields.Many2one('stock.location',string='Location',copy=False,tracking=True)
