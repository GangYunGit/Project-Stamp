<template>
  <div style="background-color: #BDFCFE; height:fit-content">
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }" style="text-decoration: none; color: black;">Home</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'BookView' }" style="text-decoration: none; color: black;">Album</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'InitialLogin' }" style="text-decoration: none; color: black;">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
    <div class='p-4' style="background-color:#BDFCFE;">
      <div class="mx-auto mt-2 p-2 col-sm-8 col-lg-4 col-md-6" style="background-color:#FBFEAB;">
        <b-card
        class="mb-2 rounded-3 mx-auto"
        :title="movie?.title"
        :img-src="`https://image.tmdb.org/t/p/original/${movie?.poster_path}`"
        img-alt="Poster Image"
        img-top
        img-height="650px"
        style="height: 50%"
        img-width="60%"
      >
        <b-card-text>
          <p>{{ genres }}</p>
          <b-icon icon="star" class="border-warning"></b-icon>
          {{ movie.vote_average }}
          <br>
          {{ movie?.overview }}
        </b-card-text>
      </b-card>
      <b-button pill variant="#667eea" class="m-2 gradient-custom" @click="addToAlbum">앨범에 추가하기</b-button>
      <b-button pill variant="outline-secondary" class="m-2" @click="goBack">돌아가기</b-button>
      <b-button class='m-2' pill variant="primary" @click="getRecommend">영화 추천받기</b-button>
      </div>
    </div>
  </div>
</template>

<script>
// bootstrap, axios 관련 라이브러리
// @ is an alias to /src
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

// API_URL = "http://127.0.0.1:8000/"
const API_URL = 'http://localhost:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: this.$store.state.temp,
      genres: '',
    }
  },
  created() {
    this.getMovieDetail()
    this.getGenreList()
    // console.log(this.movie)
  },
  updated() {
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    // notAdded() {
    //   const albumSrc = this.$store.state.albums
    //   const thisTitle = this.movie.title
    //   // console.log(albumSrc)
    //   console.log(this.movie.title)
    //   for (const album of albumSrc) {
    //     if (thisTitle === album.movie_title) {
    //     // console.log(true)
    //     return true
    //     }
    //   }
    //   return false
    // }
  },
  methods: {
    // 페이지를 열 때 영화 상세 정보 조회
    getMovieDetail() {
      for (const part of this.movies) {
        if (part.id === this.$route.params.id) {
          this.movie = part
          this.$store.dispatch('detailTemp', part)
          break
        }
      }
    },

    // 앨범에 이 영화를 추가
    addToAlbum() {
      const albumSrc = this.$store.state.albums
      const thisMovie = this.movie
      let quit = false

      // console.log(albumSrc)
      // console.log(thisMovie.title)
      for (const album of albumSrc) {
        // console.log(album.movie_title)
        if (thisMovie.title === album.movie_title) {
          quit = true
          alert('이미 추가된 영화입니다.')
          }
        }
        if (quit === false) {
          axios({
          method: 'post',
          url: `${API_URL}/albums/`,
          data: {
            // pk: movieData.pk,
            user: this.$store.state.user_pk,
            movie_poster_path: this.movie.poster_path,
            movie_title: this.movie.title,
            content: null,
            // review: '',
          },
        })
        .then((response) =>{
          // console.log(response)
          this.$store.commit('ADD_ALBUM', response.data)
          alert('앨범에 추가되었습니다.')
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    // 추천 영화 조회(TMDB)
    getRecommend() {
      const movieId = this.$route.params.id
      this.$store.dispatch('getRecommendByTMDB', movieId)
    },

    // 이전 페이지로 돌아가기
    goBack() {
      this.$router.go(-1)
    },

    // 장르 이름 가져오기
    getGenreList() {
      axios({
        method: 'get',
        url: "http://localhost:8000/movies/genres",
      })
      .then((response) => {
        let payload = ''
        const genreIdList = response.data
        // console.log(genreIdList)
        for (const genre of this.movie.genre_ids) {
          const genreName = genreIdList.filter(genreInfo => {
            if (genre === genreInfo.id) {
              return genreInfo.name
            }
          })
          payload = payload + genreName[0].name + ','
        }
        const sortedPayload = payload.slice(0, payload.length-1)
        this.genres = sortedPayload
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
}
</script>

<style>

</style>