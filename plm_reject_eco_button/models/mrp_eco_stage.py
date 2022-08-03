# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields, api

class MrpEcoStage(models.Model):
    _inherit = 'mrp.eco.stage'

    rejected_stage=fields.Boolean(help='Helps to determine the Rejected state')