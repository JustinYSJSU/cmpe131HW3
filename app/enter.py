from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CityNameForm(FlaskForm):
 city_name = StringField('City Name', validators = [DataRequired()])
 submit = SubmitField('Submit')
