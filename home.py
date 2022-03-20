from flask import Flask

myApp = Flask(__name__)

@myApp.route("/")
def home():
 name = "Lisa"
 city_names = ["Paris", "London", "Rome", "Tahiti"] 
 
 return '''
 <html>
  <head>
   <title> Home Page </title>
  </head>
  <body>
  <h1> Welcome ''' + name + '''!</h1>
  <p> <a href="www.google.com"> not google </a> </p>
 
  <ul>
    <li> '''+city_names[0]+'''</li>
    <li> '''+city_names[1]+'''</li>
    <li> '''+city_names[2]+'''</li>
    <li> '''+city_names[3]+'''</li>
  </ul>
 </body>
</html>
  '''


myApp.run()
