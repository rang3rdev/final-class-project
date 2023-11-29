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

w_gavin = 'win-percentage/gavin-win.txt'
w_bryan = 'win-percentage/bryan-win.txt'
w_adam = 'win-percentage/adam-win.txt'
w_mujeeb = 'win-percentage/mujeeb-win.txt'
w_tyler = 'win-percentage/tyler-win.txt'
w_arnold = 'win-percentage/arnold-win.txt'

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
    
    weekly_pies_fig.add_trace(go.Pie(labels=labels, values=values, name=f'Line {i+1}',
    marker=dict(colors=[player_colors[player] for player in labels])),
    row=(i // 5) + 1, col=(i % 5) + 1)

stack_plot_fig = go.Figure()

stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y3, fill='tozeroy', mode='none', name='Adam', fillcolor=player_colors['Adam'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y1, fill='tozeroy', mode='none', name='Gavin', fillcolor=player_colors['Gavin'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y2, fill='tozeroy', mode='none', name='Bryan', fillcolor=player_colors['Bryan'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y6, fill='tozeroy', mode='none', name='Arnold', fillcolor=player_colors['Arnold'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y4, fill='tozeroy', mode='none', name='Mujeeb', fillcolor=player_colors['Mujeeb'], line=dict(color='rgba(255,255,255,0)')))
stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=y5, fill='tozeroy', mode='none', name='Tyler', fillcolor=player_colors['Tyler'], line=dict(color='rgba(255,255,255,0)')))

above_below_avg_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

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

scatter_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x1, y1, 'Gavin'), (x2, y2, 'Bryan'), (x3, y3, 'Adam'), (x4, y4, 'Mujeeb'), (x5, y5, 'Tyler'), (x6, y6, 'Arnold')], start=1):
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, line=dict(color=player_colors[name])), row=2, col=1)

win_rate_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])

for i, (x, y, name) in enumerate([(x7, y7, 'Gavin'), (x8, y8, 'Bryan'), (x9, y9, 'Adam'), (x10, y10, 'Mujeeb'), (x11, y11, 'Tyler'), (x12, y12, 'Arnold')], start=1):
    win_rate_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=name, marker=dict(size=10, color=player_colors[name])), row=1, col=1)

for i, (x, y, name) in enumerate([(x7, y7, 'Gavin'), (x8, y8, 'Bryan'), (x9, y9, 'Adam'), (x10, y10, 'Mujeeb'), (x11, y11, 'Tyler'), (x12, y12, 'Arnold')], start=1):
    win_rate_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=name, marker=dict(size=10, color=player_colors[name])), row=2, col=1)

pie_fig = go.Figure()

pie_fig.add_trace(go.Pie(labels=['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold'],
values=[sum(y1), sum(y2), sum(y3), sum(y4), sum(y5), sum(y6)],
name='Total Points', marker=dict(colors=[player_colors['Gavin'], player_colors['Bryan'], player_colors['Adam'], player_colors['Mujeeb'], player_colors['Tyler'], player_colors['Arnold']])))

scatter_fig.update_layout(
    title_text='Fantasy Football Scoring: Weeks 1-10',
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=True,
    width=1000,
    height=800,
)

win_rate_fig.update_layout(
    title_text='Fantasy Football Win Rates: Weeks 1-10',
    xaxis_title='Week #',
    yaxis_title='Win Rate',
    showlegend=True,
    width=800,
    height=600,
)

above_below_avg_fig.update_layout(
    title_text='Above/Below Weekly Average',
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=True,
    width=1000,
    height=800,
)

specific_fig.update_layout(
    title_text='Fantasy Football Points: Above/Below Weekly Average',
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=False,
    width=1000,
    height=800,
)

stack_plot_fig.update_layout(
    xaxis_title='Week #',
    yaxis_title='Points Added Towards Total',
    showlegend=True,
    plot_bgcolor='rgba(255,255,255,0.9)',
    paper_bgcolor='rgba(255,255,255,0.9)',
    width=800,
    height=600,
)

weekly_pies_fig.update_layout(
    title_text=f'Share of the Week Point Total: Weeks 1-10',
    height=600, 
    width=1340
)

changes_fig.update_layout(
    title_text='Changes in Y-Values for Each Player',
    xaxis_title='Player Point Total',
    yaxis_title='Points Added Towards Total',
    showlegend=True,
    width=1000,
    height=600,
)

scatter_html = scatter_fig.to_html(full_html=False)
pie_html = pie_fig.to_html(full_html=False)
win_rate_html = win_rate_fig.to_html(full_html=False)
above_below_avg_html = above_below_avg_fig.to_html(full_html=False)
stack_plot_html = stack_plot_fig.to_html (full_html=False)
specific_html = specific_fig.to_html (full_html=False)
weekly_pies_html = weekly_pies_fig.to_html(full_html=False)
changes_html = changes_fig.to_html(full_html=False)

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
    and visualized the additional points added towards the player's point total that week with the y-axis.</p>
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
    <p> Now seeing a visualization of the win rates across players, 
    let's now go back to the Change in Point Totals graph to add a trendline to see if we can further analyze player performances.</p>
"""

commentaries_3 = """
    <p> Smashing everyone's point totals into a pie chart reveals how relatively competitive the league is, 
    with not one person pertaining even a quarter percent share the of overall point total. Beyond my sample size of weeks 1-10, 
    I believe that the distance between teams will stand to further increase, and I expect some motion in who shares what percentage of the overall point total, 
    such as Bryan potentially overtaking me for second-most points. </p>
    <p> We can also break the pie graph down to the player shares of the weekly point totals for weeks 1-10. </p>  
"""

commentaries_4 = """
    <p> With the addition of a trendline, we can see how Tyler's pitiful win rate can be considered
    a product of a continuous string of below average performances week to week. 
    It can also be inferred that Adam's early season slump is a possible consequence of his lone two below average performances during the span of weeks 2-3, 
    with his rebound reflected by his return to above average performances going from weeks 4-10. 
    It is also worth noting that below average points tend to be stay closer to the trendline, 
    whereas above averages points, chiefly during the latter end of the sample period, tend to be far more distanced from the trendline. </p>
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
<p> Analyzing this graph, you can see that only three people are members of the elusive 170+ point week club, 
that being myself, Adam, and, most interestingly, Arnold. Like Bryan, Arnold's been incredibly streaky week by week, albeit with a lower floor than Bryan, 
so it was a shock to me when I faced against Arnold as my week 10 matchup to see him go from an unremarkable past couple of weeks performance-wise, 
to blasting off to the moon with a monstrous 175.36 scoring. </p>
<p> There is also insight to be gained from looking at the outliers. For one, there are three above average performances that are under 120 points, 
making them sit amidst a sea of red. Two of these occurred during week 9, which is to be expected, 
as week 9 had the lowest average points scored amongst all weeks, sitting at a lowly 106.33-week average. The remaining point occurred during week 1, 
wherein Bryan just barely squeaked out an above average performance by 1.84 points. Interestingly, Tyler possesses both the highest below average point score, 
as well as the lowest above average point score, at 132.58 to a 141.73-week 3 average and 108.78 to a 106.33-week 9 average, respectively. </p>
"""

tips = """
<p> To hide a variable, such as Gavin, click on the dots/lines next to names in the legend. This makes it so you can compare and contrast different players, 
as well as look exclusively at the data of one certain player. You can unhide a variable by simply reclicking the aforementioned dots/lines. </p>
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
        {commentaries_1}
    </div>

    <!-- Win Rate Scatter Plot Section -->
        <h2>Change in Win Rate: Weeks 1-10</h2>
    <div style="width: 100%; margin: 20px 20px 20px 20px;">
        {win_rate_html}
    </div>
    <div class="comm">
        {commentaries_2}
    </div>

    <!-- Averages Scatter Plot Section -->
        <h2>Trendline: Weeks 1-10</h2>
    <div style="width: 100%; margin: 20px 20px 20px 20px;">
        {above_below_avg_html}
        {changes_html}
    </div>
    <div class="comm">
        {commentaries_4}
    </div>

    <!-- Averages Scatter Plot Section -->
        <h2>Points Above/Below Average: Weeks 1-10</h2>
    <div style="width: 100%; margin: 20px 20px 20px 20px;">
        {specific_html}
    </div>
    <div class="comm">
        {commentaries_6}
    </div>

    <!-- Pie Chart Section -->
        <h2>Pie Chart</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {pie_html}
    </div>
    <div class="comm">
        {commentaries_3}
    </div>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {weekly_pies_html}
    </div>
    <div class="comm">
        {commentaries_5}
    </div>
        
    <!-- Pie Chart Section -->
        <h2>Stack Plot</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {stack_plot_html}
    </div>
    <div class="comm">
        {explanations}
    </div>

    <!-- Player Stats Tables -->
        <h2>Player Stats</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {table_2_html}
        {table_1_html}
    </div>
    <div class="comm">
        {commentaries_1}
    </div>
</body>
</html>
"""

with open('index.html', 'w') as report_file:
    report_file.write(html_report)