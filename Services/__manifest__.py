{
    'name': "Odoo universitaire ",
    'version': '1.0',
    'depends': ['base', 'mail', 'hr', 'formation'],
    'summary': 'Services&Claims',
    'author': "stage",
    'category': 'Category',
    'description': """
    Description text
    """,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/claim_view.xml',
        'views/template/mail_template.xml',
        'reports/claim_report.xml',
        'reports/service_report.xml',
        'wizard/view_import_chart.xml',
        'menu.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo.xml'
    ],
    'css': [
        # 'static/src/css/style.css'
    ],
}
