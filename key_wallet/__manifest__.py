# -*- coding: utf-8 -*-
#    Key Wallet to Odoo
#    Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
#    @author Michell Stuttgart <m.faria@itimpacta.org.br>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Key Wallet',
    'version': '10.0.1.0.0',
    'summary': 'Password manager',
    'category': 'Extra',
    'author': 'MultidadosTI',
    'website': 'https://github.com/multidadosti-erp/multidadosti-addons',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/view_res_password.xml',
        'views/view_res_password_category.xml',
    ],
}
