from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    helpdesk_id = fields.Many2one('helpdesk.phonecall.service',
                                  string='Helpdesk')
