from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

'''def validate_url(form, field):
    if len(field.data) < 20:
        raise ValidationError('The URL is already short!!')'''

class UrlForm(FlaskForm):
    Original_URL = StringField('Original URL', validators=[DataRequired(), Length(min=20)])   
    Word = StringField('Customize your URL', validators=[DataRequired()])
    Submit = SubmitField('Generate Link')

class OutForm(FlaskForm):
	Original = StringField('From:', render_kw={'readonly': True}) 
	New =  StringField('To:', render_kw={'readonly': True}) 