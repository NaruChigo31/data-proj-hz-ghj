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
# print(len(track_id_list))
id_image_dataFrame.to_csv("asdasdasd_dataset.csv", sep=',', index=False, encoding='utf-8')
# print(len(track_id_list),len(dataFrame["track_id"].tolist()))
constant_len = len(track_id_list)
counter = 0
for i in range(constant_len):
    print(i)
    row_number1 = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{track_id_list[2*i]}"].index[0])
    row_number2 = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{track_id_list[2*i+1]}"].index[0])
    row_number3 = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{track_id_list[constant_len-(2*i)-2]}"].index[0])
    row_number4 = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{track_id_list[constant_len-(2*i+1)-2]}"].index[0])

    song1 = get_song(token1, track_id_list[2*i])
    song2 = get_song(token2, track_id_list[2*i+1])
    song3 = get_song(token1, track_id_list[constant_len-(2*i)-2])
    song4 = get_song(token2, track_id_list[constant_len-(2*i+1)-2])
    # print(song1)

    # if counter > 1000:
    if type(dataFrame.loc[row_number1, 'image_url']) != str or type(dataFrame.loc[row_number2, 'image_url']) != str or type(dataFrame.loc[row_number3, 'image_url']) != str or type(dataFrame.loc[row_number4, 'image_url']) != str:
        song_image_url1 = song1["album"]["images"][1]["url"]
        song_release_date1 = song1["album"]["release_date"]
        song_spotify_url1 = song1["external_urls"]["spotify"]
        song_album_type1 = song1["album"]["album_type"]

        song_image_url2 = song2["album"]["images"][1]["url"]
        song_release_date2 = song2["album"]["release_date"]
        song_spotify_url2 = song2["external_urls"]["spotify"]
        song_album_type2 = song2["album"]["album_type"]

        song_image_url3 = song3["album"]["images"][1]["url"]
        song_release_date3 = song3["album"]["release_date"]
        song_spotify_url3 = song3["external_urls"]["spotify"]
        song_album_type3 = song3["album"]["album_type"]

        song_image_url4 = song4["album"]["images"][1]["url"]
        song_release_date4 = song4["album"]["release_date"]
        song_spotify_url4 = song4["external_urls"]["spotify"]
        song_album_type4 = song4["album"]["album_type"]

        print(row_number1)
        print(row_number2)
        print(row_number3)
        print(row_number4)

        dataFrame.loc[row_number1, 'image_url'] = song_image_url1
        dataFrame.loc[row_number1, 'release_date'] = song_release_date1
        dataFrame.loc[row_number1, 'spotify_url'] = song_spotify_url1
        dataFrame.loc[row_number1, 'album_type'] = song_album_type1

        dataFrame.loc[row_number2, 'image_url'] = song_image_url2
        dataFrame.loc[row_number2, 'release_date'] = song_release_date2
        dataFrame.loc[row_number2, 'spotify_url'] = song_spotify_url2
        dataFrame.loc[row_number2, 'album_type'] = song_album_type2
        
        dataFrame.loc[row_number3, 'image_url'] = song_image_url3
        dataFrame.loc[row_number3, 'release_date'] = song_release_date3
        dataFrame.loc[row_number3, 'spotify_url'] = song_spotify_url3
        dataFrame.loc[row_number3, 'album_type'] = song_album_type3

        dataFrame.loc[row_number4, 'image_url'] = song_image_url4
        dataFrame.loc[row_number4, 'release_date'] = song_release_date4
        dataFrame.loc[row_number4, 'spotify_url'] = song_spotify_url4
        dataFrame.loc[row_number4, 'album_type'] = song_album_type4

        dataFrame.to_csv("cleaned_and_parsed_dataset.csv", sep=',', index=False, encoding='utf-8')
        print("a1",song_image_url1)
        print("a2",song_image_url2)
        print("a3",song_image_url3)
        print("a4",song_image_url4)
        print("counter", counter)
    counter += 1
    sleep(1)

