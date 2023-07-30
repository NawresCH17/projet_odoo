from odoo import models, fields, api,_
from odoo.exceptions import UserError,ValidationError


class ProgramExamen(models.Model):
    _name = 'program.program'
    _description = "Programme d'examen"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Description')
    date_debut = fields.Date(string='Start Date')
    date_fin = fields.Date(string='End Date')
    type = fields.Selection([('cc', 'CC'), ('CTR', 'DS exam'), ('sum', 'final exam')], string='Type of exam')
    session = fields.Selection([('control', 'control'), ('principal', 'Principal')], string='Session')
    semester = fields.Selection([
        ('s1', 'Semester 1'),
        ('s2', 'Semester 2'),
        ('s3', 'Semester 3'),
    ], required=True)
    year_id = fields.Many2one('year.year', string='Year')
    personnel_id = fields.Many2one('personnel.personnel', string='Personnel administrative')
    line_ids = fields.One2many('program.program_line','program_id', string='Programs')


class ProgramLine(models.Model):
    _name = 'program.program_line'
    _rec_name="classe_ids"

    date_examen = fields.Date(
        string='Date',
    )
    heure_debut = fields.Float(
        string='Heure de début',
    )
    heure_fin = fields.Float(
        string='Heure de fin',
    )
    prof_id = fields.Many2one('prof.prof', string='Professor', required=True)

    classe_ids = fields.Many2one('class.class', string="Class")
    matter_id = fields.Many2one('matter.matter', string='Matter', required=True)
    salle_id = fields.Many2one('salle.salle', string='Salle', required=True)
    coefficient = fields.Integer(string='Coefficient')
    program_id = fields.Many2one(
        'program.program',
        string='Programme',
    )
