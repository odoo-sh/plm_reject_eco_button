# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    reject_eco = fields.Boolean(
        config_parameter="plm_reject_eco_button.reject_eco", string="Reject Eco from any stage", readonly=False,
    )
    
