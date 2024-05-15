from odoo import models, fields


class HmsDoctors(models.Model):
    _name='hms.doctor'
    _rec_name='fname'

    fname=fields.Char(required=True)
    lname=fields.Char(required=True)
    image=fields.Binary()