from odoo import models, fields, api,_
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
    section_ids = fields.Many2one('section.section', string='Section')
    cycle_id = fields.Many2one('cycle.cycle', string='Cycle')


class Section(models.Model):
    _name = 'section.section'
    _description = 'modules'

    name = fields.Char(string='Name', required=False, readonly=False)
    description = fields.Text(string='Description', required=False, readonly=False)
    module_ids = fields.Many2one('module.module', string='Module')
    level_id = fields.One2many('level.level', 'section_ids', string='Level')


class Module(models.Model):
    _name = 'module.module'
    _description = 'modules'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', default='001')
    description = fields.Text(string='Description')
    section_id = fields.One2many('section.section','module_ids', string='Section')
    matter_id = fields.One2many('matter.matter', 'module_id', string='Matter')


class Matter(models.Model):
    _name = 'matter.matter'
    _description = 'Matters'

    name = fields.Char(string='Name', required=True)
    Moy_mat = fields.Float(string='Average')
    max = fields.Integer(string="Coefficient")
    module_id = fields.Many2one('module.module', string='Modules')
    prof_ids = fields.Many2one('prof.prof', string='Professor')
    type = fields.Selection([
        ('theorique', 'theoretical'),
        ('pratique', 'Pratique')
    ], string="Type",
        required=True, )


class Class(models.Model):
    _name = 'class.class'
    _description = 'class.class'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
    nbr_std = fields.Integer(compute='_compute_student', string="Students")
    capacity=fields.Integer(string='capacity')
    # prof_ids = fields.One2many('prof.prof','class_id', string='Prof')
    prof_ids = fields.Many2many('prof.prof', relation='class_prof_rel', column1='name', column2='first_name')
    student_ids = fields.One2many('eleve.eleve', 'class_id', string='Student')
    salle_ids = fields.One2many('salle.salle', 'class_ids', string='Salle')

    @api.depends('student_ids')
    def _compute_student(self):
        self.nbr_std = len(self.student_ids)


class Salle(models.Model):
    _name = 'salle.salle'
    _description = 'salle records'

    name = fields.Char(string='Salle', required=True)
    capacity = fields.Integer(string="Capacity")
    bloc = fields.Selection([('a','A'),('b','B'),('C','C'),('D','D')], string="Bloc", default='A')
    class_ids = fields.Many2one('class.class', string='Class')





