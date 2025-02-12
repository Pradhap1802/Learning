from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Patient Master"
    _inherit = ['mail.thread']

    name=fields.Char(string="Name", required=True, tracking=True)
    date_of_birth=fields.Date(string="DOB", tracking=True)
    gender=fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking=True)
    diagnosis=fields.Char(string="Diagnosis", tracking=True)
    tag_ids=fields.Many2many("patient.tag",'patient_tag_rel','patient_id','tag_id',  string="Patient Tags")

