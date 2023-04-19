from odoo import models, fields, api
from odoo.exceptions import UserError


class Claim(models.Model):
    _name = 'claims.claims'
    _description = 'claims.claims'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=False, readonly=False)
    start_date = fields.Date('Date ask', help="Date")
    end_date = fields.Date('Date response', help="Date",default=fields.Date.today())
    code = fields.Char(string='Code', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    reg_id = fields.Many2one('registration.registration', string='Inscription')
    user_id = fields.Many2one('res.users', string="Responsible")
    student_id = fields.Many2one('eleve.eleve', string='Student')
    file = fields.Binary('Upload File')
    type = fields.Selection([('note', 'reclamation pour note'),
                             ('emploi', 'reclamation pour emploi du temps'),
                             ('examen', 'reclamation pour examen'),('other','Other claims')], string='Type')
    state = fields.Selection([('new', 'In progress'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2','Medium'),
         ('3', 'High')],
        'Priority', default='1')

    def print_claim(self):
        return self.env.ref('Services.report_claim_view').report_action(self)

    def action_new(self):
     self.state = 'new'
     return True

    def action_done(self):
     self.state = 'done'
     return True

    def action_cancel(self):
     self.state = 'cancel'
     return True

    def unlink(self):
        for record in self:
            if record.state in 'done':
                raise UserError('You cannot delete records in done state.')
        res = super(Claim, self).unlink()
        return res
