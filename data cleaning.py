'''

This is the raw_data cleaning script.
Here I get data for only needed genres and columns.
I also convert the duration from ms to mm:ss format.
And add some columns for the data that I will get from Spotify API.

The most important part of this script is to remove duplicates and null values.
As the dataset is big and may have some of duplicates and null values.

Then dataset from here is used in the parser.py file to add the images, release date, spotify url and album type to rows.
'''

# import libraries
import pandas as pd

# Get the dataset to work with
dataFrame = pd.read_csv("raw_data.csv")
print("Raw Data Info:")
print(dataFrame.info())


# Check for missing values
print("Missing Values:\n", dataFrame.isnull().sum(),"\n")

#genres I need
desired_values = ["alt-rock", "alternative","black-metal", "death-metal", "emo", "funk", "garage", "goth", "grindcore", "groove", "grunge", "hard-rock", "heavy-metal", "industrial", "j-rock", "metal", "metalcore", "psych-rock", "punk", "punk-rock", "rock", "rock-n-roll"]

# checks for duplicates and null values and removes rows with them
def remove_and_check_duplicates_null():
    global dataFrame

    initial_len = len(dataFrame)
    dataFrame = dataFrame.drop_duplicates()
    dataFrame = dataFrame.drop_duplicates(subset='track_id', keep="first")
    print(len(dataFrame))
    dataFrame = dataFrame.dropna()
    print(len(dataFrame))
    if(initial_len > len(dataFrame)):
        print(f"{initial_len-len(dataFrame)} duplicates are removed\n")
    else:
        print("There's no duplicates\n")


#converts ms to mm:ss format
def duration_standartization(ms):
    seconds = ms // 1000  
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"  # Format as mm:ss



# cleaning the data
remove_and_check_duplicates_null()

# I guess alt-rock is the same as alternative so I will standartize it
dataFrame.loc[dataFrame["track_genre"] == "alt-rock", "track_genre"] = "alternative"

# Apply the conversion function to the column
dataFrame['duration_mm/ss'] = dataFrame['duration_ms'].apply(duration_standartization)
dataFrame["loudness"] = dataFrame["loudness"].apply(lambda x: abs(x))
dataFrame["image_url"] = ""
dataFrame["release_date"] = ""
dataFrame["spotify_url"] = ""
dataFrame["album_type"] = ""



dataFrame = dataFrame[dataFrame['track_genre'].isin(desired_values)]

# deleting not needed data
dataFrame = dataFrame.drop("mode", axis=1)
dataFrame = dataFrame.drop("time_signature", axis=1)
dataFrame = dataFrame.drop("acousticness", axis=1)
dataFrame = dataFrame.drop("valence", axis=1)
dataFrame = dataFrame.drop("instrumentalness", axis=1)
# dataFrame = dataFrame.drop("speechiness", axis=1)
# dataFrame = dataFrame.drop("liveness", axis=1)
# dataFrame = dataFrame.drop("loudness", axis=1)
dataFrame = dataFrame.drop("key", axis=1)


# print dataFrame info
print("Cleaned Data Info:")
print(dataFrame)

dataFrame.to_csv("cleaned_dataset.csv", sep=',', index=False, encoding='utf-8')