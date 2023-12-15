# -*- coding: utf-8 -*-pack
{  # App information
    'name': 'Shopify to Odoo Connector',
    'category': '',
    'version': '16.0',
    'summary': """ Management are made up of Shopify to Odoo Connector""",
    'description': """ 
            """,
    'depends': ['base','stock','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/shopify_instance_integration.xml',
        'views/order_workflow_automation.xml',
        'views/shopify_location.xml',
        'views/shopify_payment_gateway.xml',
        'views/shopify_financial_status_configuration.xml',
    ],

    'images': ['static/description/icon.png'],
    'author': 'Vraja Technologies',
    'maintainer': 'Vraja Technologies',
    'website': 'https://www.vrajatechnologies.com',
    'live_test_url': 'https://www.vrajatechnologies.com/contactus',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
