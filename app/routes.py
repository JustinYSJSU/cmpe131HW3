from app import myApp
from app.enter import CityNameForm
from flask import render_template, flash


name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myApp.route("/", methods = ['GET', 'POST'])
def home():
  form = CityNameForm()
  
  if form.validate_on_submit():
   flash(f'{form.city_name.data}')
  return render_template('home.html', name = name, city_names = city_names,
   form = form)
