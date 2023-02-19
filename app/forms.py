from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField

class ContactForm(FlaskForm):
    name = StringField()
    email = EmailField()
    subject = StringField()
    textArea = TextAreaField()