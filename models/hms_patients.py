from odoo import models, fields

class Patients(models.Model):
    _name = 'patient'
    _rec_name = 'firstName'

    firstName = fields.Char(required=True)
    lastName = fields.Char(required=True)
    birthDate = fields.Date()
    age = fields.Integer()
    bloodType = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    history = fields.Html()
    cr_ratio = fields.Float()
    address = fields.Text()  
    image = fields.Binary()
    pcr = fields.Boolean()
    log_history=fields.Char(string='Patient History')
    status=fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious')
    ])


    department_id = fields.Many2one('hms_department',domain="[('is_opened','=','True')]")
    department_capacity = fields.Integer(related_to='department_id.capacity')

    doctor_ids = fields.Many2many('hms.doctor', string="Doctors")



