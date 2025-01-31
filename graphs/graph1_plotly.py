import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

# Load the dataset
df = pd.read_csv("../cleaned_and_parsed_dataset.csv")

# Calculate the mean popularity for each genre
avgTable = df.groupby('track_genre', as_index=False)['popularity'].mean()

# Sort by mean popularity in descending order
avgTable = avgTable.sort_values(by='popularity', ascending=True)

y = avgTable["popularity"].tolist()
x = avgTable["track_genre"].tolist()

# Get a color palette from seaborn
colors = sns.color_palette("coolwarm", len(x)).as_hex()

# Create the Plotly figure
fig1 = go.Figure()

# Add horizontal bars for each genre's average popularity
fig1.add_trace(go.Bar(
    y = x,  # Genres on y-axis
    x = y,  # Popularity on x-axis
    orientation = 'h',
    marker=dict(color=colors),
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
fig1.show()