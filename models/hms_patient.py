from odoo import  models,fields, api,tools
from odoo.exceptions import UserError
from datetime import date


class Hmspatient(models.Model):
    _name = "hms.patient"
    _rec_name = "fname"


    fname = fields.Char()

    lname = fields.Char()
    birthdate = fields.Date()
    address = fields.Text()
    history = fields.Text()
    cr_ratio = fields.Float()
    
    blood_type = fields.Selection([
        ('A', 'Type A'),
        ('B', 'Type B'),
        ('AB', 'Type AB'),
        ('O', 'Type O')
    ], string='Blood Type')

    pcr_test = fields.Boolean(string='PCR', default=False)
    image = fields.Binary(string='Image')
    patient_status = fields.Selection([
        ('undetermined', 'un'),
        ('good', 'g'),
        ('fair', 'f'),
        ('serious', 's')
    ], string='patient_status')

    depart_name = fields.Many2one("hms.department")
    depart_capcity = fields.Integer(related='depart_name.capcity')
    doctors_of_patient = fields.Many2many("hms.doctor")
    
    
    
    history_logs=fields.One2many("hms.patient.history.log","patient_name")
    
    email = fields.Char(string="Email", required=True)

    @api.constrains('email')
    def _check_valid_email(self):
        for record in self:
            if record.email and  not tools.single_email_re.match(record.email):
                raise UserError(("Enter a valid email address"))
    @api.constrains('cr_ratio')
    def _check_valid_cr_ratio(self):
        for record in self:
            if (record.cr_ratio==0.00 and record.pcr_test==True):
                
                raise UserError(("enter a valid cr_ratio"))

    
    
    
    @api.depends('birthdate')
    def _compute_age(self):
        for rec in self:
            if rec.birthdate:
                today = date.today()
                rec.age = today.year - rec.birthdate.year - ((today.month, today.day) < (rec.birthdate.month, rec.birthdate.day))
                if (rec.age<0):
                    raise UserError(("age cannot be negative"))

            else:
                rec.age = 0

                
    age = fields.Integer(string="Age", compute="_compute_age")
    @api.onchange('age')
    def onchange_age(self):
        if self.age and self.age < 30:
            self.pcr_test = True
            return {
                'warning': {
                    "title": "PCR CHECKED",
                    "message": "PCR has been checked automatically because age is less than 30"
                }
            }

    @api.onchange("patient_status")
    def onchange_status(self):
        if self.patient_status:
            return {
                'warning': {
                    "title": "State Changed",
                    "message": "State is changed %s" %(self.patient_status)
                }
            }

    @api.onchange("history")
    def patient_history(self) :
        if self.history:
            vals={
                "description":"history change to %s" %(self.history),
                "patient_name": self.id
            }
            self.env["hms.patient.history.log"].create(vals)
            
            
    _sql_constraints = [
        ( 'email_check' ,'UNIQUE(email)' ,'email should be Unique') ,
    ]
