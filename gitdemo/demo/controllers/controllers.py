# -*- coding: utf-8 -*-
from odoo import http

# class Gitdemo(http.Controller):
#     @http.route('/gitdemo/gitdemo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gitdemo/gitdemo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gitdemo.listing', {
#             'root': '/gitdemo/gitdemo',
#             'objects': http.request.env['gitdemo.gitdemo'].search([]),
#         })

#     @http.route('/gitdemo/gitdemo/objects/<model("gitdemo.gitdemo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gitdemo.object', {
#             'object': obj
#         })