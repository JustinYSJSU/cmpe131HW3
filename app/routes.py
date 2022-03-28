from app import myApp
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CityNameForm(FlaskForm):
 city_name = StringField('City Name', validators = [DataRequired()])
 submit = SubmitField('Submit')


name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myApp.route("/", methods = ['GET', 'POST'])
def home():
  form = CityNameForm()
  
  if form.validate_on_submit():
   flash(f'{form.city_name.data}')
  return render_template('home.html', name = name, city_names = city_names,
   form = form)
