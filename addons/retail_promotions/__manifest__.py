{
    'name': 'Retail Promotions',
    'version': '1.0',
    'author': 'Frank Urbina',
    'category': 'Sales',
    'summary': 'Gestión de promociones con descuentos automáticos en ventas',
    'description': """
        Aplica descuentos automáticos en órdenes de venta
        basados en promociones activas y vigentes.
    """,
    'depends': [
        'sale_management',         
        'product',      
        'stock'         
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/promocion_views.xml',
        'views/sale_order_views.xml',
        'report/promocion_report.xml',    
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',  
    'sequence': 10,       
}