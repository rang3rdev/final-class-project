# The Fantasy Football Report
# By: Gavin Schnowske

import csv 
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

### Data Reading

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

w_gavin = 'win-percentage/gavin-win.txt'
w_bryan = 'win-percentage/bryan-win.txt'
w_adam = 'win-percentage/adam-win.txt'
w_mujeeb = 'win-percentage/mujeeb-win.txt'
w_tyler = 'win-percentage/tyler-win.txt'
w_arnold = 'win-percentage/arnold-win.txt'

p_gavin = 'projections/gavin-proj.txt'
p_bryan = 'projections/bryan-proj.txt'
p_adam = 'projections/adam-proj.txt'
p_mujeeb = 'projections/mujeeb-proj.txt'
p_tyler = 'projections/tyler-proj.txt'
p_arnold = 'projections/arnold-proj.txt'

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

def read_y_values(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split(', ') for line in file.readlines()]
        y_values = [float(row[1]) for row in data]
    return y_values

x1, y1 = read_data(gavin)
x2, y2 = read_data(bryan)
x3, y3 = read_data(adam)
x4, y4 = read_data(mujeeb)
x5, y5 = read_data(tyler)
x6, y6 = read_data(arnold)

x7, y7 = read_data(w_gavin)
x8, y8 = read_data(w_bryan)
x9, y9 = read_data(w_adam)
x10, y10 = read_data(w_mujeeb)
x11, y11 = read_data(w_tyler)
x12, y12 = read_data(w_arnold)

x13, y13 = read_data(p_gavin)
x14, y14 = read_data(p_bryan)
x15, y15 = read_data(p_adam)
x16, y16 = read_data(p_mujeeb)
x17, y17 = read_data(p_tyler)
x18, y18 = read_data(p_arnold)

def calculate_changes(y_values):
    return [round(y_values[i] - y_values[i - 1], 2) if i > 0 else 0 for i in range(len(y_values))]

changes_gavin = calculate_changes(y1)
changes_bryan = calculate_changes(y2)
changes_adam = calculate_changes(y3)
changes_mujeeb = calculate_changes(y4)
changes_tyler = calculate_changes(y5)
changes_arnold = calculate_changes(y6)

file_paths = [gavin, bryan, adam, mujeeb, tyler, arnold]
y_values_list = [read_y_values(file_path) for file_path in file_paths]

players = ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold']
player_paths = [p_gavin, p_bryan, p_adam, p_mujeeb, p_tyler, p_arnold]

players_data_proj = {
    'Gavin': (x13, y13),
    'Bryan': (x14, y14),
    'Adam': (x15, y15),
    'Mujeeb': (x16, y16),
    'Tyler': (x17, y17),
    'Arnold': (x18, y18)
}

players_data_real = {
    'Gavin': (x1, y1),
    'Bryan': (x2, y2),
    'Adam': (x3, y3),
    'Mujeeb': (x4, y4),
    'Tyler': (x5, y5),
    'Arnold': (x6, y6),
}

### Graphs

proj_bar_fig = make_subplots(rows=5, cols=2, subplot_titles=[f'Week {i+1}' for i in range(10)])

for i in range(10):
    row = i // 2 + 1
    col = i % 2 + 1

    for player, data in players_data_proj.items():
        x_data, y_data = data

        if 0 <= i < len(x_data) and 0 <= i < len(y_data):
            proj_bar_fig.add_trace(
                go.Bar(x=[x_data[i]], y=[y_data[i]], name=player, marker=dict(color=player_colors[player]), showlegend=False),
                row=row, col=col
            )

real_bar_fig = make_subplots(rows=5, cols=2, subplot_titles=[f'Week {i+1}' for i in range(10)])

for i in range(10):
    row = i // 2 + 1
    col = i % 2 + 1

    for player, data in players_data_real.items():
        x_data, y_data = data

        if 0 <= i < len(x_data) and 0 <= i < len(y_data):
            x_values = [0] * len(x_data)

            real_bar_fig.add_trace(
                go.Bar(x=x_values, y=[y_data[i]], name=player, marker=dict(color=player_colors[player]), showlegend=False),
                row=row, col=col
            )

simple_x = np.arange(1, 11)

changes_fig = go.Figure()

changes_fig.add_trace(go.Scatter(x=x1[1:], y=changes_gavin, mode='lines', name='Gavin', line=dict(color=player_colors['Gavin'])))
changes_fig.add_trace(go.Scatter(x=x2[1:], y=changes_bryan, mode='lines', name='Bryan', line=dict(color=player_colors['Bryan'])))
changes_fig.add_trace(go.Scatter(x=x3[1:], y=changes_adam, mode='lines', name='Adam', line=dict(color=player_colors['Adam'])))
changes_fig.add_trace(go.Scatter(x=x4[1:], y=changes_mujeeb, mode='lines', name='Mujeeb', line=dict(color=player_colors['Mujeeb'])))
changes_fig.add_trace(go.Scatter(x=x5[1:], y=changes_tyler, mode='lines', name='Tyler', line=dict(color=player_colors['Tyler'])))
changes_fig.add_trace(go.Scatter(x=x6[1:], y=changes_arnold, mode='lines', name='Arnold', line=dict(color=player_colors['Arnold'])))

weekly_pies_fig = make_subplots(rows=2, cols=5, subplot_titles=[f'Week {i+1}' for i in range(10)], specs=[[{'type': 'pie'}]*5]*2)

for i in range(len(y_values_list[0])):
    labels = ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold']
    values = [y_values[i] for y_values in y_values_list]
    
    weekly_pies_fig.add_trace(go.Pie(labels=labels, values=values, name=f'Week {i+1}',
    marker=dict(colors=[player_colors[player] for player in labels])),
    row=(i // 5) + 1, col=(i % 5) + 1)

above_below_avg_fig = make_subplots(rows=2, cols=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    above_below_avg_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    above_below_avg_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, marker=dict(size=10, color=player_colors[name])), row=2, col=1)

overall_trendline_y = [sum(week) / len(week) for week in zip(y1, y2, y3, y4, y5, y6)]

above_below_avg_fig.add_trace(go.Scatter(x=x1, y=overall_trendline_y, mode='lines', name='Overall Trendline', line=dict(color='black', dash='dash')), row=1, col=1)
above_below_avg_fig.add_trace(go.Scatter(x=x1, y=overall_trendline_y, mode='lines', name='Overall Trendline', line=dict(color='black', dash='dash')), row=2, col=1)

specific_fig = go.Figure()

overall_below_trendline_count = 0
overall_above_trendline_count = 0

overall_trendline_y = [sum(week) / len(week) for week in zip(y1, y2, y3, y4, y5, y6)]

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    overall_points = [sum(week) for week in zip(y1, y2, y3, y4, y5, y6)]

    markers_below_trendline = [val for val, trendline_val in zip(y, overall_trendline_y) if val < trendline_val]
    markers_above_trendline = [val for val, trendline_val in zip(y, overall_trendline_y) if val >= trendline_val]

    below_trendline_count = len(markers_below_trendline)
    above_trendline_count = len(markers_above_trendline)

    overall_below_trendline_count += below_trendline_count
    overall_above_trendline_count += above_trendline_count

    marker_colors = ['red' if val < trendline_val else 'green' for val, trendline_val in zip(y, overall_trendline_y)]
    
    specific_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=marker_colors)))

scatter_fig = make_subplots(rows=2, cols=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, line=dict(color=player_colors[name])), row=2, col=1)

win_rate_fig = make_subplots(rows=2, cols=1)

for i, (x, y, name) in enumerate([(x7, y7, 'Gavin'), (x8, y8, 'Bryan'), (x9, y9, 'Adam'), (x10, y10, 'Mujeeb'), (x11, y11, 'Tyler'), (x12, y12, 'Arnold')], start=1):
    win_rate_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x7, y7, 'Gavin'), (x8, y8, 'Bryan'), (x9, y9, 'Adam'), (x10, y10, 'Mujeeb'), (x11, y11, 'Tyler'), (x12, y12, 'Arnold')], start=1):
    win_rate_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, marker=dict(size=10, color=player_colors[name])), row=2, col=1)

pie_fig = go.Figure()

pie_fig.add_trace(go.Pie(labels=['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
values=[sum(y1), sum(y2), sum(y3), sum(y4), sum(y5), sum(y6)],
name='Total Points', marker=dict(colors=[player_colors['Gavin'], player_colors['Bryan'], player_colors['Adam'], player_colors['Mujeeb'], player_colors['Tyler'], player_colors['Arnold']])))

### Graph Layouts

scatter_fig.update_layout(
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=True,
    width=1000,
    height=800
)

win_rate_fig.update_layout(
    xaxis_title='Week #',
    yaxis_title='Win Rate',
    showlegend=True,
    width=800,
    height=600
)

above_below_avg_fig.update_layout(
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=True,
    width=1000,
    height=800
)

specific_fig.update_layout(
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=False,
    width=1000,
    height=800
)

weekly_pies_fig.update_layout(
    showlegend=True, 
    width=1340,
    height=600
)

changes_fig.update_layout(
    xaxis_title='Overall Player Point Total',
    yaxis_title='Change',
    showlegend=True,
    width=1000,
    height=600
)

proj_bar_fig.update_layout(
    title='Projected Point Totals by Week',
    showlegend=False,
    width=1340,
    height=800,
)

real_bar_fig.update_layout(
    title='Real Point Totals by Week',
    showlegend=False,
    width=1340,
    height=800,
)

### HTML Conversion 

scatter_html = scatter_fig.to_html(full_html=False)
pie_html = pie_fig.to_html(full_html=False)
win_rate_html = win_rate_fig.to_html(full_html=False)
above_below_avg_html = above_below_avg_fig.to_html(full_html=False)
specific_html = specific_fig.to_html (full_html=False)
weekly_pies_html = weekly_pies_fig.to_html(full_html=False)
changes_html = changes_fig.to_html(full_html=False)
proj_bar_html = proj_bar_fig.to_html(full_html=False)
real_bar_html = real_bar_fig.to_html(full_html=False)

### Stat Tables

data_1 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold', 'Total'],
    'Below Average Performances': [4, 4, 2, 7, 8, 4, 29],
    'Above Average Performances': [6, 6, 8, 3, 2, 6, 31],
}

df_table_1 = pd.DataFrame(data_1)

table_1_html = df_table_1.to_html(index=False)

data_2 = {
    'Player': ['Adam', 'Gavin', 'Bryan', 'Arnold', 'Mujeeb', 'Tyler'],
    'Total Points': [sum(y3), sum(y1), sum(y2), sum(y4), sum(y6), sum(y5)]
}

df_table_2 = pd.DataFrame(data_2)

table_2_html = df_table_2.to_html(index=False)

data_3 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Wins': [7, 6, 7, 3, 3, 4],
    'Losses': [3, 4, 3, 7, 7, 6],
}

df_table_3 = pd.DataFrame(data_3)

table_3_html = df_table_3.to_html(index=False)

data_4 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold', 'Total'],
    'Weeks Within Projection Margin': [3, 8, 8, 3, 4, 3, 29],
    'Weeks Outside Projection Margin': [7, 2, 2, 7, 6, 7, 31],
}

df_table_4 = pd.DataFrame(data_4)

table_4_html = df_table_4.to_html(index=False)

### Projected vs Real Tables

def color_map(val):
    intensity = min(1, abs(val) / 50)
    green_intensity = min(255, int(255 - abs(val) * 2 * intensity))
    red_intensity = min(255, int(255 - abs(val) * 2 * intensity))

    color = f'background-color: rgba(0, {green_intensity}, 0, 0.8)' if val > 0 else \
            f'background-color: rgba({red_intensity}, 0, 0, 0.8)' if val < 0 else \
            'background-color: rgba(255, 255, 255, 1)'
    
    text_color = 'color: white' if val != 0 else 'color: black'
    
    return f'{color}; {text_color}; text-align: center;'

def round_to_hundredth(value):
    return round(value, 2)

def custom_formatter(value):
    return '{:g}'.format(value) if isinstance(value, (float, int)) else str(value)

def create_rounded_table(data, week_num):
    df_table = pd.DataFrame(data)
    
    columns = [f'Week {week_num} Projected Points', f'Week {week_num} Real Points']
    
    for col in columns:
        df_table[col] = df_table[col].map(round_to_hundredth)
    
    df_table['Point Difference'] = df_table.apply(lambda row: round_to_hundredth(row[columns[1]] - row[columns[0]]), axis=1)
    
    df_table.set_index('Player', inplace=True)
    
    table_html = df_table.style.format(custom_formatter).applymap(color_map, subset=['Point Difference']) \
                    .to_html(index=False, escape=False, classes='styled-table') \
                    .replace('style="', f'style="white-space: nowrap; Week {week_num} ')
    
    return table_html

data_5 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 1 Projected Points': [119.5, 118.4, 133.3, 130.1, 132.4, 120],
    'Week 1 Real Points': [91.94, 114.88, 137.9, 61.58, 138.16, 133.76],
}

table_5_html_colored = create_rounded_table(data_5, 1)

data_6 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 2 Projected Points': [138.6, 129.7, 137.8, 131.2, 130, 116.9],
    'Week 2 Real Points': [108.2, 131.34, 128.32, 151.38, 122.48, 137.16],
}

table_6_html_colored = create_rounded_table(data_6, 2)

data_7 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 3 Projected Points': [142, 124.6, 141.3, 124, 135.8, 122.2],
    'Week 3 Real Points': [165.98, 152.3, 132.18, 122.32, 132.58, 145.02],
}

table_7_html_colored = create_rounded_table(data_7, 3)

data_8 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 4 Projected Points': [134.8, 125.8, 136.3, 127.1, 132.7, 124.3],
    'Week 4 Real Points': [148.32, 163.22, 142.96, 110.68, 103.38, 136.68],
}

table_8_html_colored = create_rounded_table(data_8, 4)

data_9 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 5 Projected Points': [136, 128.3, 144.5, 124.5, 135, 113.7],
    'Week 5 Real Points': [151.84, 126.58, 158.84, 159.46, 92.44, 112.32],
}

table_9_html_colored = create_rounded_table(data_9, 5)

data_10 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 6 Projected Points': [145, 130.5, 146.5, 126.7, 141.3, 127.1],
    'Week 6 Real Points': [143.74, 118.7, 151.8, 101.46, 117.62, 87.12],
}

table_10_html_colored = create_rounded_table(data_10, 6)

data_11 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 7 Projected Points': [138.9, 129.8, 144.1, 112.8, 118.4, 125.3],
    'Week 7 Real Points': [183.76, 143.1, 155.46, 110, 82.78, 81.34],
}

table_11_html_colored = create_rounded_table(data_11, 7)

data_12 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 8 Projected Points': [145.8, 132.7, 149.5, 128.7, 135.9, 125.7],
    'Week 8 Real Points': [102.8, 122.76, 192.06, 133.16, 98.38, 137.76],
}

table_12_html_colored = create_rounded_table(data_12, 8)

data_13 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 9 Projected Points': [131, 115.3, 148.6, 132.6, 113.2, 125.7],
    'Week 9 Real Points': [76.8, 109.38, 162.88, 89.82, 108.78, 90.32],
}

table_13_html_colored = create_rounded_table(data_13, 9)

data_14 = {
    'Player': ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
    'Week 10 Projected Points': [125.6, 125, 126.9, 137.3, 113.9, 127.6],
    'Week 10 Real Points': [135.08, 114.12, 167.04, 102.78, 97.42, 175.36],
}

table_14_html_colored = create_rounded_table(data_14, 10)

### HTML Commentaries

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

start = """
    <p>Starting things off, for my first graph I displayed the change in overall point totals over the span of 10 weeks fixed to the x-axis, 
    with the points added towards the player's overall point total with the y-axis.</p>
"""

commentaries_1 = """
    <p> The first thing you may notice is the volatility that many players display in their weekly point scorings. 
    Peculiarities such as Mujeeb's measly debut of 61.58 to an explosive showing of 151.38 points just the next week
    seem to imply high variance to player scoring outcomes week by week. 
    As we are dealing with statistics, however, there is always to be expected outliers who stray away from the general trend. 
    Adam has proved himself to be a remarkably consistent performer, reliably occupying a top 1 to 2 showing weekly, so it should come to no surprise
    Adam comes out with the highest overall point total of weeks 1-10, clocking in with an impressive 1529.44 points accrued. </p> 
"""

commentaries_2 = """
    <p> A aspect to this graph which stood out to me was Tyler's falloff exiting the beggining weeks, 
    going on a 6 week losing streak that would briefly drag him all the way down to a 17% win rate, the lowest anyone has gone thus far. 
    Similarly, even despite consistently strong weekly outings, Adam suffered an initial 4 week slump that brought his 
    win rate as low as 25%, although experienced a rebound beggining week 5. Bryan is the definitely one of the most volatile figures in the data, 
    frequently teasing a losing record, only to spike up once he comes close to an under 50% win rate. </p>
"""

commentaries_2_half = """
<p> With the insight gained from analyzing the fluctuating win rates of our 6 players, 
    let's now go back to the Change in Point Totals graph to add a trendline to see if we can further analyze player performances.</p>
"""

commentaries_3 = """
    <p> Smashing everyone's point totals into a pie chart reveals how relatively competitive the league is, 
    with not one person pertaining even a quarter percent share the of overall point total. Beyond my sample size of weeks 1-10, 
    I believe that the distance between teams will stand to further increase, and I expect some motion in who shares what percentage of the overall point total, 
    such as Bryan potentially overtaking me for second-most points. </p>
"""

commentaries_3_half = """
<p> We can also break the pie graph down to the player shares of the weekly overall point totals. </p>  
"""

commentaries_4 = """
    <p> With the addition of a trendline, we can see how Tyler's pitiful win rate can be considered
    a product of a continuous string of below average performances week to week. 
    It can also be inferred that Adam's early season slump is a possible consequence of his lone two below average performances during the span of weeks 2-3, 
    with his rebound reflected by his return to above average performances going from weeks 4-10. 
    It is also worth noting that below average points tend to be stay closer to the trendline, 
    whereas above averages points, chiefly during the latter end of the sample period, tend to be far more distanced from the trendline. </p>
"""

commentaries_4_half = """
<p> The chaotic spikes of up and down further reinforce my theory that there is a high variance in player scoring outcomes week by week. 
    Mujeeb in particular leapfrogs from being up sky high to hitting rock bottom almost routinely. The biggest drop in performance from one week to the next unfortunately goes to me, 
    scoring 80.96 points fewer in week 9 than I had during week 8. The largest jump in performance goes to Mujeeb, scoring 89.8 points more in week 2 than he had done during week 1. </p>
"""

commentaries_5 = """
<p> Surprisingly, everyone has had at least one week where they've enjoyed a plurality of the share of points scored. 
    As expected, Adam occupies the status of having the highest share of a week's total points scored, 
    being responsible for 25.5 percent of the points scored during week 9. 
    My first assumption was that Tyler would possess the lowest share of a week's total points scored, 
    but it is actually Mujeeb's meager showing of 61.58 points in week 1 that takes the cake for lowest share of a week's points scored total at 9.08 percent, 
    as well as being the only instance of a player being responsible for less than 10 percent of a week's total points scored. </p>
"""

commentaries_6 = """
<p> Notice that there are only three people who hold memberships to the elusive 170+ point week club, 
    that being myself, Adam, and, most interestingly, Arnold. Like Bryan, Arnold's been incredibly streaky week by week, albeit with a lower floor than Bryan, 
    so it was a shock to me when I faced against Arnold as my week 10 matchup to see him go from an unremarkable past couple of weeks performance-wise, 
    to blasting off to the moon with a monstrous 175.36 scoring. </p>
"""

commentaries_6_half = """
<p> There is also insight to be gained from looking at the outliers. For one, there are three above average performances that are under 120 points, 
    making them sit amidst a sea of red. Two of these occurred during week 9, which is to be expected, 
    as week 9 had the lowest average points scored amongst all weeks, sitting at a lowly 106.33-week average. The remaining point occurred during week 1, 
    wherein Bryan just barely squeaked out an above average performance by 1.84 points. Interestingly, Tyler possesses both the highest below average point score, 
    as well as the lowest above average point score, at 132.58 to a 141.73-week 3 average and 108.78 to a 106.33-week 9 average, respectively. </p>
"""

commentaries_7 = """
<p> Before games begin, most fantasy football platforms provide their own projections as to what they believe your point total outcome will be for the week. The platform we use, 
that being ESPN's fantasy app, shares this common attribute, and its projections are often used as one of the various statistics both me and my teammates consider in analyzing
how our teams will perform for the week. </p>
"""

commentaries_8 = """
<p> It can be inferred that projections tend to stay consistent week by week, albeit with 
    the occasional occurrence of a significant drop of 20 or so points in comparison to the week's former, although this phenomenon is more of a product of the concept of the NFL bye week, 
    wherein there are certain weeks where teams are granted a rest week with no slated games, 
    meaning players that would otherwise bolster someone's projection are now noncontributors for the duration of the week. 
    This is the reason why both myself and Adam's projections plummeted down from a respective 145.8 and 149.5 during week 9 down to a 125.6 and 126.9 in week 10.
"""

commentaries_9 = """
<p> Comparing both the projected point totals and real player point totals week by week, however, shows projections to be relatively unreliable at providing a realistic outlook
    in who will score what number of points for the week. Using a 10% margin of error, we can calculate projected point totals to be accurate at reflecting player performance only 48 percent
    of the time, with only Bryan and Adam having more projections being within the margin than outside of the margin. </p>
"""

commentaries_9_half = """
<p> This could also be used to further reinforce how luck-based fantasy performances are, as aspects of the game that can be highly influential in an individual's point total for the week,
    such as touchdowns, are incredibly difficult to predict yet can swing you from losing the week to winning it, as a single touchdown counts for 6 points. </p>
"""

commentaries_10 = """
<p> For another way to view the data, I've also configured the stats collected from every week into tables, as well as calculated the difference between the player's projected total and real total. </p>
"""

commentaries_11 = """
<p> As a final note, here are some of the various statistics I used displayed using simple tables. </p>
"""

tips = """
<p> To hide a variable, such as Gavin, click on the dots/lines next to names in the legend. This makes it so you can compare and contrast different players, 
    as well as look exclusively at the data of one certain player. You can unhide a variable by simply reclicking the aforementioned dots/lines. </p>
"""

### HTML Report 

html_report = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Fantasy Football Report</title>
    <link rel="stylesheet" href="fantasy.css">
    <style>
        body {{
            display: flex;
            flex-direction: column;
        }}
        header, nav {{
            width: 100%;
            text-align: center;
        }}
        nav ul {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            justify-content: flex-end;
        }}
        nav li {{
            margin-left: 10px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>The Fantasy Football Report</h1>
        <h5>By: Gavin Schnowske</h5>
    </header>

    <nav>
        <ul>
            <li><a href="#what-is-fantasy-football">What is Fantasy Football?</a></li>
            <li><a href="#change-in-point-totals">Change in Point Totals</a></li>
            <li><a href="#change-in-win-rate">Change in Win Rate</a></li>
            <li><a href="#trendline">Trendline</a></li>
            <li><a href="#change-in-player-point-totals">Change in Player Point Totals</a></li>
            <li><a href="#points-above-below-week-average">Points Above/Below Week Average</a></li>
            <li><a href="#overall-point-total-pie-chart">Overall Point Total Pie Chart</a></li>
            <li><a href="#projected-point-total-vs-real-point-total">Projected Point Total vs Real Point Total</a></li>
            <li><a href="#projected-point-total-vs-real-point-total-tables">Projected Point Total vs Real Point Total: Tables</a></li>
            <li><a href="#miscellaneous-player-stat-tables">Miscellaneous Player Stat Tables</a></li>
        </ul>
    </nav>

    <h2 id="what-is-fantasy-football">What is Fantasy Football?</h2>
    <div class="comm">
        {intro_text}
    </div>

    <!-- Points Total Scatter Plots Section -->
    <h2 id="change-in-point-totals">Change in Point Totals</h2>
    <div class="comm">
        {start}
    </div>
    <div class="set">
        {scatter_html} <aside>{tips}</aside>
    </div>
    <div class="comm">
        {commentaries_1}
    </div>

    <!-- Win Rate Scatter Plot Section -->
    <h2 id="change-in-win-rate">Change in Win Rate</h2>
    <div class="set">
        {win_rate_html}
    </div>
    <div class="comm">
        {commentaries_2}
    </div>

    <!-- Trendline Scatter Plots Section -->
    <h2 id="trendline">Trendline</h2>
    <div class="comm">
        {commentaries_2_half}
    </div>
    <div class="set">
        {above_below_avg_html}
    </div>
    <div class="comm">
        {commentaries_4}
    </div>

    <!-- Trendline Scatter Plots Section -->
    <h2 id="change-in-player-point-totals">Change in Player Point Totals</h2>
    <div class="set">
        {changes_html}
    </div>
    <div class="comm">
        {commentaries_4_half}
    </div>

    <!-- Above/Below Average Scatter Plot Section -->
    <h2 id="points-above-below-week-average">Points Above/Below Week Average</h2>
    <div class="set">
        {specific_html}
    </div>
    <div class="comm">
        {commentaries_6}
    </div>
    <hr class="block">
    <div class="comm">
        {commentaries_6_half}
    </div>

    <!-- Pie Chart Section -->
    <h2 id="overall-point-total-pie-chart">Overall Point Total Pie Chart</h2>
    <div class="other">
        {pie_html}
    </div>
    <div class="comm">
        {commentaries_3}
    </div>
    <hr class="block">
    <div class="comm">
        {commentaries_3_half}
    </div>
    <div class="set">
        {weekly_pies_html}
    </div>
    <div class="comm">
        {commentaries_5}
    </div>

    <!-- Bar Graphs Section -->
    <h2 id="projected-point-total-vs-real-point-total">Projected Point Total vs Real Point Total</h2>
    <div class="comm">
        {commentaries_7}
    </div>
    <div class="set">
        {proj_bar_html}
    </div>
    <div class="comm">
        {commentaries_8}
    </div>
    <div class="set">
        {real_bar_html}
    </div>
    <div class="comm">
        {commentaries_9}
    </div>
    <hr class="block">
    <div class="comm">
        {commentaries_9_half}
    </div>

    <!-- Stack Plot Section -->
    <h2 id="projected-point-total-vs-real-point-total-tables">Projected Point Total vs Real Point Total: Tables</h2>
    <div class="comm">
        {commentaries_10}
    </div>
    <div class="other">
        {table_5_html_colored}
        {table_6_html_colored}
        {table_7_html_colored}
        {table_8_html_colored}
        {table_9_html_colored}
        {table_10_html_colored}
        {table_11_html_colored}
        {table_12_html_colored}
        {table_13_html_colored}
        {table_14_html_colored}
    </div>

    <!-- Player Stats Tables -->
    <h2 id="miscellaneous-player-stat-tables">Miscellaneous Player Stat Tables</h2>
    <div class="comm">
        {commentaries_11}
    </div>
    <div class="other">
        {table_1_html}
        {table_2_html}
        {table_3_html}
        {table_4_html}
    </div>

</body>
</html>
"""

with open('index.html', 'w') as report_file:
    report_file.write(html_report)