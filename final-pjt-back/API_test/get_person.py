import requests
from pprint import pprint


def get_person():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/person/'
    person_list = []
    params = {
        'api_key': '1b05dc44579ab8b52d94ac2f4e057d63',
        'language': 'ko',
    }
    for person_id in range(1000):
        response = requests.get(BASE_URL + path + f'/{person_id}', params=params)
        person_info = response.json()
        person_list.append(person_info)

    return person_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_person())
