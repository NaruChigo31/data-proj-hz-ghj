import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly
import chart_studio.plotly as py
import plotly.tools as tls

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
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the line
ax.plot(years, popularity, linestyle='-', marker='o', color='black', linewidth=1, label="Popularity Trend")



# Add colored dots for each year based on genre
for year, pop, genre in zip(years, popularity, genres):
    ax.plot(year, pop, linestyle='-', marker='o', color=colors[GenreNamesList.index(genre)], label=genre if genre not in ax.get_legend_handles_labels()[1] else "")


# Customize the legend to show genres
ax.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
ax.set_title('Most Popular Genre by Year', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Popularity (Mean)', fontsize=14)
ax.grid(alpha=0.3)

plotly_fig = tls.mpl_to_plotly(fig)
plotly.offline.plot(plotly_fig, filename="plotly version of an mpl figure")
# Now the plot is stored in the `fig` variable