'''
This script was unexpected thing to do,
as I expected that I won't use some of the columns from dataset.

Therefore I droped them and then parsed some data into final one.
And at the final stage of doing reccomendation system I realized that I need some of the columns that I droped before.
So I decided to merge the datasets and get the final one that I will use for the reccomendation system.

I merged the datasets using 'track_id' as the key and then droped the duplicate columns that came from df2 where df1 already had them.

So when you're gonna be checking how the code works on yourself, 
you could skip this one as it's not necessary to run it, 
unless you already parsed data into dataset and don't have those columns:

1) speachiness
2) liveness
3) loudness

So, that's it :3
'''

# import libraries
import pandas as pd

# Get the dataset to work with
dataFrame1 = pd.read_csv("cleaned_and_parsed_dataset_orig.csv",index_col=0)
dataFrame2 = pd.read_csv("cleaned_dataset.csv", index_col=0)

# Merge datasets using 'track_id' as the key
merged_df = pd.merge(dataFrame1, dataFrame2, on="track_id", how="left", suffixes=("", "_h"))

# Drop duplicate columns that came from df2 where df1 already had them
columns_to_drop = ['artists_h', 'album_name_h', 'track_name_h', 'popularity_h', 
                   'duration_ms_h', 'explicit_h', 'danceability_h', 'energy_h', 
                   'tempo_h', 'track_genre_h', 'duration_mm/ss_h', 'image_url_h', 
                   'release_date_h', 'spotify_url_h', 'album_type_h']
merged_df = merged_df.drop(columns=[col for col in columns_to_drop ])


merged_df.to_csv("cleaned_and_parsed_dataset.csv", sep=',', index=False, encoding='utf-8')

# -------------------------------------------------------------------------------------------------------
# code below must remove the first column of unneeded ids from the prev dataset(not track_id!!!!)
# but it doesn't work and I found another way to do 
# it just buy adding index_col=0 to the read_csv function
# 
# dataFrame1.loc[:, ~dataFrame1.columns.str.contains('^Unnamed')]
#-------------------------------------------------------------------------------------------------------
df = pd.read_csv("cleaned_and_parsed_dataset.csv")
print(df.info())
print(df.head())