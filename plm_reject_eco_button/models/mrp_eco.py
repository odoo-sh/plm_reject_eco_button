# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models, fields, api

class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    rejected_stage = fields.Boolean(related="stage_id.rejected_stage")
    reject_eco = fields.Boolean(compute="_compute_reject_eco")

    def action_recject_eco(self):
        eco_stage_id=self.env['mrp.eco.stage'].search([
            ('rejected_stage','=',True),
            ('type_ids', 'in', self.type_id.id)], limit=1)
        eco_stage_id.with_context(eco_id=self)._compute_is_blocking()
        self._compute_allow_change_stage()
        self.stage_id = eco_stage_id

    @api.depends('kanban_state', 'stage_id', 'approval_ids')
    def _compute_allow_change_stage(self):
        super()._compute_allow_change_stage()
        for rec in self:
            if rec._context.get('reject_eco', False):
                rec.allow_change_stage= True

    @api.depends('stage_id','state','kanban_state')
    def _compute_reject_eco(self):
        for rec in self:
            rec.reject_eco=False
            reject_eco=self.env['ir.config_parameter'].sudo().get_param('plm_reject_eco_button.reject_eco',default=False)
            if reject_eco:
                rec.reject_eco=True
            elif rec.stage_id.approval_template_ids and not reject_eco and self.env.user in rec.stage_id.approval_template_ids.mapped('user_ids'):
                rec.reject_eco=True



class MrpEcoStage(models.Model):
    _inherit = 'mrp.eco.stage'

    @api.depends('approval_template_ids.approval_type')
    def _compute_is_blocking(self):
        super()._compute_is_blocking()
        eco_id=self._context.get('eco_id',False)
        if eco_id:
            current_stage_id = eco_id.stage_id
            for eco in self:
                blocking_stage_eco_ids=eco.search([
                        ('sequence', '>=', current_stage_id.sequence),
                        ('sequence', '<=', eco.sequence),
                        ('type_ids', 'in', eco_id.type_id.id),
                        ('id', 'not in', [eco.id] + [current_stage_id.id]),
                        ('is_blocking', '=', True)])
                blocking_stage_eco_ids.write({'is_blocking':False})
