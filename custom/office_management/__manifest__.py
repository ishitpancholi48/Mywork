# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Office Management',
    'category': '',
    'version': '16.0',
    'summary': """ Managments are made up here""",
    'description': """ Module is for managing office """,
    'depends': ["sale","purchase"],

    'data': ['security/ir.model.access.csv',
             'views/management_view.xml',
             'views/service_view.xml',
             'views/query_view.xml',
             'views/sale_order.xml',
             'views/inventory_view.xml',
             'views/purchase_order_inherit.xml',
             'views/new_employee.xml',
             'wizard/office_staff_wizard_view.xml',
             ],

    #'images': [],
    # 'images': ['static/description/odd.png'],
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