from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _description="Patient Appointment"
    _inherit = ['mail.thread']
    _rec_names_search = ['reference', 'patient_id']
    _rec_name = 'patient_id'

    reference=fields.Char(string="Reference", default="New")
    patient_id=fields.Many2one("hospital.patient", string="Patient", required=False, ondelete="restrict")
    date_of_appoint=fields.Date(string="Appointment Date", tracking=True)
    doctor=fields.Char(string="Doctor")
    note=fields.Text(string="Note")
    state=fields.Selection([('draft','Draft'),('confirmed','Confirmed'),('ongoing','Ongoing'),('done','Done'),('cancel','Cancelled')],default="draft", tracking=True)
    appointment_line_ids=fields.One2many('hospital.appointment.lines','appointment_id', string="Prescription")
    total_qty = fields.Float( compute='_compute_total_qty', string='Total Quantity', store=True)
    date_of_birth=fields.Date(related="patient_id.date_of_birth", store=True)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':  # Corrected syntax
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)

    @api.depends('appointment_line_ids','appointment_line_ids.qty')
    def _compute_total_qty(self):
        for rec in self:
            total_qty=0
            for line in rec.appointment_line_ids:
                print("line value",line.qty)
                total_qty=total_qty+line.qty
            rec.total_qty=total_qty

    def _compute_display_name(self):
        for rec in self:
            rec.display_name=f"[{rec.reference}] {rec.patient_id.name}"

    def action_confirm(self):
        self.state = 'confirmed'

    def action_ongoing(self):  # Ensure this method exists
        self.state = 'ongoing'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Hospital Appointment Lines'

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity')

