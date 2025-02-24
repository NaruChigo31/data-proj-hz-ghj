import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

import plotly.express as px

data = pd.read_csv('..\cleaned_and_parsed_dataset.csv')

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
fig3.show()