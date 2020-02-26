# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Turkish Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
    CoA Turkish, Account Group, Formal Chart of Account for Turkey with Account groups and default journals with defaults accounts for the journals.
    """,
    'summary': 'CoA Turkish, Formal Chart of Account for Turkey with Account groups and default journals with defaults accounts for the journals.',
    'author': 'Boraq-Group',
    'maintainer':'https://boraq-group.com',
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
