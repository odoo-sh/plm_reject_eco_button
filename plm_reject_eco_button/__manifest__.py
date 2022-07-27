# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Plm Reject Eco Button",
    "summary": """
        Short (1 phrase/line) summary of the module"s purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "version": "15.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        'mrp_plm',
    ],
    "data": [
        "views/mrp_eco_views.xml",
    ],
}
