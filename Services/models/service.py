from odoo import models, fields, api
from odoo.exceptions import UserError


class Service(models.Model):
    _name = 'services.services'
    _description = 'services.services'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=False, readonly=False)
    date_ask = fields.Date('Date Ask', help="Date")
    date_response = fields.Date('Date Response', help="Date",default=fields.Date.today())
    code = fields.Char(string='Code', required=False, readonly=False)
    reg_id = fields.Many2one('registration.registration', string='Registration')
    student_id = fields.Many2one('eleve.eleve', string='Student')
    category = fields.Selection([('certificate_attendance', 'certificate of attendance'),
                                 ('certificate_registration', 'certificate_registration'),
                                 ('internship_doc', 'internship documents')], string='Category')
    state = fields.Selection([('in progress', 'In progress'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status')
    description = fields.Text(string='Description', required=False, readonly=False)
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'Medium'),
         ('3', 'High')],
        'Priority', default='1')
    color = fields.Integer('Color Index')
    personnel_id = fields.Many2one('personnel.personnel', string='Personnel')
    file = fields.Binary('Upload File')

    def action_new(self):
     self.state = 'in progress'
     return True

    def action_done(self):
     self.state = 'done'
     return True

    def action_cancel(self):
     self.state = 'cancel'
     return True

    def print_service(self):
     return self.env.ref('Services.report_service_view').report_action(self)

    def unlink(self):
        for record in self:
            if record.state in 'done,cancel':
                raise UserError('You cannot delete records in done state.')
        res = super(Service, self).unlink()
        return res

    def action_send_mail(self):
        mail_template = self.env.ref('Services.mail_template_service')
        mail_template.send_mail(self.id,force_send=True)
