{
    'name': "Odoo universitaire ",
    'version': '1.0',
    'depends': ['base', 'mail', 'hr', 'hr_attendance', 'website'],
    'summary': 'Formation&Inscription',
    'author': "stage",
    'category': 'Category',
    'description': """
    Description text
    """,

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'controller/claim.xml',
        'controller/formation.xml',
        'views/registration_view.xml',
        'views/student_view.xml',
        'views/formation_views.xml',
        'views/attendance_view.xml',
        'views/emploi_view.xml',
        'views/Timetable_view.xml',
        'views/personnel_view.xml',
        'views/prof_view.xml',
        'data/sequence.xml',
        'wizard/liste_student_view.xml',
        'wizard/list_timetable_view.xml',
        'views/snippet.xml',
        'report/registration.xml',
        'report/CarteEtud.xml',
        'report/cartePerso.xml',
        'report/CardProf.xml',
        'report/Fich_student.xml',
        'report/student_list.xml',
        'report/liste_eleves_classe.xml',
        'report/timetable.xml',
        'report/emploi_report.xml',
        'report/timetable_class.xml',
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
