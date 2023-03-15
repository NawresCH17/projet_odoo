from odoo import models, fields, api


class Document(models.Model):
    _name = 'bib.bib'
    name = fields.Char(string="Titre", required=True)
    description = fields.Text()
    author_name = fields.Many2many('res.partner', string='Authors')
    publisher_id = fields.Many2one('res.partner', string='Editeur')
    image = fields.Binary('Cover')
    book_id = fields.Integer(string='idlivre', required=True)
    book_release_date = fields.Date(string='Book release date')
    book_Category = fields.Selection([('D','Documents'), ('M','Magazines'), ('R','Reports'), ('A','Others')], 'Books Categories')


class InscriptionBiblio(models.Model):
    _name = 'biblio.inscription'

    nom_utilisateur = fields.Many2one('res.users', string='User')
    date_debut_inscription = fields.Date(string='Date inscription ')
    date_fin_inscription = fields.Date(string='Date end inscription ')
    nombre_livres_lus = fields.Integer(string='The number of books read per user')


class LibrairieGeneral(models.Model):
    _name = 'biblio.general'

    total_number_of_books = fields.Integer(string='total number of books', required=True)
    number_of_books_out = fields.Integer(string='number of books released', required=True)
    date_situation = fields.Date(string='Date of the situation of the library', default=fields.Date.today)
    taken_books_percentage = fields.Float(string="Percentage of books released", compute='_taken_books')

    @api.depends('number_of_books_out', 'total_number_of_books')
    def _taken_books(self):
        self.taken_books_percentage = self.number_of_books_out / self.total_number_of_books * 100 \
            if self.total_number_of_books != 0 \
            else 0
