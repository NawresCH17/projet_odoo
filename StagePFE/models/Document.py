from odoo import models, fields, api
from odoo.exceptions import UserError


class Document(models.Model):
    _name = 'documents.documents'
    _description = 'documents.documents'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=False, readonly=False)
    bilans = fields.Binary('Load Bilan')
    rapport = fields.Binary('Load Rapport')
    Journaux = fields.Binary('Load Journaux')
    date_response = fields.Date('Date Depot', help="Date", default=fields.Date.today())
    description = fields.Html(string='Description', required=False, readonly=False)


class File(models.Model):
        _name = 'fileu.fileu'
        _description = 'fileu.fileu'

        #name = fields.Char(string='Name', required=False, readonly=False)
        #description = fields.Html(string='Description', required=False, readonly=False)