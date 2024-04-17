from odoo import models, fields, api

class ServiceOrder(models.Model):
    _name = 'service.order'
    _description = 'Service Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    purchase_order_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)
    service_date = fields.Date(string='Service Date')
    location_id = fields.Many2one('stock.location', string='Service Location')
    product_ids = fields.Many2many('product.product', string='Products Used')
    total_products = fields.Integer(string='Total Products', compute='_compute_total_products')

    @api.depends('product_ids')
    def _compute_total_products(self):
        for record in self:
            record.total_products = len(record.product_ids)