'''

This script creates the graphs for:
    the average popularity by genre, 
    the most popular genre by year, and 
    the explicit and non-explicit songs popularity. 

The graphs are saved as HTML strings and rendered in the templateGraphs.html file.

'''

# Import the required libraries
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import plotly.express as px
import os
from jinja2 import Template

# Path to the actual graphs HTML page
output_html_path = os.path.abspath("app\\templates\\graphs.html")
#path to the template
input_template_path = os.path.abspath("app\\templates\\templateGraphs.html" )     

# Load the dataset
data = pd.read_csv(os.path.abspath("cleaned_and_parsed_dataset.csv"))


# function to create the graph for average popularity by genre
def graph_avg_pop_genre(data, show=False):

    global fig1
    fig1 = go.Figure()

    # Calculate the mean popularity for each genre
    avgTable = data.groupby('track_genre', as_index=False)['popularity'].mean()

    # Sort by mean popularity in descending order
    avgTable = avgTable.sort_values(by='popularity', ascending=True)

    y = avgTable["popularity"].tolist()
    x = avgTable["track_genre"].tolist()

    # Get a color palette from seaborn
    colors1 = sns.color_palette("coolwarm", len(x)).as_hex()

    # Add horizontal bars for each genre's average popularity
    fig1.add_trace(go.Bar(
        y = x,  # Genres on y-axis
        x = y,  # Popularity on x-axis
        orientation = 'h',
        marker=dict(color=colors1),
        text = [f"{value:.1f}" for value in y],  # Data labels on bars
        textposition = 'inside',
        name = "Average Popularity"
    ))

    # Update layout for title, axis labels, and grid
    fig1.update_layout(
        title="Average Popularity by Genre",
        title_font_size=18,
        xaxis_title="Popularity",
        yaxis_title="Genre",
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightGray'),
        yaxis=dict(showgrid=False),
        plot_bgcolor='white',
        margin=dict(l=150, r=20, t=40, b=40)
    )
    # Show the plot
    if show:
        fig1.show()

# function to create the graph for most popular genre by year
def graph_most_pop_genre_year(data, show=False):

    global fig2
    fig2 = go.Figure()

    # Extract year from the date column
    data['year'] = pd.to_datetime(data['release_date'], errors='coerce').dt.year

    # Remove rows with missing or invalid years, genres, or popularity
    data = data.dropna(subset=['year', 'track_genre', 'popularity'])

    # Group by year and genre, then calculate mean popularity
    grouped = data.groupby(['year', 'track_genre'])['popularity'].mean().reset_index()

    # Find the most popular genre for each year
    most_popular = grouped.loc[grouped.groupby('year')['popularity'].idxmax()]

    # Prepare data for plotting
    years = most_popular['year'].to_list()
    popularity = most_popular['popularity'].to_list()
    genres = most_popular['track_genre'].to_list()

    # making list with genres without repetition
    GenreNamesList = list(dict.fromkeys(genres))

    colors = sns.color_palette("bright", n_colors=len(GenreNamesList)).as_hex()
    sns.set_palette(colors, n_colors=len(GenreNamesList), desat=0.05, color_codes=False)
    colors = list(dict.fromkeys(colors))
    append_colors = lambda x: [x.append(i) for i in ["#ff0080", "#115e04"]]
    append_colors(colors)

    # Add the line for the popularity trend
    fig2.add_trace(go.Scatter(
        x = years,
        y = popularity,
        mode = 'lines+markers',
        line=dict(color='black', width=2),
        marker=dict(symbol='circle', size=8, color='black'),
        name = "Popularity Trend"
    ))

    # Add colored dots for each year based on genre
    for genre in GenreNamesList:
        # Filter data for the current genre
        genre_years = [years[i] for i in range(len(years)) if genres[i] == genre]
        genre_popularity = [popularity[i] for i in range(len(popularity)) if genres[i] == genre]

        # Add the scatter plot for the current genre
        fig2.add_trace(go.Scatter(
            x=genre_years,
            y=genre_popularity,
            mode='markers',
            marker=dict(color=colors[GenreNamesList.index(genre)], size=10),
            name = genre,
            showlegend = True
        ))

    # Update the layout for titles, labels, and legend
    fig2.update_layout(
        title = 'Most Popular Genre by Year',
        title_font_size = 16,
        xaxis_title = 'Year',
        yaxis_title = 'Popularity (Mean)',
        # xaxis=dict(tickmode='linear', dtick = 4),
        yaxis=dict(tickmode='linear', range=[0, 100], dtick=10),
        legend_title="Genre",
        legend=dict(x=1.05, y=1, traceorder='normal'),
        plot_bgcolor='white',
        showlegend=True
    )
    fig2.update_xaxes(rangeslider_visible=True)

    if show:
        fig2.show()

# function to create the graph for explicit and non-explicit songs popularity
def graph_explicit_or_non(data, show=False):
    global fig3
    fig3 = px.histogram(data, x="popularity", color="explicit") 
    # Update the layout for titles, labels, and legend
    fig3.update_layout(
        title = 'Avarage popularity of Explicit and Non-Explicit Songs',
        title_font_size = 16,
        xaxis_title = 'Popularity (Mean)',
        legend_title="Genre",
        showlegend=True,
        margin=dict(l=150, r=20, t=40, b=40)
    )
    # Show the plot
    if show:
        fig3.show()

# Call the functions to create the graphs
graph_avg_pop_genre(data)
graph_most_pop_genre_year(data)
graph_explicit_or_non(data)

# Save the figures as HTML strings
plotly_jinja_data = {"fig1":fig1.to_html(full_html=False), 
                     "fig2":fig2.to_html(full_html=False), 
                     "fig3":fig3.to_html(full_html=False)}

# Render the HTML template with the plotly figures
with open(output_html_path, "w", encoding="utf-8") as output_file:
    with open(input_template_path) as template_file:
        j2_template = Template(template_file.read())
        output_file.write(j2_template.render(plotly_jinja_data))
