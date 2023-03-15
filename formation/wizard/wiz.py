from odoo import models, fields, api
from datetime import date, datetime


class wiz_calc_age(models.TransientModel):
    _name = 'calc.age.wiz'

    from_date = fields.Date("From Date", required=True)

    @api.multi
    def calc_age(self):
        hr_obj = self.env['res.partner']
        for rec in self:
            student_ids = hr_obj.search([('birthday', '<=', rec.from_date)])
            for student in student_ids:
                birthday = student.birthday
                if birthday:
                    student.age = (datetime.now() - datetime.strptime(birthday, '%Y-%m-%d')).days / 365
        return True
