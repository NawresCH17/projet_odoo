# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import time
from datetime import datetime
import tempfile
import binascii
from datetime import date, datetime
import io
from odoo.exceptions import Warning, UserError
from odoo import models, fields, exceptions, api, _
import logging
_logger = logging.getLogger(__name__)

try:
    import xlrd
except ImportError(xlrd):
    _logger.debug('Cannot `import xlrd`.')
try:
    import csv
except ImportError(csv):
    _logger.debug('Cannot `import csv`.')
try:
    import xlwt
except ImportError:
    _logger.debug('Cannot `import xlwt`.')
try:
    import cStringIO
except ImportError:
    _logger.debug('Cannot `import cStringIO`.')
try:
    import base64
except ImportError(base64):
    _logger.debug('Cannot `import base64`.')


class ImportChartAccount(models.TransientModel):
    _name = "import.chart.service"
    _description = "Chart of services"

    File_select = fields.Binary(string="Select Excel File")
    import_option = fields.Selection([('csv', 'CSV File'), ('xls', 'XLS File')], string='Select', default='csv')

    def import_file(self):

        if self.import_option == 'csv':

            keys = ['code', 'name', 'date_ask', 'category', 'student_id']

            try:
                csv_data = base64.b64decode(self.File_select)
                data_file = io.StringIO(csv_data.decode("utf-8"))
                data_file.seek(0)
                file_reader = []
                values = {}
                csv_reader = csv.reader(data_file, delimiter=',')
                file_reader.extend(csv_reader)

            except UserError:
                raise UserError(_("Invalid file!"))

            for i in range(len(file_reader)):
                field = list(map(str, file_reader[i]))
                values = dict(zip(keys, field))
                if values:
                    if i == 0:
                        continue
                    else:
                        values.update({
                            'code': field[0],
                            'name': field[1],
                            'date_ask': field[2],
                            'student_id': field[3],
                            'category': field[4]
                        })
                        return self.create_chart(values)

        # ---------------------------------------
        elif self.import_option == 'xlsx':
            try:
                fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
                fp.write(binascii.a2b_base64(self.File_select))
                fp.seek(0)
                values = {}
                workbook = xlrd.open_workbook(fp.name)
                sheet = workbook.sheet_by_index(0)

            except UserError:
                raise UserError(_("Invalid file!"))

            for row_no in range(sheet.nrows):
                val = {}
                if row_no <= 0:
                    map(lambda row: row.value.encode('utf-8'), sheet.row(row_no))
                else:

                    line = list(
                        map(lambda row: isinstance(row.value, bytes) and row.value.encode('utf-8') or str(row.value),
                            sheet.row(row_no)))

                    values.update({
                        'code': line[0],
                        'name': line[1],
                        'date_ask': line[2],
                        'student_id': line[3],
                        'category': line[4]
                    })
                    res = self.create_chart(values)
        # ------------------------------------------------------------
        else:
            raise UserError(_("Please select any one from xls or csv formate!"))

        return res

    def create_chart(self, values):

        if values.get("code") == "":
            raise UserError(_('Code field cannot be empty.'))

        if values.get("name") == "":
            raise UserError(_('Name field cannot be empty.'))

        if values.get("date_ask") == "":
            raise UserError(_('type field cannot be empty.'))

        if values.get("code"):
            s = str(values.get("code"))
            code_no = s.rstrip('0').rstrip('.') if '.' in s else s

        service_obj = self.env['service.service']

        data = {
            'code': code_no,
            'name': values.get('name'),
            'date_ask': values.get('date_ask'),
            'category': values.get('category')
        }
        chart_id = service_obj.create(data)

        return chart_id
