import requests
import json
import re


class URLMaker:
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_movie_url(self, category='movie', feature='popular', page='1'):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'
        return url

    def get_all_movie_url(self, movie_id):
        url = f'{self.url}/movie/{movie_id}?api_key={self.key}&language=ko-KR'
        return url

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None

    def get_genre_url(self):
        url = f'{self.url}/genre/movie/list?api_key={self.key}'
        return url

    def get_actor_url(self, page='1'):
        url = f'{self.url}/person/popular/?api_key={self.key}&language=ko-KR&page={str(page)}'
        return url

    def actor_name_url(self, person_id):
        url = f'{self.url}/person/{person_id}?api_key={self.key}&language=ko-KR'
        return url

    # def get_movie_cast_url(self, movie_id):
    #     url = f'{self.url}/movie/{movie_id}/credits?api_key={self.key}'
    #     return url


TMDB_KEY = '1b05dc44579ab8b52d94ac2f4e057d63'
url = URLMaker(TMDB_KEY)


def is_korean_name(name):
    korean_name = re.compile('[가-힣]').findall(name)
    if korean_name:
        return True
    else:
        return False


# def create_genre_data():
#     genre_url = url.get_genre_url()
#     raw_data = requests.get(genre_url)
#     json_data = raw_data.json()
#     genres = json_data.get('genres')

#     genre_data = []

#     for genre in genres:
#         tmp = {
#             'model': 'movies.genre',
#             'pk': genre['id'],
#             'fields': {'name': genre['name'], 'like_users': []},
#         }
#         genre_data.append(tmp)

#     with open('genres.json', 'w') as f:
#         json.dump(genre_data, f, indent=4)


# def create_movie_data():
#     with open('genres.json', 'r+') as f:
#         movie_data = json.load(f)

#     for page in range(1, 20):
#         raw_data = requests.get(url.get_movie_url(page=page))
#         json_data = raw_data.json()
#         movies = json_data.get('results')

#         for movie in movies:
#             if movie.get('release_date') == "" or movie.get('poster_path') == "":
#                 continue

#             movie.pop('adult')
#             movie.pop('original_language')
#             movie.pop('original_title')
#             movie.pop('popularity')
#             movie.pop('backdrop_path')
#             movie.pop('video')
#             movie['like_users'] = []
#             tmp = {
#                 'model': 'movies.movie',
#                 'pk': movie.pop('id'),
#                 'fields': movie,
#             }
#             movie_data.append(tmp)

#     with open('movies.json', 'w') as f:
#         json.dump(movie_data, f, indent=4)


def create_actor_data():
    actors = []
    for page in range(1, 9):
        raw_data = requests.get(url.get_actor_url(page=page))
        json_data = raw_data.json()
        actor_data = json_data.get('results')

        for actor in actor_data:
            person_id = actor.get('id')
            raw_person_data = requests.get(url.actor_name_url(person_id=person_id))
            person_name = raw_person_data.json().get('name')
            person_names_data = raw_person_data.json().get('also_known_as')
            person_profile_path = raw_person_data.json().get('profile_path')

            filmo = []
            known_for_data = actor.get('known_for')
            for known_for in known_for_data:
                movie_id = known_for.get('title')
                filmo.append(movie_id)

            for i in range(len(person_names_data)):
                if is_korean_name(person_names_data[i]):
                    person_name = person_names_data[i]
                    break

            print(person_name, filmo)

            tmp = {
                'model': 'movies.actor',
                'pk': person_id,
                'fields': {
                    'name': person_name,
                    'profile_path': person_profile_path,
                    'movie_ids': filmo,
                    'like_users': [],
                },
            }
            actors.append(tmp)

    with open('actors.json', 'w') as f:
        json.dump(actors, f, indent=4)


# create_genre_data()
# create_movie_data()
create_actor_data()
