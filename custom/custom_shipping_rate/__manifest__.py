# -*- coding: utf-8 -*-pack

{
    # App information
    'name': 'Custom Shipping Rate',
    'category': '',
    'version': '16.0',
    'summary': """ Custom Shipping Rate""",
    'description': """ Module is custom shipping rate """,
    'depends': ["delivery"],

    'data': ['security/ir.model.access.csv',
             'views/custom_shipping_rules.xml',
             'views/delivery_model_inherit.xml',
             ],

    #'images': [],
    #'images': ['static/description/images.png'],
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