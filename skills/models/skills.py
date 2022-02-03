# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError


class Skills(models.Model):
    _name = 'skills'

    def _compute_name_skill(self):
        partner = ""
        skill = ""
        percent = ""
        if self.partner_id:
            partner = self.partner_id.name

        if self.percent:
            percent = self.percent

        if self.skill:
            skill = self.skill

        self.name = partner + "/" + str(percent) + "/" + skill

    name = fields.Char(string="Name", compute='_compute_name_skill')
    skill = fields.Char(string="Skill")
    years = fields.Integer(string='Years', default=0)
    percent = fields.Float(string='Percent', default=0.00)
    partner_id = fields.Many2one(string="Partner", comodel_name="res.partner", required=True)
    company_id = fields.Many2one(comodel_name='res.company', string='Company', default=lambda self: self.env.company)

    @api.onchange('years')
    def _onchange_years(self):
        if self.years < 0:
            raise UserError('Debes agregar un número valido de años')

    @api.onchange('percent')
    def _onchange_percent(self):
        if self.percent > 100 or self.percent < 0:
            raise UserError('Debes agregar un porcentaje en un rango entre 0 y 100 %')
