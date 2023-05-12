from odoo import models, fields, api,_
from odoo.exceptions import UserError,ValidationError


# class Prof(models.Model):
#     _inherit = 'hr.employee'
#     # _name = 'teacher.teacher'
#
#     age = fields.Integer(string='Age')
#     cin = fields.Char(string='CIN')
#     prof_ok = fields.Boolean(string='is professor')
#     class_id = fields.One2many('class.class', 'prof_ids', string='Class')
#     sign_signature = fields.Binary(string="Digital Signature")
#     emploi_ids = fields.One2many('emploi.emploi', 'professor_id', string="TimeTable")


class Professor(models.Model):
    _name = 'prof.prof'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'prof.prof'

    first_name = fields.Char(string="first name", required=True, str=True)
    name = fields.Char(string="N° registration")
    prof_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    last_name = fields.Char(string="last name")
    photo = fields.Binary(string="Picture")
    date_birth = fields.Date(string="Date Birth", default='')
    gender = fields.Selection([('masculin', 'Men'), ('feminin', 'Women')], string="Gender", default='')
    telephone = fields.Char(string="Phone", track_visibility='onchange', default='')
    email = fields.Char(string="E-mail", required=True)
    address = fields.Text(string="Address", default='')
    num_cin = fields.Char(string="N° Nationality Card")
    # class_id = fields.Many2one('class.class', string='Class')
    class_id = fields.Many2many('class.class', relation='prof_class_rel', column1='first_name', column2='name')
    sign_signature = fields.Binary(string="Digital Signature")
    emploi_ids = fields.One2many('emploi.emploi', 'prof_id', string="TimeTable")
    status = fields.Selection([('PE', 'permanent'), ('F', 'flying'), ('P', 'partiel')], string='Status', default='P')
    sign_signature = fields.Binary(string="Digital Signature")
    date_takenup = fields.Date(string="Date TakenUp", default='')
    time = fields.Integer(compute='_compute_time', string="TimeTable")
    matter_id = fields.One2many('matter.matter', 'prof_ids', string='Matter')

    @api.depends('first_name', 'last_name')
    def name_get(self):
     result = []
     for test in self:
      name = test.first_name + ' ' + test.last_name
      result.append((test.id, name))
     return result

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
        values.update(prof_id=user_id.id)
        res = super(Professor, self).create(values)

        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            profs = self.env['prof.prof'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if profs:
                raise ValidationError(_("Name %s Already Exists" % rec.name))

    def print_carte(self):
        return self.env.ref('formation.report_card_professor').report_action(self)

    @api.depends('emploi_ids')
    def _compute_time(self):
        self.time = len(self.emploi_ids)


class Personnel(models.Model):
    _name = 'personnel.personnel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'personnel.personnel'

    first_name = fields.Char(string="first name", required=True)
    name = fields.Char(string="N° registration")
    personnel_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    last_name = fields.Char(string="last name")
    photo = fields.Binary(string="Picture")
    date_birth = fields.Date(string="Date Birth", default='')
    gender = fields.Selection([('masculin', 'Men'), ('feminin', 'Women')], string="Gender", default='')
    telephone = fields.Char(string="Phone", track_visibility='onchange', default='')
    email = fields.Char(string="E-mail",required=True)
    address = fields.Text(string="Address", default='')
    num_cin = fields.Char(string="N° Nationality Card")
    position = fields.Selection([('personnel', 'Library service'), ('service', 'student service'),('intern','internship service'),('o', 'others')], string='Position', default='')
    status = fields.Selection([('PE','permanent'), ('F','flying'), ('P','partiel')], string='Status', default='P')
    sign_signature = fields.Binary(string="Digital Signature")
    date_takenup = fields.Date(string="Date TakenUp", default='')
    #service_ids = fields.One2many('services.services', 'personnel_id', string='Service')

    @api.depends('first_name', 'last_name')
    def name_get(self):
        result = []
        for test in self:
            name = test.first_name + ' ' + test.last_name
            result.append((test.id, name))
        return result

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

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            persos = self.env['personnel.personnel'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if persos:
                raise ValidationError(_("Name %s Already Exists" % rec.name))

    def print_carte1(self):
        return self.env.ref('formation.report_cardpersonnel').report_action(self)



