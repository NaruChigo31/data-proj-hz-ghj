import pandas as pd
import matplotlib.pyplot as plt

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
years = most_popular['year']
popularity = most_popular['popularity']
genres = most_popular['track_genre']

# Create a dictionary to map genres to unique colors
unique_genres = genres.unique()
genre_colors = {genre: color for genre, color in zip(unique_genres, plt.cm.tab10.colors)}

# Plot the line
plt.figure(figsize=(12, 8))
plt.plot(years, popularity, color='black', linewidth=2, label="Popularity Trend")

# Add colored dots for each year based on genre
for year, pop, genre in zip(years, popularity, genres):
    plt.plot(year, pop, 'o', label=genre if genre not in plt.gca().get_legend_handles_labels()[1] else "")

# Customize the legend to show genres
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.title('Most Popular Genre by Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Popularity (Mean)', fontsize=14)
plt.grid(alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()