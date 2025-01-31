# importing the necessary libraries
import pandas as pd
from spoti_test import *
from time import sleep
import math

dataFrame = pd.read_csv("cleaned_and_parsed_dataset.csv")
dataFrame = dataFrame.drop_duplicates(subset='track_id', keep="first")

print(dataFrame)
id_image_dataFrame = dataFrame[["track_id","image_url"]]

id_image_dataFrame = id_image_dataFrame.loc[id_image_dataFrame.index.difference(id_image_dataFrame.dropna().index)]
# print(id_image_dataFrame)
track_id_list = id_image_dataFrame["track_id"].tolist()
print(track_id_list)
id_image_dataFrame.to_csv("asdasdasd_dataset.csv", sep=',', index=False, encoding='utf-8')
# print(len(track_id_list),len(dataFrame["track_id"].tolist()))
constant_len = len(track_id_list)
counter = 0
print(constant_len)
def getData(formula, token):
    row_number = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{track_id_list[formula]}"].index[0])
    print(row_number)
    song = get_song(token, track_id_list[formula])
    print(song["album"])
    if type(dataFrame.loc[row_number, 'image_url']) != str:
        song_image_url = song["album"]["images"][1]["url"]
        song_release_date = song["album"]["release_date"]
        song_spotify_url = song["external_urls"]["spotify"]
        song_album_type = song["album"]["album_type"]
    dataFrame.loc[row_number, 'image_url'] = song_image_url
    dataFrame.loc[row_number, 'release_date'] = song_release_date
    dataFrame.loc[row_number, 'spotify_url'] = song_spotify_url
    dataFrame.loc[row_number, 'album_type'] = song_album_type
    return f"app {row_number}: {song_image_url}"

for i in range(constant_len):
    a11 = getData(0,token1)
    # a21 = getData(2*i+2,token2)
    # a31 = getData(constant_len-(2*i)-2,token3)
    # a41 = getData(constant_len-(2*i+1)-2,token4)

    print(a11)
    # print(a21)
    # print(a31)
    # print(a41)
    dataFrame.to_csv("cleaned_and_parsed_dataset.csv", sep=',', index=False, encoding='utf-8')
    print("counter", counter)
    counter += 1
    sleep(1)