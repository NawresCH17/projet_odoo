from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,UserError


class Student(models.Model):
    _name = 'eleve.eleve'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'formation.eleve'
    _order = "id desc"

    student_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    name = fields.Char(string="N° registration")
    first_name = fields.Char(string="first name")
    last_name = fields.Char(string="last name")
    photo = fields.Binary(string="Picture")
    date_birth = fields.Date(string="Date Birth", default='')
    gender = fields.Selection([('masculin', 'Men'), ('feminin', 'Women')], string="Gender", default='')
    nationality = fields.Many2one('res.country', string="Nationality", default=216)
    telephone = fields.Char(string="Phone", track_visibility='onchange', default='')
    email = fields.Char(string="E-mail", track_visibility='always')
    address = fields.Text(string="Address", default='')
    num_cin = fields.Char(string="N° Nationality Card")
    status = fields.Selection([('N', 'New'), ('D', 'Doubling')], string='Status', default='N')
    reg_ids = fields.One2many('registration.registration', 'student_id', string='Inscription')
    class_id = fields.Many2one('class.class', string='Class')
    sign_signature = fields.Binary(string="Digital Signature")

    conduite_ids = fields.One2many('conduite.conduite','eleve_id',string='Conduite')

    absences = fields.Integer(string="Absence", compute="_compute_absence")
    retard = fields.Integer(string="Absence", compute="_compute_retard")

    @api.depends('first_name', 'last_name')
    def name_get(self):
        result = []
        for test in self:
            name = test.first_name + ' ' + test.last_name
            result.append((test.id, name))
        return result

    @api.depends('conduite_ids')
    def _compute_absence(self):
        for conduit in self:
            conduite_ids = conduit.sudo().conduite_ids
            conduit.absences = len(conduite_ids)

    def print_carte(self):
       return self.env.ref('formation.report_carte').report_action(self)

    def print_fich(self):
       return self.env.ref('formation.report_fich').report_action(self)

    def print_list(self):
       return self.env.ref('formation.report_list').report_action(self)

    @api.model
    def create(self, values):
            # if values.get('reference', _('New')) == _('New'):
            #     values['reference'] = self.env['ir.sequence'].next_by_code('university.teacher.seq') or _('New')
            # res = super(UniversityTeacher, self).create(values)

        vals_user = {
              'name': values.get('first_name'),
              'login': values.get('email'),
              'password': values.get('email'),
                # other required field
            }
        user_id = self.env['res.users'].sudo().create(vals_user)
        values.update(student_id=user_id.id)
        res = super(Student, self).create(values)
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            students = self.env['eleve.eleve'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if students:
                raise ValidationError(_("Name %s Already Exists" % rec.name))




