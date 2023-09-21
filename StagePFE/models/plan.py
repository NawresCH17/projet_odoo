from odoo import models, fields, api
from odoo.exceptions import UserError


class Convention(models.Model):
    _name = 'plan.plan'
    _description = 'plan.plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=False, readonly=False)
    title = fields.Char(string='project Title')
    problematic = fields.Char(string='Problematic')
    Function = fields.Char(string='Functions')
    Technology = fields.Char(string='Technologies')
    company = fields.Char(string='company Name')
    encadrant = fields.Char(string='Company supervisor')
    diagram = fields.Binary('Load diagram')
    description = fields.Html(string='Description', required=False, readonly=False)
    state = fields.Selection([('in progress', 'In progress'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status')

    def action_new(self):
     self.state = 'in progress'
     return True

    def action_done(self):
     self.state = 'done'
     return True

    def action_cancel(self):
     self.state = 'cancel'
     return True

    #def print_Demande(self):
     #return self.env.ref('report_Convention_view').report_action(self)

    def unlink(self):
        for record in self:
            if record.state in 'done,cancel':
                raise UserError('You cannot delete records in done state.')
        res = super(Convention, self).unlink()
        return res
