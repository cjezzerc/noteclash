
import plotly.utils
import plotly.graph_objects as go
import pprint
import json

def make_fig():

    fig = go.Figure(data=go.Scatter(x=[1,2,3], y=[1,4,9], mode='markers'))
    pprint.pprint(fig)
    fig_json=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return fig_json

if __name__=="__main__":
    output_html_file=sys.argv[1]
    make_fig().write_html(output_html_file)
