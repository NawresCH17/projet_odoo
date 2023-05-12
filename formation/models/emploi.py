from odoo import models, fields, api


class TimeTable(models.Model):
    _name = 'timenet.timenet'
    _description = 'TimeTable'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    classe_ids = fields.Many2one('class.class', string="Class")
    year_id = fields.Many2one('year.year', string='Year')
    semester = fields.Selection([
        ('s1', 'Semester 1'),
        ('s2', 'Semester 2'),
        ('s3', 'Semester 3'),
    ], required=True)

    session_id = fields.Many2many('emploi.emploi', relation='seance_emploi_rel', column1='name', column2='semester')

    def print_emploi(self):
        return self.env.ref('formation.report_emploi').report_action(self)

