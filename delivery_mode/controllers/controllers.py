# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryMode(http.Controller):
#     @http.route('/delivery_mode/delivery_mode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_mode/delivery_mode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_mode.listing', {
#             'root': '/delivery_mode/delivery_mode',
#             'objects': http.request.env['delivery_mode.delivery_mode'].search([]),
#         })

#     @http.route('/delivery_mode/delivery_mode/objects/<model("delivery_mode.delivery_mode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_mode.object', {
#             'object': obj
#         })
