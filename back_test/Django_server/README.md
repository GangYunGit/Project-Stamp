# PJT 08

## 이번 pjt 를 통해 배운 내용

- AJAX를 이용하여 팔로우, 좋아요 기능을 구현하는 방법을 익혔다.

- views.py에서 특정한 쿼리 셋을 가져올 알고리즘을 구현하는 방법을 배웠다.

---

## A. 유저 팔로우 기능

> 요구사항

- 프로필 페이지에 `팔로워 수`와 `팔로잉 수`를 표시

- 프로필 페이지에 해당 사용자를 팔로우 할 수 있는 버튼 표시

- 인증된 사용자만 다른 사용자를 팔로우 할 수 있으며, 사용자는 자기 자신을 팔로우 할 수 없음

- 팔로우 버튼 클릭 시, `AJAX 통신`을 이용하여 서버에서 JSON 데이터를 받아와 화면을 구성

> 어려웠던 부분

- 원래 동기 방식으로 팔로우 기능을 구현했었지만, 이를 비동기 방식으로 바꾸려고 하니 생각보다 바꿔야할 부분이 많았다.

- 특히 script코드를 작성할 때 자동완성 기능을 쓰지 못해서 오타를 수정하기가 매우 힘들었다.
  - 마니또가 디버깅을 도와주었다.

- script코드에서 `팔로워, 팔로잉 수 count`을 쓰고 싶은데 어떻게 했었는지 기억이 잘 나지 않았다. 예전에 hws에서 작성해 놓은 코드를 참고해보니, view함수에서 orm으로 쿼리셋을 가공하여 템플릿으로 넘겨주는 방법으로 이를 해결할 수 있었다. 

> 핵심 코드

- accounts/profile.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}의 프로필 페이지</h1>
  {% with followings=person.followings.all followers=person.followers.all %}
    <div>
      <div>
        팔로워 : <span id="followers-count">{{ followers|length }}</span> /
        팔로잉 : <span id="followings-count">{{ followings|length }}</span> 
      </div>
      {% if user != person %}
        <div>
          <form id="follow-form" data-user-id="{{ person.pk }}">
            {% csrf_token %}
            {% if user in followers %}
              <button id="followBtn">언팔로우</button>
            {% else %}
              <button id="followBtn">팔로우</button>
            {% endif %}
          </form>
        </div>
      {% endif %}
    </div>
  {% endwith %}
{% endblock %}

{% block script %}
<script>
  const form = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`,
      headers: {'X-CSRFToken': csrftoken,}
    })
    .then((response) => {
      const isFollowed = response.data.is_followed
      const followButton = document.querySelector('#followBtn')
      const followersCount = response.data.followers_count
      const followingsCount = response.data.followings_count
      if (isFollowed) {
        followButton.innerText = '언팔로우'
      } else {
        followButton.innerText = '팔로우'
      }
      
      const followersCountTag = document.querySelector('#followers-count')
      const followingsCountTag = document.querySelector('#followings-count')
      followersCountTag.innerText = followersCount
      followingsCountTag.innerText = followingsCount
    })
    .catch((error) => {
      console.log(error.response)
    })
  })
</script>
{% endblock script %}
```

- accounts/views.py의 follow 함수

```python
from django.http import JsonResponse
...

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if user != person:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                is_followed = False
            else:
                person.followers.add(user)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': person.followers.count(),
                'followings_count': person.followings.count(),
            }
            return JsonResponse(context)

        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

> 결과 사진

- 다른 사람의 프로필 페이지

![image](https://user-images.githubusercontent.com/109258306/199910577-ffb2a9db-d13d-4814-a1b6-495b514bae92.png)

- 자신의 프로필 페이지

![image](https://user-images.githubusercontent.com/109258306/199910735-fb9e247a-3f64-4d0f-99e7-ea94713b1896.png)

---

## B. 리뷰 좋아요 기능

> 요구사항

- 전체 리뷰 목록 조회 페이지에 `좋아요 버튼`과 `좋아요 개수` 표시

- 이미 좋아요 버튼을 누른 경우 `좋아요 취소 버튼`을 표시

- 인증된 사용자만 리뷰에 좋아요 가능

- 좋아요 클릭 시, `AJAX 통신`을 이용하여 서버에서 JSON 데이터를 받아와 화면을 구성

> 어려웠던 부분

- 팔로우 기능과 비슷한 방법으로 구현하면 될 것 같았지만, 생각보다 쉽지 않았다

- 특히 좋아요를 누른 사람 수를 view함수에서 likes_count라는 변수에 할당하여 가져오려고 했는데, 변수가 초기화 되는 위치가 좋아요가 눌리기 이전 시점으로 되어있어서 계속 좋아요와 좋아요 취소가 반대로 적용되는 현상이 있었다. 이 역시 hws에 작성된 코드를 보고 고쳤다.

> 핵심 코드

- community/index.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Community</h1>
  <hr>
  {% for review in reviews %}
    <p>작성자 : <a href="{% url 'accounts:profile' review.user.username %}">{{ review.user }}</a></p>
    <p>글 번호: {{ review.pk }}</p>
    <p>글 제목: {{ review.title }}</p>
    <p>글 내용: {{ review.content }}</p>
    {% if request.user.is_authenticated %}
      <form class="like-forms" data-review-id="{{ review.pk }}">
        {% if user in review.like_users.all %}
          <button id="like-button-{{ review.pk }}">좋아요 취소</button>
        {% else %}
          <button id="like-button-{{ review.pk }}">좋아요</button>
        {% endif %}
      </form>
    {% endif %}
    <p>
      <span id="review-like-{{ review.pk }}">{{ review.like_users.count }}</span> 명이 이 글을 좋아합니다.
    </p>
    <a href="{% url 'community:detail' review.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}

{% block script %}
<script>
  const forms = document.querySelectorAll('.like-forms')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  forms.forEach((form) => {
    form.addEventListener('submit', function (event) {
      event.preventDefault()
      const reviewId = event.target.dataset.reviewId
      axios({
        method: 'post',
        url: `/community/${reviewId}/like/`,
        headers: {'X-CSRFToken': csrftoken,}
      })
      .then((response) => {
        const isLiked = response.data.is_liked
        const likesCount = response.data.likes_count
        const likeBtnTag = document.querySelector(`#like-button-${reviewId}`)
        const likeCountTag = document.querySelector(`#review-like-${reviewId}`)
        if (response.data.is_authenticated) {
          const reviewId = event.target.dataset.reviewId
          if (isLiked === true) {
            likeCountTag.innerText = likesCount
            likeBtnTag.innerText = '좋아요 취소'
          } else {
            likeCountTag.innerText = likesCount
            likeBtnTag.innerText = '좋아요'
          }
        }
      })
      .catch((error) => {
        console.log('에러')
      })
    })
  })
</script>
{% endblock script %}
```

- community/views.py

```python
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


@require_GET
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user
        
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False
        else:
            review.like_users.add(user)
            is_liked = True

        likes_count = review.like_users.count()  
        context = {
            'is_liked': is_liked,
            'likes_count': likes_count,
            'is_authenticated': request.user.is_authenticated,
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

> 결과 사진

- 리뷰 목록 조회 페이지

![image](https://user-images.githubusercontent.com/109258306/199910920-a4c99b37-0c7a-445d-b586-c7280a27fac1.png)


---

## C. Movie 앱 기능

> 요구사항

1. 전체 영화 목록 조회(index)

- 사용자의 인증 여부와 관계없이 `전체 영화 목록 조회 페이지`에서 적절한 UI를 활용하여 영화 목록을 제공

2. 단일 영화 상세 조회(detail)

- 사용자의 인증 여부와 관계없이 `단일 영화 상세 조회 페이지`에서 적절한 UI를 활용하여 영화 정보를 제공

3. `영화 추천 기능(recommended)`

- 사용자가 인증되어 있다면, 적절한 알고리즘을 활용하여 10개의 영화를 추천하여 제공

> **사용한 알고리즘**

  - 파이썬의 random.sample함수를 이용한다. 우선 1부터 100까지의 영화 id를 랜덤하게 10개 씩 뽑아서 리스트를 만들고 orm의 filter method를 이용하여 뽑아 놓은 10개의 영화 id와 일치하는 query set만 가져와 'movies' 변수에 저장하고, context를 통해 template에 넘겨준다.

- recommended 핵심 코드
  
```python
from django.views.decorators.http import require_safe

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
```

> 어려웠던 부분

- 단순히 모든 쿼리셋을 받아와서 random.sample로 뽑아낸 요소들을 리스트에 담아서 출력하면 될 줄 알았지만, template에 context로 넘겨주려면 list형이 아니라 `QuerySet으로만` 넘겨주어야 에러가 발생하지 않았다. orm의 filter 메서드를 이용하여 이를 해결하였다.

> 핵심 코드

- movies/index.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Movies</h1>
  <a href="{% url 'movies:recommended' %}">영화 추천받기!!</a>
  <hr>
  {% for movie in movies %}
    <p>제목 : <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p>
    <p>장르 : 
      <span>
        {% for genre in movie.genres.all %}
        *{{ genre.name }} 
        {% endfor %}
      </span>
    </p>
    <p>평점 : {{ movie.vote_average }}</p>
    <hr>
  {% endfor %}
{% endblock %}
```

- movies/detail.html

```html
{% extends 'base.html' %}

{% block content %}
<h1>Movie Detail</h1>
<hr>
<h2>{{ movie.title }}</h2>
<p>출시일 : {{ movie.release_date }}</p>
<img src="{{ movie.poster_path }}" alt="img" width="200px">
<p>인기도 : {{ movie.popularity }}</p>
<p>관객 : {{ movie.vote_count }}명</p>
<p>평점 : {{ movie.vote_average }}</p>
<p>줄거리 : {{ movie.overview }}</p>
<p>장르 : 
  <span>
    {% for genre in movie.genres.all %}
      {{ genre.name }}
    {% endfor %}
  </span>
</p>
{% endblock %}
```

- movies/recommended.html

```html
{% extends 'base.html' %}

{% block content %}
  <br>
  <h1>이런 영화는 어때요?</h1>
  <hr>
  {% if request.user.is_authenticated %}
    {% for movie in recommended_movies %}
      <p>제목 : <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p>
      <p>장르 : 
        <span>
          {% for genre in movie.genres.all %}
          *{{ genre.name }} 
          {% endfor %}
        </span>
      </p>
      <p>평점 : {{ movie.vote_average }}</p>
      <hr>
    {% endfor %}
  {% endif %}
{% endblock %}
```


- movies/views.py

```python
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from .models import Movie, Genre
import random

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
    
```

> 결과 사진

- movies/index.html

![image](https://user-images.githubusercontent.com/109258306/199913148-793f91e6-750b-451c-aa6f-9642a146682f.png)

- movies/detail.html

![image](https://user-images.githubusercontent.com/109258306/199913879-3a8aef7d-4c3b-4ce0-a8aa-445c8639d719.png)

- movies/recommended.html

![image](https://user-images.githubusercontent.com/109258306/199914392-348af838-c7b3-40ee-b83a-fd7bfdc67536.png)

---

# 후기

- 이전 프로젝트에서는 팔로우나 좋아요 버튼을 누르면 페이지가 자동으로 새로고침되어 매우 불편했지만 AJAX 비동기 통신을 이용하여 새로고침 없이 해당 페이지의 필요한 부분만 바꿔줌으로써 UX가 향상되었다.

- 알고리즘을 잘 짜서 상황에 맞는 데이터를 잘 가져오는 것도 중요한 작업임을 깨달았다.

- 알고리즘을 잘 짜려면 orm이나 쿼리문을 통해 데이터를 어떻게 조회할 것인지가 중요하다는 것을 알게 되었다.