from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError
from datetime import date


class Patients(models.Model):
    _name = "patient"
    _rec_name = "firstName"

    firstName = fields.Char(required=True)
    lastName = fields.Char(required=True)
    birthDate = fields.Date()
    age = fields.Integer(compute='calc_age', store=True)
    bloodType = fields.Selection([("A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O")])
    history = fields.Html()
    cr_ratio = fields.Float()
    address = fields.Text()
    image = fields.Binary()
    pcr = fields.Boolean()
    log_history = fields.Char(string="Patient History")
    email = fields.Char(required=True)
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

    sql_constraints=[
       ('unique_patient_email','unique(email)','This Email is Created Before'),
        
    ]

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
            else:
                rec.pcr = False
    
    @api.constrains('email')
    def _check_email(self):
        email_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        for rec in self:
            if rec.email and not re.match(email_pattern, rec.email):
                raise ValidationError("The email address is not valid.")

    @api.depends('birthDate')
    def calc_age(self):
        for rec in self:
            if rec.birthDate:
                today = date.today()
                rec.age = today.year - rec.birthDate.year - ((today.month, today.day) < (rec.birthDate.month, rec.birthDate.day))
            else:
                rec.age = 0
