#Testing out Flask functionality
#To run this code from bash, type: flask --app hello run
#This code will use your machine as a server to print "Hello, World!"
#Press ctrl + C to quit hosting

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! </p>"

