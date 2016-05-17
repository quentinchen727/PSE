from flask_wtf import Form
from wtforms import StringField, SubmitField, DateTimeField, SelectField
from wtforms.validators import Required


class PolicyForm(Form):
    location_id = SelectField('Location', validators=[Required()])