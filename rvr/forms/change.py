"""
Form for change of screenname page
"""
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Length
from flask_wtf import FlaskForm

class ChangeForm(FlaskForm):  # pylint:disable=R0903
    """
    User chooses a new screenname.
    """
    change = TextAreaField(label="New screenname:",
                       validators=[Length(min=1)])