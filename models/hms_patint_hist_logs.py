from odoo import models, fields


class HmsPatientHistoryLog(models.Model):
    _name = "hms.patient.history.log"


    description = fields.Text()
    patient_name = fields.Many2one("hms.patient")
