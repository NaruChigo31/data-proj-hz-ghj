# importing the necessary libraries
import pandas as pd
from spoti_test import *
from time import sleep
import ast  

dataFrame = pd.read_csv("cleaned_and_parsed_dataset2.csv")
dataFrame = dataFrame.drop_duplicates(subset='track_id', keep="first")

track_id_list = dataFrame["track_id"].tolist()
# print(track_id_list)
# dataFrame.to_csv("asdasdasd_dataset.csv", sep=',', index=False, encoding='utf-8')
# print(len(track_id_list),len(dataFrame["track_id"].tolist()))
counter = 0
# print(constant_len)

# actual_track_id_list = track_id_list
actual_track_id_list = []
listFile = open("list.txt", "r")
actual_track_id_list = ast.literal_eval(listFile.read())
listFile.close()
# listFile = open("list.txt", "w")
# listFile.write(f"{track_id_list}")
# listFile.close()
constant_len = len(actual_track_id_list)
temp_id_list = actual_track_id_list

def getData(formula, token):
    row_number = dataFrame.index.get_loc(dataFrame[dataFrame['track_id'] == f"{actual_track_id_list[formula]}"].index[0])
    print("hkjhkj",row_number)
    song = get_song(token, actual_track_id_list[formula])
    # print(song["album"])
    print("hkjh",song["popularity"])
    if dataFrame.loc[row_number, 'popularity'] != song["popularity"]:
        print("huiiiiiiiiiiiiii")
        song_popularity = song["popularity"]
        print(dataFrame.loc[row_number, 'popularity'], "huiTam - ",song_popularity)
        dataFrame.loc[row_number, 'popularity'] = song_popularity
        return f"app {row_number}: {song_popularity}"
    print("huiiiiiiiiiiiiii2")

for i in range(constant_len):
    try:
        print("i",i)
        a11 = getData(i,token1)
        # a21 = getData(2*i+3,token2)

        # print(a11)
        # print(a21)
        # print(a31)
        # print(a41)
        dataFrame.to_csv("cleaned_and_parsed_dataset2.csv", sep=',', index=False, encoding='utf-8')
        print("track_id_list",actual_track_id_list[i])
        print("jkhkj",actual_track_id_list[i])
        temp_id_list.remove(actual_track_id_list[i])
        print("counter", counter)
        # temp_id_list.remove(actual_track_id_list[2*i+1])

        counter += 1
        sleep(1)
        listFile = open("list.txt", "w")
        listFile.write(f"{temp_id_list}")
        listFile.close()
    except Exception as e:
        print("actual_track_id_list",len(actual_track_id_list))
        # print(actual_track_id_list[2*i+1])
        print("hhuuuuuuuui", e)
        break