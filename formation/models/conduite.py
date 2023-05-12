from odoo import models, fields, api


class Conduite(models.Model):
    _name = 'conduite.conduite'
    _description = 'Attendance'

    name = fields.Char(string='Name', default='New')
    class_id = fields.Many2one('class.class', string='Class')
    eleve_id = fields.Many2one('eleve.eleve', string='Student')

    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.today(),
    )
    type = fields.Selection([
        ('present', 'Present'),
        ('absence', 'Absence'),
        ('retard', 'Retard')
    ], string="Type",
        required=True, )

    year_id = fields.Many2one(
        'year.year',
        string='Year',
        required=True
    )
    semester = fields.Selection([
        ('s1', 'Semester 1'),
        ('s2', 'Semester 2'),
        ('s3', 'Semester 3'),
    ], required=True)

    nombre_heure = fields.Integer(
     string="Nombre d'heure",
     required=True)



