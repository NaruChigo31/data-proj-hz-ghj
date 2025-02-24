# importing the necessary libraries
import pandas as pd
from spoti_test import *
from time import sleep
import math

dataFrame = pd.read_csv("cleaned_dataset.csv")
dataFrame = dataFrame.drop_duplicates(subset='track_id', keep="first")

print(dataFrame)
id_image_dataFrame = dataFrame[["track_id","image_url"]]

id_image_dataFrame = id_image_dataFrame.loc[id_image_dataFrame.index.difference(id_image_dataFrame.dropna().index)]
# print(id_image_dataFrame)
track_id_list = id_image_dataFrame["track_id"].tolist()
# print(len(track_id_list))
id_image_dataFrame.to_csv("asdasdasd_dataset.csv", sep=',', index=False, encoding='utf-8')
# print(len(track_id_list),len(dataFrame["track_id"].tolist()))

counter = 0
for i in track_id_list:
    row_number = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{i}"].index[0])
    song = get_song(token1, i)
    # if counter > 1000:
    if type(dataFrame.loc[row_number, 'image_url']) != str or type(dataFrame.loc[row_number, 'release_date']) != str or type(dataFrame.loc[row_number, 'spotify_url']) != str or type(dataFrame.loc[row_number, 'album_type']) != str:
        song_image_url = song["album"]["images"][1]["url"]
        song_release_date = song["album"]["release_date"]
        song_spotify_url = song["external_urls"]["spotify"]
        song_album_type = song["album"]["album_type"]

        print(row_number)
        dataFrame.loc[row_number, 'image_url'] = song_image_url
        dataFrame.loc[row_number, 'release_date'] = song_release_date
        dataFrame.loc[row_number, 'spotify_url'] = song_spotify_url
        dataFrame.loc[row_number, 'album_type'] = song_album_type
        dataFrame.to_csv("cleaned_and_parsed_dataset.csv", sep=',', index=False, encoding='utf-8')
        print("a",song_image_url)
        print("counter", counter)
    counter += 1
    sleep(1)