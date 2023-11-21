import csv
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

gavin = 'gavin.txt'
bryan = 'bryan.txt'
adam = 'adam.txt'
mujeeb = 'mujeeb.txt'
tyler = 'tyler.txt'
arnold = 'arnold.txt'

def read_data(file_path):
    x, y = [], []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x, y

x1, y1 = read_data(gavin)
x2, y2 = read_data(bryan)
x3, y3 = read_data(adam)
x4, y4 = read_data(mujeeb)
x5, y5 = read_data(tyler)
x6, y6 = read_data(arnold)

scatter_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

scatter_fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers', name='Gavin'), row=1, col=1)
scatter_fig.add_trace(go.Scatter(x=x2, y=y2, mode='markers', name='Bryan'), row=1, col=1)
scatter_fig.add_trace(go.Scatter(x=x3, y=y3, mode='markers', name='Adam'), row=1, col=1)
scatter_fig.add_trace(go.Scatter(x=x4, y=y4, mode='markers', name='Mujeeb'), row=1, col=1)
scatter_fig.add_trace(go.Scatter(x=x5, y=y5, mode='markers', name='Tyler'), row=1, col=1)
scatter_fig.add_trace(go.Scatter(x=x6, y=y6, mode='markers', name='Arnold'), row=1, col=1)

scatter_fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='Gavin'), row=2, col=1)
scatter_fig.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='Bryan'), row=2, col=1)
scatter_fig.add_trace(go.Scatter(x=x3, y=y3, mode='lines', name='Adam'), row=2, col=1)
scatter_fig.add_trace(go.Scatter(x=x4, y=y4, mode='lines', name='Mujeeb'), row=2, col=1)
scatter_fig.add_trace(go.Scatter(x=x5, y=y5, mode='lines', name='Tyler'), row=2, col=1)
scatter_fig.add_trace(go.Scatter(x=x6, y=y6, mode='lines', name='Arnold'), row=2, col=1)

pie_fig = go.Figure()

pie_fig.add_trace(go.Pie(labels=['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
                        values=[sum(y1), sum(y2), sum(y3), sum(y4), sum(y5), sum(y6)],
                        name='Total Points'))

scatter_fig.update_layout(
    title_text='Fantasy Football Scoring: Weeks 1-10',
    showlegend=True
)

scatter_html = scatter_fig.to_html(full_html=False)
pie_html = pie_fig.to_html(full_html=False)

data = {'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
        'Total Points': [sum(y1), sum(y2), sum(y3), sum(y4), sum(y5), sum(y6)]}
df = pd.DataFrame(data)

table_html = df.to_html(index=False)

html_report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fantasy Football Report</title>
</head>
<body>
    <h1>Fantasy Football Report</h1>

    <!-- Scatter Plot Section -->
    <div id="scatter-plot-section">
        <h2>Scatter Plot</h2>
        {scatter_html}
    </div>

    <!-- Pie Chart Section -->
    <div id="pie-chart-section">
        <h2>Pie Chart</h2>
        {pie_html}
    </div>

    <!-- Player Stats Table -->
    <div id="player-stats-section">
        <h2>Player Stats</h2>
        {table_html}
    </div>
</body>
</html>
"""

with open('fantasy_football_report.html', 'w') as report_file:
    report_file.write(html_report)