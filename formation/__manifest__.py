{
    'name': "Odoo universitaire ",
    'version': '1.0',
    'depends': ['base', 'mail', 'hr','hr_attendance', 'website'],
    'summary': 'application,university,odoo16',
    'author': "stage",
    'category': 'Category',
    'description': """
    Description text
    """,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        # 'views/template/formation.xml',
        # 'views/template/claim.xml',
        'views/formation_views.xml',
        'views/student_view.xml',
        'views/formation_inherit.xml',
        'views/bib_view.xml',
        'views/registration_view.xml',
        'views/claim_view.xml',
        'data/sequence.xml',
        'wizard/wiz_view.xml',
        'wizard/view_import_chart.xml',
        'views/snippet.xml',
        'report/registration.xml',
        'report/report.xml',
        'report/CarteEtud.xml',
        'report/report2.xml',
        'menu.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo.xml'
    ],
    'css': [
        'static/src/css/style.css'
    ],
}
