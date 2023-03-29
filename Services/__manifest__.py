{
    'name': "Odoo universitaire ",
    'version': '1.0',
    'depends': ['base', 'mail', 'hr'],
    'summary': 'application,university,odoo16',
    'author': "stage",
    'category': 'Category',
    'description': """
    Description text
    """,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/claim_view.xml',
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
