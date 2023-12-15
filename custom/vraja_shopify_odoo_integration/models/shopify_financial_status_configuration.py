from odoo import models, fields


class ShopifyFinancialStatusConfiguration(models.Model):
    _name = 'shopify.financial.status.configuration'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Shopify Financial Status Configuration'

    instance_id = fields.Many2one('shopify.instance.integration', string='Instance', help='Select Instance Id',
                                  copy=False, tracking=True)
    company_id = fields.Many2one('res.company', string='Company', help='Select Company', copy=False, tracking=True)
    payment_gateway_id = fields.Many2one('shopify.payment.gateway', string='Payment Gateway', help='select payment id',
                                         copy=False, tracking=True)
    payment_term_id = fields.Many2one('account.payment.term', string='Payment Term', help='select payemt term id',
                                      copy=False, tracking=True,
                                      default=lambda self: self.env.ref('account.account_payment_term_immediate'))
    sale_auto_workflow_id = fields.Many2one('order.workflow.automation', string='Auto Workflow',
                                            help='select workflow id', copy=False, tracking=True)
    active = fields.Boolean(string='Active', default=True)
    financial_status = fields.Selection([
        ('pending', ' The finances are pending'),
        ('authorized', 'The finances have been authorized'),
        ('partially_paid', 'The finances have been partially paid'),
        ('paid', 'The finances have been paid'),
        ('partially_refunded', 'The finances have been partially refunded'),
        ('refunded', 'The finances have been refunded'),
        ('voided', 'The finances have been voided')
    ], string='Financial Status', help='select financial status', copy=False, tracking=True)
