from flask import Flask

myApp = Flask(__name__)

@myApp.route("/")
def home():
 name = "Lisa"
 city_names = ["Paris", "London", "Rome", "Tahiti"] 
 html = '''
 <html>
  <head>
   <title> Home Page </title>
  </head>
  <body>
  <h1> Welcome ''' + name + '''!</h1>
  <p> <a href="www.google.com"> not google </a> </p>
 
  <ul>
  
  </ul> 
 </body>
</html>
  '''
 for city in city_names:
  html += '''<li> '''+city+''' </li>'''
 return html

#myApp.run()
