from odoo import models, fields, api
from odoo.exceptions import UserError


class Year(models.Model):
    _name = 'year.year'
    _description = 'year.year'

    name = fields.Char(string='Name', required=False, readonly=False)
    start_date = fields.Date('Date start', help="Date")
    end_date = fields.Date('Date end', help="Date")
    description = fields.Text(string='Description', required=False, readonly=False)
    session_ids = fields.Many2one('session.session', string='session')


class Session(models.Model):
    _name = 'session.session'
    _description = 'session.session'

    name = fields.Char(string='Name', required=False, readonly=False)
    start_date = fields.Date('Date start', help="Date")
    end_date = fields.Date('Date end', help="Date")
    description = fields.Text(string='Description', required=False, readonly=False)
    year_id = fields.One2many('year.year', 'session_ids', string='Année univ')


class Cycle(models.Model):
    _name = 'cycle.cycle'
    _description = 'cycle.cycle'
    name = fields.Char(string='Name', required=False, readonly=False)
    code = fields.Char(string='Code', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    level_ids = fields.One2many('level.level', 'cycle_id', string='Niveau')

    def name_get(self):
        result = []
        for record in self:
            if record.name and record.code:
                result.append((record.id, record.name+'...'+record.code))
            if record.name and not record.code:
                result.append((record.id, record.name))
        return result


class Level(models.Model):
    _name = 'level.level'
    _description = 'level.level'
    name = fields.Char(string='Name', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    section_ids = fields.One2many('section.section', 'level_id', string='Section')
    cycle_id = fields.Many2one('cycle.cycle', string='Cycle')


class Section(models.Model):
    _name = 'section.section'
    _description = 'modules'

    name = fields.Char(string='Name', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    module_ids = fields.One2many('module.module', 'section_id', string='Module')
    level_id = fields.Many2one('level.level', string='Level')


class Module(models.Model):
    _name = 'module.module'
    _description = 'modules'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', default='001')
    description = fields.Text(string='Description')
    section_id = fields.Many2one('section.section', string='Section')


class Class(models.Model):
    _name = 'class.class'
    _description = 'class.class'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')

    nbr_std = fields.Integer(compute='_compute_student', string="Students")
    prof_ids = fields.Many2one('hr.employee', string='Prof')
    student_ids = fields.One2many('eleve.eleve','class_id', string='Student')

    @api.depends('student_ids')
    def _compute_student(self):
        self.nbr_std = len(self.student_ids)


class Salle(models.Model):
    _name = 'salle.salle'
    _description = 'salle records'

    nom_salle = fields.Char(string="Nom de la salle")
    capacity = fields.Integer(string="Capacité pour les cours")
    bloc=fields.Selection([('a','A'),('b','B'),('C','C'),('D','D')],string="Bloc")
