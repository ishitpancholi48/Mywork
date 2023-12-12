from odoo import models, fields

class OfficeDetails(models.Model):
    _name = "office.details"
    _description = "This is office details"

    service = fields.Char(string="Service",size=80)
    error_detail=fields.Char(string="Error_detail",size=500)
