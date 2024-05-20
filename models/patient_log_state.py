from odoo import models,fields

class patients_log(models.Model):
    _name='patient_logs'

    description =fields.Char()
    patient_id=fields.Many2one('patient')