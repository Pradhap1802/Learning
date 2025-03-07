from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Master"
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=True, tracking=True)
    fullname = fields.Char(string="Full Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    diagnosis = fields.Char(string="Diagnosis", tracking=True)
    tag_ids = fields.Many2many("patient.tag", 'patient_tag_rel', 'patient_id', 'tag_id', string="Patient Tags")
    patient_id = fields.Many2one('hospital.appointment', string="Appointment")

    @api.ondelete(at_uninstall=False)
    def _check_patient_appointments(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['hospital.appointment'].search(domain)
            if appointments:
                raise ValidationError(_("You cannot delete the patient now. Appointments existing for this patient :%s")% rec.name)

    # def unlink(self):
    #     for rec in self:
    #         domain = [('patient_id', '=', rec.id)]
    #         appointments = self.env['hospital.appointment'].search(domain)
    #         if appointments:
    #             raise ValidationError(_("You cannot delete the patient now. Appointments existing for this patient ."))
    #     return super(HospitalPatient, self).unlink()
