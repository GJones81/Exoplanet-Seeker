from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import io
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# This file contains the functions which generate the graphs. It is imported over in index.py
# as graph.

# Returns the Line Graph
def plot(x, y, x_label, y_label='y - axis'):
    fig = Figure(figsize=(8, 8))
    canvas = FigureCanvas(fig)
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('Line Graph')
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    axis.grid()
    if y == 'Empty':
        axis.plot(x, 'b')
    else:
        axis.plot(x, y, 'r')
    
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = 'data:image/png; base64,'
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    image = pngImageB64String
    return image

# Returns the Histogram Graph
def histgram(values, bins, x_label):
    fig = Figure(figsize=(8, 8))
    canvas = FigureCanvas(fig)
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('Histogram Graph')
    axis.set_xlabel(x_label)
    axis.set_ylabel('y axis')
    axis.grid()
    axis.hist(values, bins)

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = 'data:image/png; base64,'
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    image = pngImageB64String
    return image

# Returns the Bar Graph
def bar(values, indices, x_label):
    fig = Figure(figsize=(8, 8))
    canvas = FigureCanvas(fig)
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('Bar Graph')
    axis.set_xlabel(x_label)
    axis.set_ylabel('y axis')
    axis.grid()
    axis.bar(indices, values)

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = 'data:image/png; base64,'
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    image = pngImageB64String
    return image

# Returns the Scatter Plot Graph
def scatter(x, y, x_label, y_label):
    fig = Figure(figsize=(8, 8))
    canvas = FigureCanvas(fig)
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('Scatter Plot Graph')
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    axis.grid()
    axis.scatter(x, y)

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = 'data:image/png; base64,'
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    image = pngImageB64String
    return image