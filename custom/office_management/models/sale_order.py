from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SalesOrder(models.Model):
    _inherit = 'sale.order'


    zipcode = fields.Integer(string="Zipcode")
    product_names = fields.Char(string="Product_Names")


    @api.model
    def action_confirm(self):
        res = super(SalesOrder,self).action_confirm()
        print("res",res)
        raise UserError(_("------Action Confirm is called------"))
        return res


