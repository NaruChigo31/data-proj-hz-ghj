import pandas as pd
import plotly.graph_objects as go
import seaborn as sns

import plotly.express as px
# df = px.data.tips()
# print(df)
# Load the dataset
data = pd.read_csv('..\cleaned_and_parsed_dataset.csv')

grouped = data.groupby(['popularity', 'explicit'])['popularity'].count()
# print(grouped)
# print(grouped.to_dict())
# записать в репорт про ошибку словаря
popularityExplicit = []
popularityOkey = []
amountExplicit = []
amountOkey = []

for i in grouped.index:
    if i[1]:
        popularityExplicit.append(i[0])
        amountExplicit.append(int(grouped[i]))
    else:
        popularityOkey.append(i[0])
        amountOkey.append(int(grouped[i]))
    # print(i[0], i[1])
    # print(grouped[i])
    # print("---------------------------------------------------------")

# used to check what the hack th grouped is
# popularity = grouped.tolist()
print(popularityExplicit)
print(amountExplicit)

# Create the fig3ure
# fig3 = go.Fig3ure()
fig3 = px.histogram(data, x="popularity", color="explicit")
# Update the layout for titles, labels, and legend
fig3.update_layout(
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
# Show the plot
fig3.show()