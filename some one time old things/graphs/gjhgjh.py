import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

# Load the dataset
data = pd.read_csv('..\cleaned_and_parsed_dataset.csv')

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

GenreNamesList = list(dict.fromkeys(genres))

colors = sns.color_palette("bright", n_colors=len(GenreNamesList)).as_hex()
sns.set_palette(colors, n_colors=len(GenreNamesList), desat=0.05, color_codes=False)
colors = list(dict.fromkeys(colors))
append_colors = lambda x: [x.append(i) for i in ["#ff0080", "#115e04"]]
append_colors(colors)

# Create the figure
fig = go.Figure()

# Add the line for the popularity trend
fig.add_trace(go.Scatter(
    x=years,
    y=popularity,
    mode='lines+markers',
    line=dict(color='black', width=2),
    marker=dict(symbol='circle', size=8, color='black'),
    name="Popularity Trend"
))

# Add colored dots for each year based on genre
added_genres = []  # List to keep track of genres added to the legend

for year, pop, genre in zip(years, popularity, genres):
    # Only add the genre to the legend the first time it appears
    if genre not in added_genres:
        fig.add_trace(go.Scatter(
            x=[year],
            y=[pop],
            mode='markers',
            marker=dict(color=colors[GenreNamesList.index(genre)], size=10),
            name=genre,
            showlegend=True
        ))
        added_genres.append(genre)  # Add the genre to the list of added genres
    else:
        # If the genre is already in the legend, just add the point without a legend entry
        fig.add_trace(go.Scatter(
            x=[year],
            y=[pop],
            mode='markers',
            marker=dict(color=colors[GenreNamesList.index(genre)], size=10),
            showlegend=False
        ))

# Update the layout for titles, labels, and legend
fig.update_layout(
    title='Most Popular Genre by Year',
    title_font_size=16,
    xaxis_title='Year',
    yaxis_title='Popularity (Mean)',
    xaxis=dict(tickmode='linear'),
    yaxis=dict(tickmode='linear'),
    legend_title="Genre",
    legend=dict(x=1.05, y=1, traceorder='normal'),
    plot_bgcolor='white',
    showlegend=True
)

# Show the plot
fig.show()