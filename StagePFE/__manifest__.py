{
    'name': "Odoo universitaire ",
    'version': '1.0',
    'depends': ['base', 'mail', 'hr', 'formation'],
    'summary': 'Stage PFE',
    'author': "stage",
    'category': 'Category',
    'description': """
    Description text
    """,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/convention_view.xml',
        'views/documents_view.xml',
        'views/plan_view.xml',
        'reports/report_convention.xml',
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
