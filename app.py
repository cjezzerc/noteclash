from flask import Flask, render_template
# import plotly.utils
# import plotly.graph_objects as go
# import pprint
import time
import figure1

app=Flask(__name__)

@app.route('/')
def testfunc():

    
    # fig = go.Figure(data=go.Scatter(x=[1,2,3], y=[1,4,9], mode='markers'))
    # pprint.pprint(fig)
    # fig_json=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    fig_json=figure1.make_fig()

    return render_template('first_template.html', time=time.time(), graphJSON=fig_json)

