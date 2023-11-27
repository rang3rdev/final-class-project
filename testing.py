import csv 
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

player_colors = {
    'Gavin': '#E50184', 
    'Tyler': '#FFBA00',  
    'Arnold': '#D80030', 
    'Bryan': '#F65900',  
    'Adam': '#3461EF',  
    'Mujeeb': '#00D5A0'  
}

gavin = 'points/gavin.txt'
bryan = 'points/bryan.txt'
adam = 'points/adam.txt'
mujeeb = 'points/mujeeb.txt'
tyler = 'points/tyler.txt'
arnold = 'points/arnold.txt'

Wgavin = 'win-percentage/gavin-win.txt'
Wbryan = 'win-percentage/bryan-win.txt'
Wadam = 'win-percentage/adam-win.txt'
Wmujeeb = 'win-percentage/mujeeb-win.txt'
Wtyler = 'win-percentage/tyler-win.txt'
Warnold = 'win-percentage/arnold-win.txt'

def read_data(file_path):
    x, y = [], []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                x.append(float(row[0]))
                y.append(float(row[1]))
            else:
                print(f"Warning: Skipping row {row} in file {file_path}. It does not have the expected number of elements.")
    return x, y

x1, y1 = read_data(gavin)
x2, y2 = read_data(bryan)
x3, y3 = read_data(adam)
x4, y4 = read_data(mujeeb)
x5, y5 = read_data(tyler)
x6, y6 = read_data(arnold)

x7, y7 = read_data(Wgavin)
x8, y8 = read_data(Wbryan)
x9, y9 = read_data(Wadam)
x10, y10 = read_data(Wmujeeb)
x11, y11 = read_data(Wtyler)
x12, y12 = read_data(Warnold)

simple_x = np.arange(1, 11)

stack_plot_fig = go.Figure()

stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y1, fill='tozeroy', mode='none', name='Gavin', fillcolor=player_colors['Gavin'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y2, fill='tozeroy', mode='none', name='Bryan', fillcolor=player_colors['Bryan'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y3, fill='tozeroy', mode='none', name='Adam', fillcolor=player_colors['Adam'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y4, fill='tozeroy', mode='none', name='Mujeeb', fillcolor=player_colors['Mujeeb'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y5, fill='tozeroy', mode='none', name='Tyler', fillcolor=player_colors['Tyler'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y6, fill='tozeroy', mode='none', name='Arnold', fillcolor=player_colors['Arnold'], line=dict(color='rgba(255,255,255,0)')))

above_below_avg_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    above_below_avg_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    above_below_avg_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, marker=dict(size=10, color=player_colors[name])), row=2, col=1)

overall_trendline_y = [(sum(week) / len(week)) for week in zip(y1, y2, y3, y4, y5, y6)]

above_below_avg_fig.add_trace(go.Scatter(x=x1, y=overall_trendline_y, mode='lines', name='Overall Trendline', line=dict(color='black', dash='dash')), row=1, col=1)
above_below_avg_fig.add_trace(go.Scatter(x=x1, y=overall_trendline_y, mode='lines', name='Overall Trendline', line=dict(color='black', dash='dash')), row=2, col=1)

specific_fig = go.Figure()

overall_below_trendline_count = 0
overall_above_trendline_count = 0

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    markers_below_trendline = [val for val, trendline_val in zip(y, overall_trendline_y) if val < trendline_val]
    markers_above_trendline = [val for val, trendline_val in zip(y, overall_trendline_y) if val >= trendline_val]

    below_trendline_count = len(markers_below_trendline)
    above_trendline_count = len(markers_above_trendline)

    overall_below_trendline_count += below_trendline_count
    overall_above_trendline_count += above_trendline_count

    print(f'For {name}:')
    print(f'Number of points below trendline: {below_trendline_count}')
    print(f'Number of points above trendline: {above_trendline_count}')

    specific_fig.add_trace(go.Scatter(x=x, y=markers_below_trendline, mode='markers', name=name + ' Below Trendline', marker=dict(size=10, color='red')))
    specific_fig.add_trace(go.Scatter(x=x, y=markers_above_trendline, mode='markers', name=name + ' Above Trendline', marker=dict(size=10, color='green')))

print(f'\nOverall counts:')
print(f'Number of points below trendline: {overall_below_trendline_count}')
print(f'Number of points above trendline: {overall_above_trendline_count}')

scatter_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, line=dict(color=player_colors[name])), row=2, col=1)

winPercent_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

for i, (x, y, name) in enumerate([(x7, y7, 'Gavin'), (x8, y8, 'Bryan'), (x9, y9, 'Adam'), (x10, y10, 'Mujeeb'), (x11, y11, 'Tyler'), (x12, y12, 'Arnold')], start=1):
    winPercent_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x7, y7, 'Gavin'), (x8, y8, 'Bryan'), (x9, y9, 'Adam'), (x10, y10, 'Mujeeb'), (x11, y11, 'Tyler'), (x12, y12, 'Arnold')], start=1):
    winPercent_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, marker=dict(size=10, color=player_colors[name])), row=2, col=1)

pie_fig = go.Figure()

pie_fig.add_trace(go.Pie(labels=['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
                        values=[sum(y1), sum(y2), sum(y3), sum(y4), sum(y5), sum(y6)],
                        name='Total Points', marker=dict(colors=[player_colors['Gavin'], player_colors['Bryan'], player_colors['Adam'], player_colors['Mujeeb'], player_colors['Tyler'], player_colors['Arnold']])))

scatter_fig.update_layout(
    title_text='Fantasy Football Scoring: Weeks 1-10',
    showlegend=True,
    width=1000,
    height=800,
)

winPercent_fig.update_layout(
    title_text='Fantasy Football Win Percentages: Weeks 1-10',
    showlegend=True,
    width=800,
    height=600,
)

above_below_avg_fig.update_layout(
    title_text='Fantasy Football Points: Above/Below Weekly Average',
    showlegend=True,
    width=1000,
    height=800,
)

specific_fig.update_layout(
    title_text='Fantasy Football Points: Above/Below Weekly Average',
    showlegend=True,
    width=1000,
    height=800,
)

stack_plot_fig.update_layout(
    title_text='Stack Plot',
    xaxis_title='X-axis Label',
    yaxis_title='Y-axis Label',
    showlegend=True,
    plot_bgcolor='rgba(255,255,255,0.9)',
    paper_bgcolor='rgba(255,255,255,0.9)',
    width=800,
    height=600,
)

scatter_html = scatter_fig.to_html(full_html=False)
pie_html = pie_fig.to_html(full_html=False)
winPercent_html = winPercent_fig.to_html(full_html=False)
above_below_avg_html = above_below_avg_fig.to_html(full_html=False)
stack_plot_html = stack_plot_fig.to_html (full_html=False)
specific_html = specific_fig.to_html (full_html=False)

data_1 = {
    'Player': ['Adam', 'Gavin', 'Bryan', 'Arnold', 'Mujeeb', 'Tyler'],
    'Below Trendline': [4, 4, 2, 7, 8, 4],
    'Above Trendline': [6, 6, 8, 3, 2, 6],
}

df_table_1 = pd.DataFrame(data_1)
df_table_1['Total Points'] = df_table_1['Below Trendline'] + df_table_1['Above Trendline']

table_1_html = df_table_1.to_html(index=False)

data_2 = {
    'Player': ['Adam', 'Gavin', 'Bryan', 'Arnold', 'Mujeeb', 'Tyler'],
    'Total Points': [sum(y3), sum(y1), sum(y2), sum(y4), sum(y6), sum(y5)]
}

df_table_2 = pd.DataFrame(data_2)

table_2_html = df_table_2.to_html(index=False)

intro_text = """
    <p>Fantasy Football is a popular game wherein a group of around 6-12 participants take on the role of a football general manager, 
    building their own teams of professional football players to compete in head-to-head matchups for the duration of 14-18 weeks, 
    with scoring based on the statistical performances of one's players in real-time games.</p>
    <p>The first 14 weeks are considered as the regular season. The postseason, commonly referred to as the playoffs, 
    occurs during weeks 15-18 and requires a certain threshold of wins to qualify.</p>
    <p>This is my first year playing fantasy football, having been invited to play in a modest 6-man league between a close group of friends. 
    Considering how fundamental statistics and the analysis of data are to the playing of fantasy football, 
    it only made sense for myself to take on the task of visualizing the various data I've collected over these past few months, 
    both to analyze trends within the league as well as for my own personal enjoyment.</p>
"""

explanations = """
    <p>In this graph, I displayed the change in point totals over the span of 10 weeks with the x-axis, 
    and visualized the additional points added towards the player's point total that week using the y-axis.</p>
"""

commentaries1 = """
    <p> The first thing you may notice is the volatility that many players display in their weekly point scorings. 
    Peculiarities such as Mujeeb's measly debut of 61.58 to an explosive showing of 151.38 points just the next week
    seem to imply high variance to player scoring outcomes week by week. 
    As we are dealing with statistics, however, there is always to be expected outliers who stray away from the general trend. 
    Adam has proved himself to be a remarkably consistent performer, reliably occupying a top 1 to 2 showing weekly, so it should come to no surprise
    Adam comes out with the highest overall point total of weeks 1-10, clocking in with an impressive 1529.44 points accrued.</p> 
"""

commentaries2 = """
    <p> The first thing that stood out to me in this graph was Tyler's falloff exiting the beggining weeks, 
    going on a 6 week losing streak that would briefly drag him all the way down to a 17% win rate, the lowest anyone has gone thus far. 
    Similarly, even despite consistently strong weekly outings, Adam suffered an initial 4 week slump that brought his 
    win rate as low as 25%, although experienced a rebound beggining in week 5. Bryan is the most volatile figure in the data, 
    frequently teasing a losing record, only to spike up once he comes close to an under 50% win rate.
"""

tips = """
<p> To hide a variable, such as Gavin, click on the dots/lines next to names in the legend. This makes it so you can compare and contrast different players, 
as well as look exclusively at the data of one certain player. You can unhide a variable by simply reclicking the aforementioned dots/lines.
"""

html_report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Fantasy Football Report</title>
    <link rel="stylesheet" href="fantasy.css">
</head>
<body>
    <header>
    <h1 style="text-align: center;">The Fantasy Football Report</h1>
    <h5 style="text-align: center;">By: Gavin Schnowske</h5>
    </header>
    <h2>What is Fantasy Football?</h2>
    <div class="comm">
        {intro_text}
    </div>

    <!-- Points Total Scatter Plot Section -->
        <h2>Change in Point Totals: Weeks 1-10</h2>
    <div class="comm">
        {explanations}
    </div>
    <div style="width: 100%; margin: 20px 20px 20px 20px;">
        {scatter_html} <aside>{tips}</aside>
    </div>
    <div class="comm">
        {commentaries1}
    </div>

    <!-- Win Rate Scatter Plot Section -->
        <h2>Change in Win Rate: Weeks 1-10</h2>
    <div style="width: 100%; margin: 20px 20px 20px 20px;">
        {winPercent_html}
    </div>
    <div class="comm">
        {commentaries2}
    </div>

    <!-- Pie Chart Section -->
        <h2>Pie Chart</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {pie_html}
    </div>
    <div class="comm">
        {explanations}
    </div>

    <!-- Pie Chart Section -->
        <h2>Stack Plot</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {stack_plot_html}
    </div>
    <div class="comm">
        {explanations}
    </div>

    <!-- Averages Scatter Plot Section -->
        <h2>Averages: Weeks 1-10</h2>
    <div style="width: 100%; margin: 20px 20px 20px 20px;">
        {above_below_avg_html}
        {specific_html}
    </div>
    <div class="comm">
        {commentaries1}
    </div>

    <!-- Player Stats Table -->
        <h2>Player Stats</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {table_2_html}
        {table_1_html}
    </div>
    <div class="comm">
        {commentaries1}
    </div>
</body>
</html>
"""

with open('index.html', 'w') as report_file:
    report_file.write(html_report)