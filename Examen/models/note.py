from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Note(models.Model):
    _name = 'note.note'
    _description = 'Gestion des resultats'
    _rec_name = 'eleve_id'

    eleve_id = fields.Many2one('eleve.eleve', string="Student", required=True)
    classe_id = fields.Many2one('class.class', string="Class")
    matter_id = fields.Many2one('matter.matter', string='Matter', required=True)
    coefficient = fields.Integer(string='Coefficient')
    saison = fields.Selection([('s1', 'Semestre 1'), ('s2', 'Semestre 2'), ('s3', 'Semestre 3')], required=True)
    note_intero = fields.Float(string="Note Exam1", store=True, )
    note_devoir = fields.Float(string="Note Exam2", store=True, )
    moy_classe = fields.Float(string="Moy. classe", store=True, )
    note_compo = fields.Float(string="Note composition", store=True, )
    moyenne = fields.Float(string="Moyenne", default=0, store=True, )
    rang = fields.Char(string="Rang", compute="CalculerRang", )
    annee_scolaire = fields.Many2one('year.year', required=True, string="Année scolaire", )
    professeur_id = fields.Many2one('prof.prof', "Professeur")
    appreciation = fields.Char(string='Appréciation', compute='Appreciation')
    non_classe = fields.Boolean(string="Non classé")
    type = fields.Selection([('cc', 'CC'), ('CTR', 'DS exam'), ('sum', 'final exam')], string='Type of exam')


    # @api.onchange('note_compo','moy_classe')
    def CalculerRang(self):
        for rec in self:
            data = list()
            notes = self.env['note.note'].search([
                ('classe_id', '=', rec.classe_id.id),
                ('saison', '=', rec.saison),
                ('coeficient', '=', rec.coeficient),
            ])
            for note in notes:
                data.append(note.moyenne)

            rec.rang = range(rec.moyenne, data)

    @api.onchange('note_intero', 'note_devoir')
    def onchange_note_intero_note_devoir(self):
        for rec in self:
            rec.moy_classe = (rec.note_intero + rec.note_devoir) / 2

    @api.onchange('moy_classe', 'note_compo', 'note_intero', 'note_devoir')
    def Appreciation(self):
        appr = self.env['appreciation.appreciation'].search([])
        for rec in self:
            for ap in appr:
                if rec.moyenne >= ap.inf and rec.moyenne < ap.sup:
                    rec.appreciation = ap.name
                if rec.moyenne >= 20:
                    rec.appreciation = 'Excellent'

    @api.constrains('note_intero', 'note_devoir', 'moy_classe', 'note_compo')
    def check_notes(self):
        for rec in self:
            if rec.note_intero < 0 or rec.note_intero > 20:
                raise ValidationError(
                    _('La note de d\'interogation doit être entre 0 et 20. Vous avez taper : ' + str(rec.note_intero)))
            if rec.note_devoir < 0 or rec.note_devoir > 20:
                raise ValidationError(
                    _('La note  de devoir doit être entre 0 et 20. Vous avez taper : ' + str(rec.note_devoir)))
            if rec.moy_classe < 0 or rec.moy_classe > 20:
                raise ValidationError(
                    _('La moyenne de classe doit être entre 0 et 20. Vous avez taper : ' + str(rec.moy_classe)))
            if rec.note_compo < 0 or rec.note_compo > 20:
                raise ValidationError(
                    _('La note de composition doit être entre 0 et 20. Vous avez taper : ' + str(rec.note_compo)))

    @api.onchange('note_intero', 'note_devoir', 'note_compo', 'moy_classe')
    def _onchange_note_compo(self):
        for rec in self:
            if rec.matter_id.max > 0:
                res = (rec.note_compo + rec.moy_classe) / 2
                if res > 10:
                    rec.moyenne = res - 10
                else:
                    rec.moyenne = 0
            else:
                rec.moyenne = (rec.note_compo + rec.moy_classe) / 2


class Appreciation(models.Model):
    _name = 'appreciation.appreciation'
    _description = 'Gestion des appications'

    name = fields.Char(string="Appréciation")
    inf = fields.Float(string='Inférieur')
    sup = fields.Float(string='Supérieur')


class ResultatExamen(models.Model):
    _name = 'examen.resultat'
    _description = "Result exam"
    _rec_name = 'eleve_id'

    eleve_id = fields.Many2one(
        'eleve.eleve',
        string='Student',
        required=True,
    )
    classe_id = fields.Many2one(
        'class.class',
        string='Class',
        required=True,
    )

    saison = fields.Selection([
        ('s1', 'Semestre 1'),
        ('s2', 'Semestre 2'),
        ('s3', 'Semestre 3')
    ],
        required=True
    )

    annee_scolaire = fields.Many2one(
        'year.year',
        required=True,
        string="Année scolaire",
    )
    moyenne = fields.Float(
        string='Moyenne',
    )
    rang = fields.Char(
        string='Rang',
    )
    result = fields.Selection([('admis', 'Admis'), ('refus', 'Refused')], string='Status')
    state = fields.Selection([('done', 'Valid'), ('cancel', 'Canceled')], string='Status')


class SaisieNote(models.Model):
    _name = 'listenote.listenote'
    _description = 'Gestion des notes'
    _rec_name = 'eleve_id'

    eleve_id = fields.Many2one('eleve.eleve', string="Student", required=True)
    classe_id = fields.Many2one('class.class', string="Class")
    matter_id = fields.Many2one('matter.matter', string='Matter', required=True)
    coefficient = fields.Integer(string='Coefficient')
    saison = fields.Selection([('s1', 'Semestre 1'), ('s2', 'Semestre 2'), ('s3', 'Semestre 3')], required=True)
    note_intero = fields.Float(string="Note Exam1", store=True, )
    note_devoir = fields.Float(string="Note Exam2", store=True, )
    note_cc = fields.Float(string="Note CC", store=True, )
    annee_scolaire = fields.Many2one('year.year', required=True, string="Année scolaire", )
