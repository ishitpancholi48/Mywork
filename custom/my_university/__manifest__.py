# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'My University',
    'category': '',
    'version': '16.0',
    'summary': """ University""",
    'description': """ Module is for university """,
    'depends': ['open_academy'],

    'data': ['security/ir.model.access.csv',
             'views/university_view.xml',
             'views/college_course.xml',
             # 'views/openacademy_session_inherit_view.xml',
             'wizard/college_university_wizard_view.xml',
             ],

    'images': [],
    # 'images': ['static/description/christmas.gif'],
    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'price': '101',
    # 'currency': 'EUR',
    'license': 'LGPL-3',
}