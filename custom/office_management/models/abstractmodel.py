from odoo import models, fields

class AbstractModel(models.AbstractModel):
    _name = "abstract.model"

    name = fields.Char(string='name')
