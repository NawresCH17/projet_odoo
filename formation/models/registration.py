from odoo import models, fields, api
from odoo.exceptions import UserError


class Registration(models.Model):

    _name = 'registration.registration'
    _description = 'registration.registration'
    _inherit = ['mail.thread']

    def print_report(self):
        return self.env.ref('formation.report_registration').report_action(self)

    def action_new(self):
        self.state = 'new'
        return True

    def action_done(self):
        self.state = 'done'
        return True

    def action_cancel(self):
        self.state = 'cancel'
        return True

    @api.model
    def create(self, vals):
        # if vals.get('name'):
        #     vals['name'] = 'value by write method'
        return super(Registration, self).create(vals)

    def write(self, vals):
        # vals['name'] = 'value by write method'
        return super(Registration, self).write(vals)

    def copy(self, default=None):
        default = dict(default or {})
        default.update({'name': 'copy(name)','code': 'copy -001'})
        return super(Registration, self).copy(default)

    def unlink(self):
        for record in self:
            if record.state in 'done,cancel':
                raise UserError('You cannot delete records in done state.')
        res = super(Registration, self).unlink()
        return res

    @api.depends('claim_ids')
    def _compute_claims(self):
        self.nbr = len(self.claim_ids)

    name = fields.Char(string='Name', required=False, readonly=False)
    start_date = fields.Date('date inscription', help="Date")
    end_date = fields.Date('date end', help="Date")
    code = fields.Char(string='Code', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    cycle_id = fields.Many2one('cycle.cycle', string='Cycle')
    year_id = fields.Many2one('year.year', string='Year')
    claim_ids = fields.One2many('claim.claim', 'reg_id', string='Claims')
    # claim_ids = fields.Many2one('claim.claim', string='Claims')
    state = fields.Selection([('new', 'New'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status', default='new')
    student_id = fields.Many2one('eleve.eleve', string='Student')
    personnel_id = fields.Many2one('personnel.personnel',string='Personnel administratif')
    nbr = fields.Integer(compute='_compute_claims', string="Claims")
