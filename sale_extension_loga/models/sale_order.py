from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_type = fields.Selection(
        selection=[
            ('parking_lot', "Esta/Estac"),
        ],
        string="Tipo de producto Loga",
        help="Campo para seleccionar el tipo de producto de Loga.")

    floor = fields.Char(string='Piso')

    orientation = fields.Char(string='Orient.')

    useful = fields.Char(string='Útil')

    terrace = fields.Char(string='Terraza')

    total_surface = fields.Char(string='Total')

