# Importing libraries.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("../cleaned_and_parsed_dataset.csv")

# Prepare data for the scatter plot
x = df["tempo"]
y = df["danceability"]

# Create a stylish scatter plot
plt.figure(figsize=(12, 8))
# scatter = plt.hexbin(x, y, gridsize=20)
colors = sns.color_palette("coolwarm", len(x))
colors.reverse()
scatter = plt.hist2d(x, y, cmap="coolwarm",bins=50)


# Add title and axis labels
plt.title("Danceability vs Tempo", fontsize=16, fontweight="bold")
plt.xlabel("Tempo", fontsize=12)
plt.ylabel("Danceability", fontsize=12)

# Tight layout to avoid clipping
plt.tight_layout()

# Show the plot
plt.show()