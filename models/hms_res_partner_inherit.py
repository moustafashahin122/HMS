from odoo import models, fields,api

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    related_patient = fields.Many2one("hms.patient")



    email = fields.Char(string='Email')

    _sql_constraints = [
        ( 'email_check' ,'UNIQUE(email)' ,'email should be Unique') ,
    ]
