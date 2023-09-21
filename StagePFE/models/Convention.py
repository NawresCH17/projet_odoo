from odoo import models, fields, api
from odoo.exceptions import UserError


class Convention(models.Model):
    _name = 'convention.convention'
    _description = 'convention.convention'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=False, readonly=False)
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    date_ask = fields.Date('Date start', help="Date")
    date_response = fields.Date('Date End', help="Date")
    company = fields.Char(string='company Name')
    encadrant = fields.Char(string='Company supervisor')
    state = fields.Selection([('in progress', 'In progress'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status')
    description = fields.Html(string='Description', required=False, readonly=False)

    def action_new(self):
     self.state = 'in progress'
     return True

    def action_done(self):
     self.state = 'done'
     return True

    def action_cancel(self):
     self.state = 'cancel'
     return True

    def print_convention(self):
       return self.env.ref('report_convention').report_action(self)

    def unlink(self):
        for record in self:
            if record.state in 'done,cancel':
                raise UserError('You cannot delete records in done state.')
        res = super(Convention, self).unlink()
        return res

