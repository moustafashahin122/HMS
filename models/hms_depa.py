from odoo import models , fields

class Hmsdepartent(models.Model) :
    _name = "hms.department"
    _rec_name= "name"
    #hello
    
    name = fields.Char()
    capcity = fields.Integer()
    is_opened = fields.Boolean(string="Open")
    #memo
    patient_ids = fields.One2many("hms.patient" , "depart_name" ,readonly=True)
    doctors_department = fields.Many2many("hms.doctor")
    
    
    # student_ids = fields.One2many('iti.student' , 'track_id' , readonly = True)

