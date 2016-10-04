from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/name/<username>")#route command gets /name/<insert whatever name here>
def name(username):
    return ("Your name is %s" % username)#return function returns premade text with the name added to the end.

if __name__ == "__main__":
    app.run()