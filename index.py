from flask import Flask, render_template, request, Response, jsonify
from pygal import Config
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import io
import json
import numpy as np
import pygal
import random
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

# Global variables to take user inputs and be entering into plotting functions
json_data = ''
x_values = []
y_values = []

def pull_x_values(x):
    for planet in json_data:
        test = isinstance(planet[x], int)
        if test == True:
            x_values.append(planet[x])
    return x_values

def pull_y_values(y):
    for planet in json_data:
        y_values.append(planet[y])
    return y_values

# Renders the Home page
@app.route('/')
def index():
    return render_template('home.html')

# Calls the NASA API for a fresh subset of the database table, renders it to /data
@app.route('/data')
def get_data():
    data = requests.get(
        'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=&order=dec&format=json'
    )
    json_data = json.loads(data.text)
    return render_template('data.html', sent_data = json_data)

@app.route('/visual', methods=['GET', 'POST'])
def data_vis():
    if request.method == 'POST':
        x_values = request.form['x_value']
        print(x_values)
        pull_x_values(x_values)
    # Builds a graph, converts it to a png formatted file, then 64 byte strings, stores them
    # in 'image' and sends it to the client
        # fig = Figure()
        # canvas = FigureCanvas(fig)
        # axis = fig.add_subplot(1, 1, 1)
        # axis.set_title('My Graph')
        # axis.set_xlabel('x - axis')
        # axis.set_ylabel('y - axis')
        # axis.grid()
        # axis.plot([1, 2, 3, 4, 5], [2, 4, 8, 16, 32], 'ro-')

        # pngImage = io.BytesIO()
        # FigureCanvas(fig).print_png(pngImage)

        # pngImageB64String = 'data:image/png; base64,'
        # pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

        # return render_template('visual.html', image=pngImageB64String)
    # Uses the pygal library
        bar_chart = pygal.Bar()
        bar_chart.add('Fibonacci', x_values)
        return bar_chart.render()
    else:
        return render_template('visual.html')

if __name__ == '__main__':
    app.run()