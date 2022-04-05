from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


class  UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])