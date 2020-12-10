# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CoA Turkey Accounting',
    'version': '14.0.1.0',
    'category': 'Localization',
    'description': """
CoA Turkish, Account Group, Formal Chart of Account for Turkey with Account groups and default journals with defaults accounts for the journals.
""",
    'author': 'Boraq-Group',
    'maintainer':'https://boraq-group.com',
    'depends': ['account'],
    "images" : ['static/description/banner.png'],
    'data': [
        'data/l10n_tr_chart_data.xml',
        'data/account.group.csv',
        'data/account.account.template.csv',
        'data/l10n_tr_chart_post_data.xml',
        'data/account_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_data.xml',
        "data/account_group_parent.xml",
        "data/account_account_group.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
