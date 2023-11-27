import csv
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Define file paths
points_files = {
    'Gavin': 'points/gavin.txt',
    'Bryan': 'points/bryan.txt',
    'Adam': 'points/adam.txt',
    'Mujeeb': 'points/mujeeb.txt',
    'Tyler': 'points/tyler.txt',
    'Arnold': 'points/arnold.txt',
}

win_percentage_files = {
    'Gavin': 'win-percentage/gavin-win.txt',
    'Bryan': 'win-percentage/bryan-win.txt',
    'Adam': 'win-percentage/adam-win.txt',
    'Mujeeb': 'win-percentage/mujeeb-win.txt',
    'Tyler': 'win-percentage/tyler-win.txt',
    'Arnold': 'win-percentage/arnold-win.txt',
}

# Read data from files
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

player_data = {}

for player, file_path in points_files.items():
    player_data[player] = read_data(file_path)

win_percent_data = {}

for player, file_path in win_percentage_files.items():
    win_percent_data[player] = read_data(file_path)

# Create a list of players and their respective colors
players = ['Gavin', 'Bryan', 'Adam', 'Mujeeb', 'Tyler', 'Arnold']
colors = ['#E50184', '#FFBA00', '#D80030', '#F65900', '#3461EF', '#00D5A0']

# Create a dictionary for player colors
player_colors = dict(zip(players, colors))

# Create subplots
scatter_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])
win_percent_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])
above_below_avg_fig = make_subplots(rows=2, cols=1, subplot_titles=['Scatter Plot', 'Line Plot'])
specific_fig = go.Figure()
stack_plot_fig = go.Figure()
table_new_fig = go.Figure()

# Initialize counters
overall_below_trendline_count = 0
overall_above_trendline_count = 0

# Iterate through players
for i, player in enumerate(players, start=1):
    x, y = player_data[player]

    # Plotting scatter plot
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=player, marker=dict(size=10, color=player_colors[player])), row=1, col=1)

    # Plotting line plot
    scatter_fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=player, line=dict(color=player_colors[player])), row=2, col=1)

    # Calculate overall trendline
    overall_trendline_y = [(sum(week) / len(week)) for week in zip(*[player_data[p][1] for p in players])]

    # Plotting overall trendline
    scatter_fig.add_trace(go.Scatter(x=x, y=overall_trendline_y, mode='lines', name='Overall Trendline', line=dict(color='black', dash='dash')), row=1, col=1)
    scatter_fig.add_trace(go.Scatter(x=x, y=overall_trendline_y, mode='lines', name='Overall Trendline', line=dict(color='black', dash='dash')), row=2, col=1)

    # Count points above and below trendline
    markers_below_trendline = [val for val, trendline_val in zip(y, overall_trendline_y) if val < trendline_val]
    markers_above_trendline = [val for val, trendline_val in zip(y, overall_trendline_y) if val >= trendline_val]

    below_trendline_count = len(markers_below_trendline)
    above_trendline_count = len(markers_above_trendline)

    # Update overall counts
    overall_below_trendline_count += below_trendline_count
    overall_above_trendline_count += above_trendline_count

    # Print individual player counts
    print(f'For {player}:')
    print(f'Number of points below trendline: {below_trendline_count}')
    print(f'Number of points above trendline: {above_trendline_count}')

    # Plotting specific points below and above trendline
    specific_fig.add_trace(go.Scatter(x=x, y=markers_below_trendline, mode='markers', name=player + ' Below Trendline', marker=dict(size=10, color='red')))
    specific_fig.add_trace(go.Scatter(x=x, y=markers_above_trendline, mode='markers', name=player + ' Above Trendline', marker=dict(size=10, color='green')))

# Print overall counts
print('\nOverall counts:')
print(f'Number of points below trendline: {overall_below_trendline_count}')
print(f'Number of points above trendline: {overall_above_trendline_count}')

# Plotting pie chart
pie_fig = go.Figure()
pie_fig.add_trace(go.Pie(labels=players, values=[sum(player_data[player][1]) for player in players], name='Total Points',
                        marker=dict(colors=colors)))

# Plotting stack plot
stack_plot_fig = go.Figure()

for player in players:
    stack_plot_fig.add_trace(go.Scatter(x=simple_x, y=player_data[player][1], fill='tozeroy', mode='none', name=player, fillcolor=player_colors[player],
                                       line=dict(color='rgba(255,255,255,0)')))

# Update layout for all figures
def update_layout(fig, title_text, width, height):
    fig.update_layout(
        title_text=title_text,
        showlegend=True,
        width=width,
        height=height,
    )

update_layout(scatter_fig, 'Fantasy Football Scoring: Weeks 1-10', 1000, 800)
update_layout(win_percent_fig, 'Fantasy Football Win Percentages: Weeks 1-10', 800, 600)
update_layout(above_below_avg_fig, 'Fantasy Football Points: Above/Below Weekly Average', 1000, 800)
update_layout(specific_fig, 'Fantasy Football Points: Above/Below Weekly Average', 1000, 800)
update_layout(stack_plot_fig, 'Stack Plot', 800, 600)

# Create DataFrame for table
table_data = {'Player': players, 'Below Trendline': [4, 4, 2, 7, 8, 4], 'Above Trendline': [6, 6, 8, 3, 2, 6]}
table_df = pd.DataFrame(table_data)

# Plotting table
table_new_fig = go.Figure(data=[go.Table(header=dict(values=table_df.columns),
                                         cells=dict(values=[table_df.Player, table_df['Below Trendline'], table_df['Above Trendline']]))
                                ])

# Update layout for the table
update_layout(table_new_fig, 'Points Above and Below Trendline Counts', None, None)

# Create HTML strings
scatter_html = scatter_fig.to_html(full_html=False)
win_percent_html = win_percent_fig.to_html(full_html=False)
above_below_avg_html = above_below_avg_fig.to_html(full_html=False)
specific_html = specific_fig.to_html(full_html=False)
stack_plot_html = stack_plot_fig.to_html(full_html=False)
pie_html = pie_fig.to_html(full_html=False)
table_new_html = table_new_fig.to_html(full_html=False)

# Modify table HTML for styling
table_new_html = table_new_html.replace('<table>', '<table style="border-collapse: collapse; width: 100%; border: 1px solid #ddd;">')
table_new_html = table_new_html.replace('<th>', '<th style="padding: 15px; text-align: left; border-bottom: 1px solid #ddd;">')
table_new_html = table_new_html.replace('<td>', '<td style="padding: 15px; border-bottom: 1px solid #ddd;">')

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
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
     {tableNew_html}
    </div>
    <div class="comm">
        {commentaries1}
    </div>

    <!-- Player Stats Table -->
        <h2>Player Stats</h2>
    <div style="width: 50%; margin: 20px 20px 20px 20px;">
        {table_html}
    </div>
    <div class="comm">
        {commentaries1}
    </div>
</body>
</html>
"""

with open('prototype.html', 'w') as report_file:
    report_file.write(html_report)