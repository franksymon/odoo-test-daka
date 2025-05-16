from odoo import models, fields, api

class Promocion(models.Model):
    _name = 'retail.promocion'
    _description = 'Promoción Retail'  
    _order = 'fecha_inicio DESC'

    name = fields.Char(string='Nombre', required=True)
    active = fields.Boolean(string='Activa', default=True)
    descuento = fields.Float(string='Descuento (%)', digits=(3, 2))  
    fecha_inicio = fields.Date(string='Fecha Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha Fin', required=True)
    producto_ids = fields.Many2many(
        'product.product', 
        string='Productos',
        domain="[('sale_ok', '=', True)]"
    )

    _sql_constraints = [
        ('check_descuento', 'CHECK(descuento >= 0 AND descuento <= 100)', 'El descuento debe estar entre 0% y 100%'),
        ('check_fechas', 'CHECK(fecha_fin >= fecha_inicio)', 'La fecha fin debe ser posterior a la fecha inicio')
    ]