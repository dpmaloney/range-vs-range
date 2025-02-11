"""
Form for backdoor authentication page
"""
from wtforms.fields.simple import StringField
from wtforms.validators import Length
from flask_wtf import FlaskForm


class BackdoorForm(FlaskForm):  # pylint:disable=R0903
    """
    User declares OIDC subject identifier and email
    """
    backdoor_sub = StringField(label="backdoor_sub",
                             validators=[Length(min=1)])
    backdoor_email = StringField(label="backdoor_email",
                               validators=[Length(min=1)])
