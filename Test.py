# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:03:47 2020

@author: SupriyaMalakar
"""


import io
import random
import numpy as np
from flask import Response,Flask,request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import logging
import json

app = Flask(__name__)
heightdata=[]
barsdata=()

@app.route('/plot.png')
def plot_png():
    
    #requestdata=request.args.get('data')
    requestdata='{"type":"bar","labels":["AVAILIBILITY","PERFORMANCE","QUALITY","OEE"],"height":[50,89,90,100]}'
    Data_dict = json.loads(requestdata)
    heightdata=Data_dict['height']
    barsdata=Data_dict['labels']

    log = logging.getLogger("my-logger")
    log.info(f"hello {Data_dict}")
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    fig = plt.figure()
    print(heightdata)
   
    height =heightdata
    bars = tuple(barsdata)
    y_pos = np.arange(len(bars))
    plt.title('OEE Gauge')
     
    # Create bars
    plt.bar(y_pos, height)
     
    # Create names on the x-axis
    plt.xticks(y_pos, bars)
    #plt.show()
    
    return fig

if __name__=='__main__':
    app.run(debug=True)