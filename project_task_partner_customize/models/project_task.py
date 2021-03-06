from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   related='project_id.partner_ids',
                                   string='Related Partners')

    # Atributo default foi sobrescrito para evitar que o usuario fosse
    # atribuido automaticamente por engano
    user_id = fields.Many2one(default=False)

    @api.model
    def create(self, values):
        project_task = super(ProjectTask, self).create(values)
        self._send_message(values=values, project_task=project_task)
        return project_task

    @api.multi
    def write(self, values):
        ret = super(ProjectTask, self).write(values)
        self._send_message(values=values, project_task=self)
        return ret

    def _send_message(self, values, project_task):

        if 'user_id' in values and values.get('user_id'):

            post_vars = {
                'subject': 'Nova tarefa atribuída a você',
                'body': 'Tarefa: %s atribuída a você.' % project_task.name,
                'partner_ids': [(4, project_task.user_id.partner_id.id)],
                'message_type': 'notification',
                'subtype': 'mt_comment',
            }

            self.env['mail.thread'].message_post(**post_vars)
            return True
        else:
            return False
