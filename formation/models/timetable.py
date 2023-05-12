from odoo import models, fields, api


class TimeTable(models.Model):
    _name = 'emploi.emploi'
    _description = 'TimeTable'

    def print_time(self):
        return self.env.ref('formation.report_timetable').report_action(self)

    name = fields.Char(string='Name', required=True)
    day = fields.Selection([('Mon', 'Monday'), ('Tue', 'Tuesday'),
                            ('Wed', 'Wednesday'), ('Thur', 'Thursday'),
                            ('Fri', 'Friday'), ('sat', 'Saturday'),
                            ('Sun', 'Sunday')], string="Day")
    jour = fields.Date('Date', help="Date")

    debut = fields.Float(string='Start time')
    fin = fields.Float(string='End time')

    classe_ids = fields.Many2one('class.class', string="Class")

    prof_id = fields.Many2one('prof.prof', string='Professor', required=True)
    matter_id = fields.Many2one('matter.matter', string='Matter', required=True)
    year_id = fields.Many2one('year.year', string='Year')
    semester = fields.Selection([
        ('s1', 'Semester 1'),
        ('s2', 'Semester 2'),
        ('s3', 'Semester 3'),
    ], required=True)

    time_id = fields.Many2many('timenet.timenet', relation='emploi_seance_rel', column1='semester', column2='name')






