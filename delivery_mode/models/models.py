# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeliveryMode(models.Model):
    _name = 'delivery.mode'
    _description = 'Delivery Mode'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name" ,required=True)

class SaleOrderFormExt(models.Model):
    _inherit = 'sale.order'

    delivery_mode = fields.Many2one(
        'delivery.mode',
        string="Delivery Mode",
        tracking=True,
        context={'create': True, 'delete': True}
    )    
    