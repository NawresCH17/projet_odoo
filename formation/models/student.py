from odoo import models, fields, api
from odoo.exceptions import UserError


class Student(models.Model):
    _name = 'eleve.eleve'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'formation.eleve'

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

    def print_carte(self):
        return self.env.ref('formation.report_carte').report_action(self)

    # @api.model_create_multi
    # def create(self, values):
    #     res = super(Student, self).create(values)
    #
    #
    #     user = cls.env['res.users'].create({
    #         'name': res.first_name,
    #         'login': 'res.email',
    #         'password': 'res.email',
    #         # 'groups_id': [Command.set(cls.env.user.groups_id.ids),
    #         #               Command.link(cls.env.ref('account.group_account_user').id)],
    #         'group_id:' [(6, 0, opp_ids)]
    #     })
    #
    #     return res

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
