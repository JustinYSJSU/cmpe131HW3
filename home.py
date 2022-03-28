
from flask import Flask

myApp = Flask(__name__)

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myApp.route("/")
def home():
 html = '''
 <html>
  <head>
   <title> Home Page </title>
  </head>
  <body>
  <h1> Welcome ''' + name + '''!</h1>
  <p> <a href="www.google.com"> not google </a> </p> 
 </body>
  
</html>
  '''
 for city in city_names:
  html += '''<ul> <li> '''+city+''' </li> </ul>'''
 return html

#myApp.run()
