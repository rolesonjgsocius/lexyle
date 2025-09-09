# -*- coding: utf-8 -*-
{
    "name": "Lexyle",
    "summary": "Lexyle",
    "version": "17.0.1.0.0",
    "author": "SIGB",
    "license": "LGPL-3",
    "category": "Uncategorized",
    "application": True,
    "installable": True,
    "depends": [
        "website",
        "web",
        "base", "website_sale","crm"
    ],
    "data": [
        "views/Lexyle_cybersecurity.xml",
        "views/display_page.xml",
        "views/home.xml",
        "views/LMS.xml",
        "views/gamification.xml",
        "views/ai.xml",
        'views/Snippets/header.xml',
        'views/Snippets/footer.xml',
        'views/Lexyle_Internships.xml',
        'views/custom_styles_odoo.xml',
        'views/careers.xml',
        'views/termsandconditions.xml',
        'views/crm_forms_custom.xml',
    ],
    "assets": {
        "web.assets_frontend": [
            'Lexyle/static/src/css/custom_global.css',

        ],
        "web.assets_backend": [
        ]
    }
}
