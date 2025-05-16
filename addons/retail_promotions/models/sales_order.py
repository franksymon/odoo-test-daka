from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def _apply_promotion_discount(self):
        for line in self:
            if line.product_id:
                today = fields.Date.today()
                promos = self.env['retail.promocion'].search([
                    ('producto_ids', 'in', line.product_id.ids),
                    ('fecha_inicio', '<=', today),
                    ('fecha_fin', '>=', today),
                    ('active', '=', True)
                ])
                if promos:
                    line.discount = max(promos.mapped('descuento'))