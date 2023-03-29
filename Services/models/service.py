from odoo import models, fields, api
from odoo.exceptions import UserError


class Service(models.Model):
    _name = 'services.services'
    _description = 'services.services'

    name = fields.Char(string='Name', required=False, readonly=False)
    date_ask = fields.Date('Date Ask', help="Date")
    date_response = fields.Date('Date Response', help="Date")
    code = fields.Char(string='Code', required=False, readonly=False)
    # reg_id = fields.Many2one('registration.registration', string='Registration')
    # student_id = fields.Many2one('eleve.eleve', string='Student')
    category = fields.Selection([('certificate_attendance', 'certificate of attendance'),
                                 ('certificate_registration', 'certificate_registration'),
                                 ('internship_doc', 'internship documents')], string='Category')
    state = fields.Selection([('in progress', 'In progress'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status')

