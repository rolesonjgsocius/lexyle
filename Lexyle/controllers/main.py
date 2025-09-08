# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.http import request


class WebsiteProductController(http.Controller):

    @http.route('/', type='http', auth="public", website=True)
    def homepage(self, **kwargs):
        return request.render('Lexyle.Lexyle_HOME')

    @http.route('/career_form', type='http', auth="public", website=True)
    def career_forms(self, **kwargs):
        return request.render('Lexyle.career_form')

    @http.route('/lms', type='http', auth="public", website=True)
    def lms(self, **kwargs):
        return request.render('Lexyle.Lexyle_LMS')

    @http.route('/gamification', type='http', auth="public", website=True)
    def gamification(self, **kwargs):
        return request.render('Lexyle.Lexyle_gamification')

    @http.route('/ai', type='http', auth="public", website=True)
    def ai(self, **kwargs):
        return request.render('Lexyle.Lexyle_ai')

    @http.route('/Internships', type='http', auth="public", website=True)
    def Internships(self, **kwargs):
        return request.render('Lexyle.Lexyle_Internships')

    @http.route('/careers', type='http', auth="public", website=True)
    def Lexyle_Careers(self, **kwargs):
        return request.render('Lexyle.Lexyle_Careers')

    @http.route('/termsandconditions', type='http', auth="public", website=True)
    def termsandconditions(self, **kwargs):
        return request.render('Lexyle.Lexyle_TermsandConditions')

    @http.route('/cybersecurity', type='http', auth="public", website=True)
    def Lexyle_cybersecurity(self, **kwargs):
        return request.render('Lexyle.Lexyle_cybersecurity')




