# -*- coding: utf-8 -*-

{
    'name': 'Project Task Partner Customize',
    'version': '10.0.1.0.0',
    'author': 'MultidadosTI',
    'maintainer': 'MultidadosTI',
    'website': 'www.multidadosti.com.br',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Replace partner field on project task screen',
    'contributors': [
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project_related_partners',
    ],
    'data': [
        'views/project_task.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
