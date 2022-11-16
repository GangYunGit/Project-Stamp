from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie
import random
import requests
from pprint import pprint

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)
    


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
    

@require_safe
def recommended(request):
    if request.user.is_authenticated:
        max_id = Movie.objects.count()
        recommended_movies = Movie.objects.filter(id__in=random.sample(range(1, max_id + 1), 10))
        context = {
            'recommended_movies': recommended_movies,
        }
        return render(request, 'movies/recommended.html', context)
    return redirect('accounts:login')


# def get_movies():
#     BASE_URL = 'https://api.themoviedb.org/3'
#     path = '/movie/'
#     movie_list = []
#     params = {
#         'api_key': '1b05dc44579ab8b52d94ac2f4e057d63',
#         'language': 'ko',
#     }
#     for movie_id in range(550, 551):
#         response = requests.get(BASE_URL + path + f'/{movie_id}', params=params)
#         movie_info = response.json()
#         movie_list.append(movie_info)

#     return movie_list


# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     """
#     popular 영화목록중 vote_average가 8 이상인 영화목록 반환
#     (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
#     """
#     pprint(get_movies())
