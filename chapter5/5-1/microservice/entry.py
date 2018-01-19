from flask import Flask, request 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

@app.route("/power/<int:base>/<int:index>")
def power(base, index): 
    return "%d" % (base ** index)

@app.route("/addition/<int:x>/<int:y>")
def add(x, y):
    return "%d" % (x+y)

@app.route("/substraction/<int:x>/<int:y>")
def substract(x, y):
    return "%d" % (x-y)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
