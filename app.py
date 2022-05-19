
import time

from flask import Flask, render_template

import figure1

app=Flask(__name__)

@app.route('/')
def testfunc():

    fig, fig_json=figure1.make_fig()

    return render_template('first_template.html', 
                            time=time.time(), 
                            graphJSON=fig_json)
