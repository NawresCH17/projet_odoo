from odoo import models, fields, api
from odoo.exceptions import UserError


class Claim(models.Model):
    _name = 'claim.claim'
    _description = 'claim.claim'

    name = fields.Char(string='Name', required=False, readonly=False)
    start_date = fields.Date('Date ask', help="Date")
    end_date = fields.Date('Date response', help="Date")
    code = fields.Char(string='Code', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    reg_id = fields.Many2one('registration.registration', string='Inscription')
    user_id = fields.Many2one('res.users', string="Responsible")
    state = fields.Selection([('new', 'New'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status')
