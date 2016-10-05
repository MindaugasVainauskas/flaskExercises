from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Now press back button to go back!"
	
@app.route("/name/<username>")#route command gets /name/<insert whatever name here>
def name(username):
    return ("Your name is %s" % username)#return function returns premade text with the name added to the end.


#Managed to get the templates routing working thanks to: http://flask.pocoo.org/docs/0.11/quickstart/#routing
@app.route("/templates/")
@app.route("/templates/<name>")#route command gets /name/<insert whatever name here>
def user(name):
    return render_template("index.html", name = name)#return function returns premade text with the name added to the end.


if __name__ == "__main__":
    app.run(debug=True)