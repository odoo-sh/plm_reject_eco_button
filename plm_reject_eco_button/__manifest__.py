# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    "name": "Plm Reject Eco Button",
    "summary": """
        Module adds reject stage in ECO""",
    "version": "15.0.1.0.0",
    "category": "Uncategorized",
    "website": "http://sodexis.com/",
    "author": "Sodexis",
    "license": "OPL-1",
    "installable": True,
    "application": False,
    "depends": [
        'base',
        'mrp_plm',
    ],
    "data": [
        "data/mrp_data.xml",
        "views/mrp_eco_views.xml",
        "views/res_config_settings_views.xml"
    ],
}
