import json
import pprint
import spotipy
from spotipy import oauth2
import datetime

#spotifyの認証
client_id = '23297992c5ee4d9ab337855e6a6a4c14'
client_secret = '22401f03003b4adfa3521e0fea7deeb7'

client_credentials_manager = oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#実施日の月取得
month = datetime.date.today().month

if month in (3,4,5):
    season = "spring"
elif month in (6,7,8):
    season = "summer"
elif month in (9,10,11):
    season = "autumn"
elif month in (1,2,12):
    season = "winter"
else:
    print("there is no season.")
    season = "none"

#spotify api 文字列検索
results = spotify.search(q='track:'+season, limit=10,offset=0,market=None)

#曲名(track)IDを取得
id_list = []
for track in results['tracks']['items']:
    id = track['id']
    id_list.append(id)

pprint.pprint(id_list)

#spotifyプレイリスト作成
username = "Eri Imaizumi"
playlist = spotify.user_playlist_create(username, "test_playlist_hpcn")

#features = spotify.audio_features(id_list)
#pprint.pprint(playlist)
