from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TimeTable(models.TransientModel):

    _name = 'listtime.listtime'
    _description = "Impression des timetable"

    name = fields.Char(string="List")
    class_id = fields.Many2one('class.class', string='Class', required=True,)
    sem = fields.Selection([
        ('s1', 'Semester 1'),
        ('s2', 'Semester 2'),
        ('s3', 'Semester 3'),
    ], required=True)

    def imprimer_timetable_class(self):
     data = {}
     liste = []
     timetable = self.env['emploi.emploi'].search([('classe_ids', '=', self.class_id.id),('semester','=',self.sem)])
     for el in timetable:
        vals = {
            'name': el.name,
            'debut': el.debut,
            'fin': el.fin,
            'day': el.day,
            'matter_id': el.matter_id.name,
            'year_id': el.year_id.name,
            'semester': el.semester,
            'classe_ids': el.classe_ids.name,
            'prof_id': el.prof_id.first_name
            }
        liste.append(vals)

     data['liste'] = liste
     return self.env.ref('formation.report_time_class').report_action(self, data=data)
