import pandas as pd

# Load the CSV file
df = pd.read_csv("cleaned_and_parsed_dataset.csv")

# average popularity of each genre 
avgTable = df.groupby('track_genre')['popularity'].mean()
print(avgTable)
# Save the result to a new CSV file if needed
avgTable.to_csv('average_popularity_by_genre.csv')