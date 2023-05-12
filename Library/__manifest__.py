{
    'name': "Odoo universitaire ",
    'version': '1.0',
    'depends': ['base', 'mail', 'formation'],
    'summary': 'application,university,odoo16',
    'author': "stage",
    'category': 'Category',
    'description': """
    Description text
    """,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/bib_view.xml',
        'views/reservation_view.xml',
        'views/emprunt_view.xml',
        'reports/report_cart.xml',
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
