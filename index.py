from flask import Flask, jsonify, render_template, request, Response 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import io
import json
import numpy as np
import pandas as pd
import requests

# My module
# graphing functions placed elsewhere to keep things orderly
import graph_engine as graph

app = Flask(__name__)
app.config['DEBUG'] = True

# This function gets the data from the NASA API
def get_data():
    data = requests.get(
        'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_hostname,pl_pnum,st_optmag,st_teff,st_dist,pl_name,pl_discmethod,pl_orbper,pl_dens,pl_radj&order=dec&format=json'
    )
    global json_data
    json_data = json.loads(data.text)
    return json_data

# This function takes the json object and converts it to a pandas data frame
def create_dataframe(data):
    global data_frame
    data_frame = pd.DataFrame(data = data).sort_values('pl_hostname')
    return data_frame

# This function creates the labels for the axes
def create_label(value):
    labels = {
        'pl_pnum': 'Num of Planets in System',
        'pl_orbper': 'Orbital Period',
        'pl_dens': 'Planet Density',
        'pl_radj': 'Radius compared to Jupiter',
        'st_optmag': 'Optical Magnitude of the Star',
        'st_teff': 'Estimated Temp of the Star',
        'st_dist': 'Distance to the Star'
    }
    return labels[value]

# Renders the Home page
@app.route('/')
def index():
    return render_template('home.html')

# Calls the function get_data for a fresh subset of the database table, renders it to /data
@app.route('/data')
def send_data():
    data = get_data()
    return render_template('data.html', sent_data = data)

# On GET method shows a form where the user enters the type of graph, x axis values, and y axis values
# On POST method takes those submitted values and calls the functions in 
# graph_engine.py to plot and return the desired graph
@app.route('/visual', methods=['GET', 'POST'])
def data_vis():
    if request.method == 'POST':
        data_frame = create_dataframe(json_data)
        graph_type = request.form['graph_type']
        # print(data_frame)

        # This block shapes data for Histogram graphs
        if graph_type == 'hist':
            x_value = request.form['x_value']
            x_label = create_label(x_value)
            x_values_array = np.array(data_frame[x_value])
            bins = int(request.form['bins'])

            return render_template('visual.html', image = graph.histgram(x_values_array, bins, x_label))

        # This block shapes data Bar graphs
        elif graph_type == 'bar':
            x_value = request.form['x_value']
            y_label = create_label(x_value)
            x_values_array = np.array(data_frame[x_value])
            indices = [x for x in range(len(x_values_array))]

            return render_template('visual.html', image = graph.bar(x_values_array, indices, y_label))

        # This block shapes data for Scatter graphs    
        else:
            x_value = request.form['x_value']
            x_label = create_label(x_value)
            x_values_array = np.array(data_frame[x_value])
            y_value = request.form['y_value']
            y_label = create_label(y_value)
            y_values_array = np.array(data_frame[y_value])

        return render_template('visual.html', image = graph.scatter(x_values_array, y_values_array, x_label, y_label))
    # This line is the GET method response, renders the form for submitting values to be graphed
    else:
        return render_template('visual.html')

if __name__ == '__main__':
    app.run()