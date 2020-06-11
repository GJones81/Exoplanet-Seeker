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
import requests

# My module made for organizing my app
import graph_engine as graph

app = Flask(__name__)
app.config['DEBUG'] = True

# This function gets the data from the NASA API
def get_data():
    data = requests.get(
        'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=&order=dec&format=json'
    )
    global json_data
    json_data = json.loads(data.text)
    return json_data

# This function takes the json object and converts it to a pandas data frame
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
    return render_template('data.html', sent_data = data)

# On GET method shows a form where the user enters the type of graph, x axis values, and y axis values
# On POST method takes those submitted values and calls the functions in 
# graph_engine.py to plot and returns the desired graph
@app.route('/visual', methods=['GET', 'POST'])
def data_vis():
    if request.method == 'POST':
        data_frame = create_dataframe(json_data)
        graph_type = request.form['graph_type']
        # print(data_frame)

        # This block creates Line graphs
        if graph_type == 'line':

            # If there is no value input for the y axis, create only the x axis array
            if request.form['y_value'] == 'None':
                x_value = request.form['x_value']
                x_values_array = np.array(data_frame[x_value])
                y_values_array = 'Empty'
  
            # Create both x and y axes arrays if there is input for the y axis
            else:
                x_value = request.form['x_value']
                x_values_array = np.array(data_frame[x_value])
                y_value = request.form['y_value']
                y_values_array = np.array(data_frame[y_value])
                
            return render_template('visual.html', image = graph.plot(x_values_array, y_values_array))

        # This block creates Histogram graphs
        elif graph_type == 'hist':
            x_value = request.form['x_value']
            x_values_array = np.array(data_frame[x_value])
            bins = 8
            return render_template('visual.html', image = graph.histgram(x_values_array, bins))

        # This block creates Bar graphs
        elif graph_type == 'bar':
            x_value = request.form['x_value']
            x_values_array = np.array(data_frame[x_value])
            y_value = [x for x in range(len(x_values_array))]
            return render_template('visual.html', image = graph.bar(x_values_array, y_value))

        # This block creates Scatter graphs    
        else:
            x_value = request.form['x_value']
            x_values_array = np.array(data_frame[x_value])
            y_value = request.form['y_value']
            y_values_array = np.array(data_frame[y_value])
        return render_template('visual.html', image = graph.scatter(x_values_array, y_values_array))
    # This line is the GET method response, renders the form for submitting values to be graphed
    else:
        return render_template('visual.html')

if __name__ == '__main__':
    app.run()