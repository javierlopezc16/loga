from odoo import api, fields, models


class AccountPaymentTermLine(models.Model):
    _inherit = 'account.payment.term.line'

    concept = fields.Char(string='Concepto')

