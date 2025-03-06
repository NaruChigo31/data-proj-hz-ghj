# import libraries
import pandas as pd

# Get the dataset to work with
dataFrame1 = pd.read_csv("test_dataset.csv",index_col=0)
dataFrame2 = pd.read_csv("h.csv", index_col=0)

dataFrame1.loc[:, ~dataFrame1.columns.str.contains('^Unnamed')]

dataFrame2_2 = dataFrame2.drop(["album_name","artists","album_name","popularity","duration_ms","explicit","danceability","energy","tempo","track_genre","duration_mm/ss","image_url","release_date","spotify_url","album_type"], axis=1)
dataFrame1_2 = dataFrame1.drop(["album_name","artists","album_name","popularity","duration_ms","explicit","danceability","energy","tempo","track_genre","duration_mm/ss","image_url","release_date","spotify_url","album_type"], axis=1)

# result = pd.merge(dataFrame1, dataFrame2, left_index=True, right_index=True)
# pd.concat([dataFrame1, dataFrame2], axis=1, join="inner")



# df_new_1 = dataFrame1(colums={'track_id': 'track_id'})
# ,"loudness","liveness","speechiness"
print(dataFrame2)

dataFrame1.merge(dataFrame2_2, left_on='track_id', right_on='speechiness')

dataFrame1.to_csv("merged.csv", sep=',', index=False, encoding='utf-8')

# dataFrame1.loc[:, ~dataFrame1.columns.str.contains('^Unnamed')]

df = pd.read_csv("merged.csv")
print(df.info())
print(df.head())