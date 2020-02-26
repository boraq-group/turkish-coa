# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Turkey - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
Turkey Localization
==========================================================

    Turkey Localization 
    Create account and account group
    """,
    'author': 'boraq',
    'maintainer':'www.boraq.com',
    'depends': ['account'],
    'data': [
        'data/l10n_tr_chart_data.xml',
        'data/account.account.template.csv',
        'data/l10n_tr_chart_post_data.xml',
        'data/account_data.xml',
        'data/account_tax_template_data.xml',
        'data/account.group.csv',
        'data/account_chart_template_data.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': True,
}
