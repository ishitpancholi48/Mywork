# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Open Academy',
    'category': '',
    'version': '16.0',
    'summary': """ Managments are made up here Open Academy""",
    'description': """ Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
            """,
    'depends': ['base', 'board','mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_cron.xml',
        'wizard/open_academy_wizard_view.xml',
        'views/academy_course_view.xml',
        'views/res_partner_view.xml',
        'views/session_board.xml',
        'views/sale_order_inherit_view.xml',
        'views/stock_picking_view.xml',
        'reports/openacademy_report.xml',
    ],
    'demo': [
        'demo/demo_data_course.xml',
    ],
    'images': ['static/description/icon.png'],
    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'AGPL-3',
}
