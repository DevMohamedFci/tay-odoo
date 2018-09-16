# -*- coding: utf-8 -*-
from odoo import http

# class Leadreport(http.Controller):
#     @http.route('/tay_account/tay_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tay_account/tay_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tay_account.listing', {
#             'root': '/tay_account/tay_account',
#             'objects': http.request.env['tay_account.tay_account'].search([]),
#         })

#     @http.route('/tay_account/tay_account/objects/<model("tay_account.tay_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tay_account.object', {
#             'object': obj
#         })