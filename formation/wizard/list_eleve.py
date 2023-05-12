from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ListStudent(models.TransientModel):

    _name = 'list.list'
    _description = "Impression des liste d'élève"

    name = fields.Char(string="List")
    class_ids = fields.Many2one('class.class', string='Class', required=True,)

    def imprimer_liste_eleve(self):
     data = {}
     liste_des_eleves = []
     eleves = self.env['eleve.eleve'].search([('class_id', '=', self.class_ids.id)])
     for el in eleves:
        vals = {
            'name': el.name,
            'first_name': el.first_name,
            'last_name': el.last_name,
            'photo': el.photo,
            'date_birth': el.date_birth,
            'num_cin': el.num_cin,
            'email': el.email,
            'nationality': el.nationality,
            'class_id': el.class_id.name
            }
        liste_des_eleves.append(vals)

     data['liste_des_eleves'] = liste_des_eleves
     return self.env.ref('formation.report_list_eleve').report_action(self, data=data)

