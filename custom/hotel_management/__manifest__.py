# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Hotel Management',
    'category': '',
    'version': '16.0',
    'summary': """ Managments are made up here Hotel Management""",
    'description': """ Hotel Management module for 
            - Restaurant
            - Staff
            - Hotel Room
            - Banquent Hall
            """,
    'depends': ["stock", "mail"],

    'data': [
        'security/ir.model.access.csv',
        'views/hotel_customer_view.xml',
        'views/hotel_restaurant_view.xml',
        'views/hotel_customer_order_view.xml',
        'views/hotel_laundary_view.xml',
        'data/demo_data_hotel_restaurant.xml',

    ],

    'images' : ['static/description/icon.png'],

    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
