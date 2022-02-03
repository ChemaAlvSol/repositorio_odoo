# -*- encoding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _calculate_skills_quantity(self):
        count = 0
        skills = self.env['skills'].search([('partner_id.id', '=', self.id)])
        if skills:
            for line in skills:
                count += 1
        self.skills_number = count

    skills_number = fields.Integer(string="Skills quantity", compute="_calculate_skills_quantity")

    def create(self, vals):
        result = super(ResPartner, self).create(vals)
        # se crea la nueva habilidad
        skills = self.create({
                'percent': 0,
                'years': 0,
                'partner_id': result.id
            })

        return result
