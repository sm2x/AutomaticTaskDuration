# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    is_start = fields.Boolean(default=False)
    start_date = fields.Datetime()
    end_date = fields.Datetime()

    @api.multi
    def start_timer(self):
        """
        Start the Timmer.
        """
        self.write({'is_start': True,
                    'start_date': fields.Datetime.now()})

    @api.multi
    def end_timer(self):
        """
        End the Timmer.
        """
        self.write({'end_date': fields.Datetime.now()})
        ctx = self._context.copy()
        ctx.update({'start_date': self.start_date, 'end_date': self.end_date})
        return {
            'view_id': self.env.ref('project_task_timer.view_task_entry').ids,
            'view_type': 'form',
            "view_mode": 'form',
            'res_model': 'task.entry',
            'type': 'ir.actions.act_window',
            'context': ctx,
            'target': 'new'
        }
