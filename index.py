from flask import Flask, render_template, request, jsonify
import requests
import json
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def get_data():
    data = requests.get(
        'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=&order=dec&format=json'
    )
    return render_template('data.html', data = {data})

if __name__ == '__main__':
    app.run()