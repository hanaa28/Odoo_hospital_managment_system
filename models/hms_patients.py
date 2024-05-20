from odoo import models, fields, api


class Patients(models.Model):
    _name = "patient"
    _rec_name = "firstName"

    firstName = fields.Char(required=True)
    lastName = fields.Char(required=True)
    birthDate = fields.Date()
    age = fields.Integer()
    bloodType = fields.Selection([("A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O")])
    history = fields.Html()
    cr_ratio = fields.Float()
    address = fields.Text()
    image = fields.Binary()
    pcr = fields.Boolean()
    log_history = fields.Char(string="Patient History")
    status = fields.Selection(
        [
            ("Undetermined", "Undetermined"),
            ("Good", "Good"),
            ("Fair", "Fair"),
            ("Serious", "Serious"),
        ]
    )

    department_id = fields.Many2one(
        "hms_department", domain="[('is_opened','=','True')]"
    )
    department_capacity = fields.Integer(related_to="department_id.capacity")

    doctor_ids = fields.Many2many("hms.doctor", string="Doctors")

    patient_state_log = fields.One2many("patient_logs", "patient_id")

    @api.onchange('status')
    def change_status(self):
        for rec in self:
            rec.env['patient_logs'].create(
                {
                    'description': 'status changed to %s' % rec.status,
                    'patient_id': rec.id,
                }
            )

    @api.onchange('age')
    def change_pcr(self):
        for rec in self:
            if rec.age < 30:
                rec.pcr = True
                return {
                    "warning": {
                        "title": "Check ",
                        "message": "PCR Checked at age %s" % rec.age,
                    }
                }
            else:
                rec.pcr = False
