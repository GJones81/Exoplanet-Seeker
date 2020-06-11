from flask import Flask, jsonify, render_template, request, Response 
from pygal import Config
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import io
import json
import numpy as np
import pandas as pd
import pygal
import random
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

# Global variables to take user inputs and be entered into plotting functions

x_values = []
y_values = []

def pull_x_values(x):
    for planet in json_data:
        if type(planet[x]) == int:
            x_values.append(planet[x])
    return x_values

def pull_y_values(y):
    for planet in json_data:
        if type(planet[y]) == int:
            y_values.append(planet[y])
    return y_values

def get_data():
    data = requests.get(
        'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=&order=dec&format=json'
    )
    global json_data
    json_data = json.loads(data.text)
    return json_data

def create_dataframe(data):
    global data_frame
    data_frame = pd.DataFrame(data = data)
    return data_frame

# Renders the Home page
@app.route('/')
def index():
    return render_template('home.html')

# Calls the function get_data for a fresh subset of the database table, renders it to /data
@app.route('/data')
def send_data():
    data = get_data()
    # data = requests.get(
    #     'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=&order=dec&format=json'
    # )
    # json_data = json.loads(data.text)
    # # This is the point at which the data needs to be converted into a 
    # # dataframe via Pandas, then into a Numpy array, then to a list
    return render_template('data.html', sent_data = data)

# On GET method shows a form where the user enters x axis values and y axis values
# On POST method takes those submitted values and inputs them into the matplotlib code to plot the graph
@app.route('/visual', methods=['GET', 'POST'])
def data_vis():
    if request.method == 'POST':
        data_frame = create_dataframe(json_data)
        # print(data_frame)
        x_value = request.form['x_value']
        # y_value = request.form['y_value']
        # print(x_value)
        x_values_array = np.array(data_frame[x_value])
        # y_values_array = np.array(data_frame[y_value])
        # print(x_values_array)
        # print(data_frame[x_value])
        
    # Builds a graph, converts it to a png formatted file, then 64 byte strings, stores them
    # in 'image' and sends it to the client
        fig = Figure(figsize=(6, 6))
        canvas = FigureCanvas(fig)
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title('My Graph')
        axis.set_xlabel('x - axis')
        axis.set_ylabel('y - axis')
        axis.grid()
        axis.plot(x_values_array, 'r')

        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)

        pngImageB64String = 'data:image/png; base64,'
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

        return render_template('visual.html', image=pngImageB64String)
    # Uses the pygal library
        # bar_chart = pygal.Bar()
        # bar_chart.add('Graph', x_values_array)
        # return bar_chart.render()
    else:
        return render_template('visual.html')

if __name__ == '__main__':
    app.run()