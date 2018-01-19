import os
import httplib
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add", methods=['POST'])
def add():
    #
    # from POST parameters
    #
    x = int(request.form['x'])
    y = int(request.form['y'])
    #
    # from Kubernetes Service(environment variables)
    #
    my_calc_host = os.environ['MY_CALC_SERVICE_SERVICE_HOST']
    my_calc_port = os.environ['MY_CALC_SERVICE_SERVICE_PORT']
    #
    # REST call to MicroService(my-calc)
    #
    client = httplib.HTTPConnection(my_calc_host, my_calc_port)
    client.request("GET", "/addition/%d/%d" % (x, y))
    response = client.getresponse()
    result = response.read()
    return render_template('index.html', add_x=x, add_y=y,
add_result=result)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
