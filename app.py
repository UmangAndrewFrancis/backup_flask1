import gzip, functools
from io import BytesIO as IO
from flask import after_this_request, request
from flask import Flask, render_template
import logging
import sys
logging.basicConfig(filename="newfile.log", level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def hello():
    logging.debug("Harmless debug Message") 
    logging.info("Just an information") 
    logging.warning("Its a Warning") 
    logging.error("Did you try to divide by zero") 
    logging.critical("Internet is down") 
    return render_template('home.html')

@app.route('/post', methods = ["POST"])
def post():
    print(request.data)
    print(request.headers)
    return 'Received\n' + str(request.data) + "\n" + str(request.headers)

@app.route("/test1")
def test1():
    logging.debug("Harmless debug Message") 
    # import osmnx
    print("abc")
    return "successful"

if __name__ == "__main__":
    app.debug = True
    app.run()