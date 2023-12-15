from odoo import models, fields, api, exceptions
from datetime import timedelta

class AcademyCourse(models.Model):
    _name = 'academy.course'
    _description = ' Open Academy Course'
    _rec_name = 'course_name'

    course_name = fields.Char(string='Academy Course', help='Select Your Course')
    course_description = fields.Text(string='Course Description', help='Course Descriptions')

    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string='Sessions')

    # This Fucntion use for copy and search count for field course_name
    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count([("course_name", "=like", u"Copy of {}%".format(self.course_name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.course_name)
        else:
            new_name = u"Copy of {} ({})".format(self.course_name, copied_count)
        default["course_name"] = new_name
        return super(AcademyCourse, self).copy(default)

    def send_birthday_alert_email(self):
        for employee in self.env['hr.employee'].search([('birthday', '!=', False)]):
            if (employee.birthday - fields.Date.today()).days <= 7:
                mail_value = {
                    'email_to': 'odoo.demo.local@gmail.com',
                    'subject': "Birthday Reminder for %s" % employee.name,
                    'recipient_ids': [(6, 0, [66])],
                    'body_html': "Reminder Email: Employee %s has upcoming birthday on %s"
                }
                mail = self.env['mail.mail'].sudo().create(mail_value)
                mail.send()
                print("Executed")

class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'Open Academy Session'
    _rec_name = 'session_name'


    session_name = fields.Char(string="Session Name", required=True, help='Enter Session Name')
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True, compute="_get_end_date", inverse="_set_end_date")
    duration = fields.Float(string="Duration", digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ('instructor', '=', True),
                                                                                ('category_id.name', 'ilike',
                                                                                 "Teacher")])
    course_id = fields.Many2one('academy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    active = fields.Boolean()
    attendees_count = fields.Integer(string="Attendees Count", compute="_get_attendees_count", store=True)
    color = fields.Char()
    email_sent = fields.Boolean('Email',default=False)



    @api.model
    def create(self, vals):
        res = super(OpenAcademySession, self).create(vals)
        res.active = True
        return res

    def get_us_country(self):
        country = self.env['res.partner'].search([('country_id', '=', 'US')])
        a= len(country)
        for rec in self:
            rec.attendee_ids = country

    @api.constrains('session_name')
    def session_name_validation(self):
        if self.session_name == 'MBA':
            raise exceptions.ValidationError('MBA is not in session')
        elif self.session_name == 'Mba':
            raise exceptions.ValidationError('Mba is not in session')
        elif self.session_name == 'mba':
            raise exceptions.ValidationError('mba is not in session')
        else:
            print("Session:-",self.session_name)

    # This function use for seats length
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats


    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    # this function use for verify valid seats
    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }


    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.duration):
                rec.end_date = rec.start_date
                continue

            # Add duration to start_date but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=rec.duration, seconds=-1)
            rec.end_date = rec.start_date + duration

    def _set_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.end_date):
                continue
            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            rec.duration = (rec.end_date - rec.start_date).days + 1

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for rec in self:
            if rec.instructor_id in rec.attendee_ids:
                raise exceptions.ValidationError("A session's instructor cannot be an attendee!!")


