from django.shortcuts import render
from visualization.models import Vis
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from datetime import datetime
 
def graph(request):
    qs = Vis.objects.all()
    graph_data = [
        {
            'Heart_Beat': x.heart_beat,
            'Time': x.time
        } for x in qs
    ]

    df = pd.DataFrame(graph_data)
    fig = px.timeline(df, x_start="Time", x_end="Time", y="Heart_Beat")

    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context={'plot_div':gantt_plot}
    return render(request, 'index.html',context=graph_data)
