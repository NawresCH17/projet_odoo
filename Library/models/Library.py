from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError


class Document(models.Model):
    _name = 'bibl.bibl'

    name = fields.Char(string="Titre", required=True)
    description = fields.Text(string='Description')
    image = fields.Binary('Cover')
    book_id = fields.Integer(string='idlivre', required=True)
    book_release_date = fields.Date(string='Book release date')
    book_Category = fields.Selection([('D','Documents'), ('M','Magazines'), ('R','Reports'), ('A','Others')], 'Books Categories')
    code = fields.Char(string='Code', required=False, readonly=False)
    Etat = fields.Selection([('disponible', 'Disponible'), ('pris', 'Pris')], string='Etat')
    auteur = fields.Many2many('res.users', string='authors')
    publisher = fields.Many2one('res.users', string='Publisher')
    published = fields.Boolean('Published')
    published_date = fields.Date(string="Published Date")
    reserv_id = fields.One2many('reserv.reserv', 'res_id', string='Reservation')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'Medium'),
         ('3', 'High')],
        'Rating', default='1')


class InscriptionBiblio(models.Model):
    _name = 'bibl.inscription'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=False, readonly=False)
    nom_utilisateur = fields.Many2one('res.users', string='User')
    library_ok = fields.Boolean(string="Library Member")
    photo = fields.Binary(string="Picture")
    date_debut_inscription = fields.Date(string='Date inscription ')
    date_fin_inscription = fields.Date(string='Date end inscription ')
    limit = fields.Integer(string='limit of books')
    nombre_livres_lus = fields.Integer(string='The number of books read per user')
    state = fields.Selection([('new', 'New'), ('done', 'Valid'), ('cancel', 'Canceled')], string='Status', default='new')

    def action_new(self):
        self.state = 'new'
        return True

    def action_done(self):
        if self.nombre_livres_lus> self.limit:
            raise UserError("you cannot take a book,you touch your limit")
        self.state = 'done'
        return True

    def action_cancel(self):
        self.state = 'cancel'
        return True

    def print_carte(self):
     return self.env.ref('Library.report_card').report_action(self)


class LibrairieGeneral(models.Model):
    _name = 'bibl.general'

    name = fields.Char(string='Name', required=False, readonly=False)
    total_number_of_books = fields.Integer(string='total number of books', required=True)
    number_of_books_out = fields.Integer(string='number of books released', required=True)
    date_situation = fields.Date(string='Date', default=fields.Date.today)
    taken_books_percentage = fields.Float(string="Percentage of books released", compute='_taken_books')

    @api.depends('number_of_books_out', 'total_number_of_books')
    def _taken_books(self):
        self.taken_books_percentage = self.number_of_books_out / self.total_number_of_books * 100 \
            if self.total_number_of_books != 0 \
            else 0
