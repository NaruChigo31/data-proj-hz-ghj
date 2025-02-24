import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('..\cleaned_and_parsed_dataset.csv')

# Extract year from the date column
data['year'] = pd.to_datetime(data['release_date'], errors='coerce').dt.year

# Remove rows with missing or invalid years or track_genre
data = data.dropna(subset=['year', 'track_genre'])

# Group by year and track_genre, then count the number of tracks
grouped = data.groupby(['year', 'track_genre']).size().reset_index(name='track_count')

# Find the genre with the highest count of tracks for each year
most_tracks = grouped.loc[grouped.groupby('year')['track_count'].idxmax()]

# Prepare data for plotting
years = most_tracks['year'].to_list()
track_counts = most_tracks['track_count'].to_list()
genres = most_tracks['track_genre'].to_list()
print(genres)

colors = sns.color_palette("muted", len(genres)).as_hex()
sns.set_palette(colors, len(genres), desat=0.1, color_codes=False)
print(colors[0])


# Plot the line
plt.figure(figsize=(12, 8))
plt.plot(years, track_counts, color='black', linewidth=2, label="Track Count Trend")

# Add colored dots for each year based on genre
for year, count, genre in zip(years, track_counts, genres):
    plt.plot(year, count, 'o', color=colors[genres.index(genre)], label=genre if genre not in plt.gca().get_legend_handles_labels()[1] else "")

# Customize the legend to show genres
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.title('Genre with Most Tracks by Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Tracks', fontsize=14)
plt.grid(alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()