# -*- coding: utf-8 -*-
#    General Views Customize to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'General Views Customize',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'summary': 'General Views Customize to Odoo',
    'category': 'Web',
    'sequence': 99,
    'depends': [
        'web',
        'crm',
        'web_settings_dashboard',
        'document',
        'br_base',
    ],
    'data': [
        'views/multi_assets.xml',
        'views/general_views_customize.xml',
    ],
    'qweb': [
        'static/src/xml/base.xml',
        'static/src/xml/dashboard.xml',
    ],
    'installable': True,
}
