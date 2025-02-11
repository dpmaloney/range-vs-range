"""
Form for change of screenname page
"""
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Length
from flask_wtf import FlaskForm
from rvr.db.tables import MAX_CHAT

class ChatForm(FlaskForm):  # pylint:disable=R0924,R0903
    """
    User enters a chat message
    """
    message = TextAreaField(label="Chat:", validators=[Length(min=1, max=MAX_CHAT)])