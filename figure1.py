

import pprint
import json
import sys

import plotly.utils
import plotly.graph_objects as go

def make_fig():

    trace1 = go.Scatter(x=[256,256,440,440], y=[256,440,256,440], mode='markers')
    traces=[trace1]

    xaxis = go.layout.XAxis(range=[128,512])
    yaxis = go.layout.YAxis(range=[128,512])

    layout= go.Layout(width=500, height=500, xaxis=xaxis, yaxis=yaxis)

    fig = go.Figure(data=traces, layout=layout)
    pprint.pprint(fig)
    fig_json=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return fig, fig_json

if __name__=="__main__":
    output_html_file=sys.argv[1]
    fig, fig_json=make_fig()
    fig.write_html(output_html_file)
    
