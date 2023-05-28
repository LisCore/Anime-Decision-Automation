import requests
from requests import Session
import json
from pprint import pprint as pp

'''
anime_info = 'One Piece'
api_load = 'https://api.jikan.moe/v4/anime'
query_params = {
    'title': anime_info,
    'moreinfo': 'rating'
}

response = requests.get(
    api_load,
    query_params
)
'''


class ANIME:
    def __init__(self):
        self.api_url = 'https://api.jikan.moe'
        self.query_params = {'title': ""}
        self.session = Session()
        self.session.headers.update(self.query_params)

    def get_all_anime(self):
        url = self.api_url + '/v4/anime'
        r = self.session.get(url)
        data = r.json()['data']
        return data

    def get_info(self, anime_title):
        url = self.api_url + '/v4/anime'
        parameters = {'letter': anime_title}
        r = self.session.get(url, params=parameters)
        if r.status_code == 200:
            data = r.json()
            with open('response.json', 'w') as fileManager:
                fileManager.write(json.dumps(r.json(), indent=4))
            return data

        return r.status_code

'''
anime = ANIME()
# pp(anime.get_all_anime())
pp(anime.get_info(anime_info))

anime = ANIME()
anime_info = 'Naruto'
pp(anime.get_info(anime_info))
'''

'''
        anime_list = []
        while anime_list != 5:
            anime_return = data['data']
            if not (anime in anime_list):
                anime_list.append(anime)

        return anime_list
'''
