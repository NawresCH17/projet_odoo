from odoo import models, fields, api
from odoo.exceptions import UserError


class Prof(models.Model):
    _inherit = 'hr.employee'
    # _name = 'teacher.teacher'

    age = fields.Integer(string='Age')
    cin = fields.Char(string='CIN')
    class_id = fields.One2many('class.class', 'prof_ids', string='Class')


class Personnel(models.Model):
    _name = 'personnel.personnel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'personnel.personnel'

    personnel_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    first_name = fields.Char(string="first name", required=True)
    last_name = fields.Char(string="last name")
    photo = fields.Binary(string="Picture")
    date_birth = fields.Date(string="Date Birth", default='')
    gender = fields.Selection([('masculin', 'Men'), ('feminin', 'Women')], string="Gender", default='')
    telephone = fields.Char(string="Phone", track_visibility='onchange', default='')
    email = fields.Char(string="E-mail",required=True)
    address = fields.Text(string="Address", default='')
    num_cin = fields.Char(string="N° Nationality Card")
    position = fields.Selection([('personnel', 'personnel_library'), ('service', 'student_service'), ('o', 'others')], string='Position', default='')
    status = fields.Selection([('PE','permanent'), ('F','flying'), ('P','partiel')], string='Status', default='P')

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
       values.update(personnel_id=user_id.id)
       res = super(Personnel, self).create(values)

       return res