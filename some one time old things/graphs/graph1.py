import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
df = pd.read_csv("../cleaned_and_parsed_dataset.csv")

# taking the popularity average of each genre
avgTable = df.groupby('track_genre', as_index=False)

# Calculate the mean popularity
avgTable = avgTable['popularity'].mean()

# Sort by mean popularity in descending order
avgTable = avgTable.sort_values(by='popularity', ascending=True)

y = avgTable["popularity"].tolist()
x = avgTable["track_genre"].tolist()


colors = sns.color_palette("coolwarm", len(x))
colors.reverse()

# Creat the bar chart
plt.figure(figsize=(14, 7))
bars = plt.barh(x, y, height=0.9, color=colors)

# Add data labels on the bars
for bar, value in zip(bars, y):
    left = bar.get_width() + 0.5
    height = bar.get_y() + bar.get_height() / 2
    plt.text(left, height, f"{value:.1f}", va="center", fontsize=10)

# Adding the title and axis labels
plt.title("Average Popularity by Genre", fontsize=18, fontweight="bold")
plt.ylabel("Genre", fontsize=14)

# Style adjustments
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()

# # Hiding the x-axis
# axes = plt.gca()
# xAxis = axes.axes.get_xaxis().set_visible(False)

plt.show()