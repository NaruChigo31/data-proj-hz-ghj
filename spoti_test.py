# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
import base64
from requests import post, get 
import json

client_id = []
client_secret = []

tokens = []
def get_token():
    for i in range(len(client_id)):
        print(i)
        auth_str = client_id[i]+":"+client_secret[i]
        auth_bytes = auth_str.encode("utf-8")
        auth64 = str(base64.b64encode(auth_bytes),"utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials"
        }

        result = post(url, headers=headers, data=data)
        json_res = json.loads(result.content)
        token = json_res["access_token"]
        tokens.append(token)
    return tokens

# def get_token():
#     auth_str = client_id+":"+client_secret
#     auth_bytes = auth_str.encode("utf-8")
#     auth64 = str(base64.b64encode(auth_bytes),"utf-8")

#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Authorization": "Basic " + auth64,
#         "Content-Type": "application/x-www-form-urlencoded"
#     }
#     data = {
#         "grant_type": "client_credentials"
#     }

#     result = post(url, headers=headers, data=data)
#     json_res = json.loads(result.content)
#     token = json_res["access_token"]
#     return token

def get_auth_header(token):
    return {"Authorization": "Bearer "+ token}

def get_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    qeury = f"?q={artist_name}&type=artist&limit=1"

    qeury_url = url+ qeury
    res = get(qeury_url, headers=headers)
    json_res = json.loads(res.content)["artists"]["items"]
    if len(json_res) ==0:
        print("No artist")
        return None
    else:
        return json_res[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = get_auth_header(token)
    res = get(url, headers=headers)
    json_res = json.loads(res.content)["tracks"]
    return json_res


def get_song(token, id):
    url = f"https://api.spotify.com/v1/tracks/{id}"
    headers = get_auth_header(token)
    res = get(url, headers=headers)
    json_res = json.loads(res.content)
    return json_res

tokens = get_token()

token1 = tokens[0]
token2 = tokens[1]
token3 = tokens[2]
token4 = tokens[3]
# artist = get_artist(token, "Полматери")
# artist_id = artist["id"]
# print(artist["name"])
# songs = get_songs_by_artist(token, artist_id)
# print(songs)

# song = get_song(token1, "1pF5SqpGCz8tHh0MR88Tg4")
# print(json.dumps(song, indent=2))
# print(song["popularity"])


# for i in song:
    # print(i)
    # continue

# print(token)
