
from odoo.http import Controller, request, Response, route


class Formation(Controller):
    @route('/formation', type='http', auth='public')
    def render_web_page(self):
        return request.render('formation.formation_page', {})

    # @http.route('/formation/claim', type='http', auth='public')
    # def navigate_to_another_page(self):
    #     claim_ids = http.request.env['claim.claim'].sudo().search([])
    #     return http.request.render('claim_page', {'claim_ids': claim_ids})
