import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import os

# Load the dataset
data = pd.read_csv(os.path.abspath("cleaned_and_parsed_dataset.csv"))

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

# Create the figure
fig2 = go.Figure()

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
    genre_years = [years[i] for i in range(len(years)) if genres[i] == genre]
    genre_popularity = [popularity[i] for i in range(len(popularity)) if genres[i] == genre]

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

# Show the plot
# fig2.show()
print(data.head())