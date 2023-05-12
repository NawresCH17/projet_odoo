import datetime

from odoo import models, fields,_
from odoo.exceptions import ValidationError,UserError


class Reservation(models.Model):
    _name = 'reserv.reserv'
    _description = 'reserv.reserv'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_reservation = fields.Date('date_reservation', help="Date")
    res_id = fields.Many2one('bibl.bibl', string='Document')
    user = fields.Many2one('res.users', string='Member')
    max_date = fields.Date(string='Expected return day', help="Date")
    state = fields.Selection([('done', 'Valid'), ('cancel', 'Canceled')], string='Status', default='done')

    def action_done(self):
        if self.res_id.Etat !='disponible':
            raise UserError("this book is not disposal")
        self.state = 'done'
        return True

    def action_cancel(self):
        self.state = 'cancel'
        return True


class Emprunt(models.Model):
    _name = 'emprunt.emprunt'
    _description = 'emprunt.emprunt'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date_emprunt = fields.Date('Issued Date', help="Date")
    date_retour = fields.Date('Return day', help="Date")
    user = fields.Many2one('res.users', string='Issued To')
    penalty = fields.Float(string="Penalty")
    nombre_livres = fields.Integer(string='The number of books Taken')
    docs_id = fields.Many2one('bibl.bibl', string='Document')
    personnel_id = fields.Many2one('personnel.personnel', string='Responsible')
    state = fields.Selection([('done', 'Issued'), ('return', 'returned')], string='Status', default='done')

    def action_done(self):
        if self.date_emprunt > self.date_retour:
            raise UserError("You should Change Date of Borrow ")

        else:
         self.state = 'done'
         return True

    def action_cancel(self):
       if self.date_retour > datetime.date.today():
          self.penalty = self.penalty+10.0
          if self.penalty > 30.0:
              raise UserError("You cannot Borrow a book for 1 week")

       else:
          self.state = 'return'
       return True

    def print_fich(self):
       return self.env.ref('Library.report_penalty').report_action(self)


