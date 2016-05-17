from datetime import datetime, timedelta

from flask_wtf import Form
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import Required


class PolicyForm(Form):
    location_id = SelectField('Location', validators=[Required()])
    text = StringField('Text')
    starting_time = DateTimeField('Starting Time', default=datetime.now())
    end_time = DateTimeField('End Time', default=datetime.now() + timedelta(1))
    event_type = SelectField('Event Type', validators=[Required()])
    user = StringField('User')
    submit = SubmitField('Submit')

class UserForm(Form):
    pass