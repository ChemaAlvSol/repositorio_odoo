# -*- coding: utf-8 -*-
{
    'name': 'Skills',
    'summary': 'Módulo de habilidades por contactos',
    'description': '''
    * Módulo para la generación de habilidades por contactos.
    ''',
    "website": "",
    'author': 'JOSE MARIA HERIBERTO ALVARADO SOLORZANO',
    'version': '1.0',
    'category': 'skills',
    'depends': [
        'contacts'
    ],
    'data': [
        'skills/views/menu.xml',
        'skills/security/ir.model.access.csv',
        'skills/security/security.xml',
    ],
    'installable': True,
    'application': True
}