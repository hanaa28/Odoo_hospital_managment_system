from odoo import models,fields

class department(models.Model):
    _name='hms_department'

    name=fields.Char(required=True)
    is_opened=fields.Boolean()
    capacity=fields.Integer()
    