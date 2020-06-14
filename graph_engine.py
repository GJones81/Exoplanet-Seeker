from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
import io
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# This file contains the functions which generate the graphs. It is imported over in index.py
# as graph.

# Returns the Histogram Graph
def histgram(values, bins, x_label):
    fig = Figure(figsize=(8, 8))
    canvas = FigureCanvas(fig)
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('Histogram Graph')
    axis.set_xlabel(x_label)
    axis.set_ylabel('y axis')
    axis.grid()
    axis.hist(values, bins, histtype = 'bar', rwidth = 0.5)

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = 'data:image/png; base64,'
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    image = pngImageB64String
    return image

# Returns the Bar Graph
def bar(values, indices, y_label):
    fig = Figure(figsize=(8, 8))
    canvas = FigureCanvas(fig)
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title('Bar Graph')
    axis.set_xlabel('x axis')
    axis.set_ylabel(y_label)
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
    s = 10
    axis.grid()
    axis.scatter(x, y, s)

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = 'data:image/png; base64,'
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    image = pngImageB64String
    return image