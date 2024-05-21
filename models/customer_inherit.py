from odoo import models ,fields,api
from odoo.exceptions import ValidationError

class customer(models.Model):
    _inherit='res.partner'
    related_patient_id=fields.Many2one('patient')

    @api.constrains('email','related_patient_id')
    def check_email_exist(self):
        for rec in self:
            if rec.related_patient_id and rec.email:

                check_operator=self.search([('email', '=', rec.email),
                    ('related_patient_id', '!=',rec.related_patient_id.id)])
                if check_operator:
                      raise ValidationError("The email %s is already assigned to another customer with a different patient." % rec.email)
