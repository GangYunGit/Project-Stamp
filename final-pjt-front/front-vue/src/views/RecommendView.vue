<template>
  <div style="background-color: #BDFCFE;">
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }" style="text-decoration: none; color: black;">Home</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'BookView' }" style="text-decoration: none; color: black;">Album</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'InitialLogin' }" style="text-decoration: none; color: black;">Recommended</router-link></b-nav-item>

      </b-nav>
    </div>
    <div class="p-4" style="background-color:#BDFCFE;">
      <div class="mx-auto mt-3 p-3 col-sm-8 col-lg-4 col-md-6" style="background-color:#FBFEAB">
        <b-card
          class="mb-2 rounded-3 mx-auto m-2 p-2"
          :title="movie.title"
          :img-src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
          img-alt="Poster Image"
          img-top
          img-height="60%"
          img-width="60%"
        >
          <b-card-text>
            {{ movie.overview }}
          </b-card-text>
        </b-card>
        <b-button pill variant="#667eea" class="m-2 gradient-custom" @click="addToAlbum">앨범에 추가하기</b-button>
        <b-button @click="goBack" pill variant="outline-warning" class="m-2">뒤로</b-button>
        <b-button pill variant="outline-secondary" class="m-2" @click="getAnother">다른 영화 보기</b-button>
      </div>
    </div>
  </div>
</template>

<script>
// bootstrap, axios 관련 라이브러리
// @ is an alias to /src
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import _ from 'lodash'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

// API_URL = "http://127.0.0.1:8000/"
const API_URL = 'http://localhost:8000'
// const VUE_APP_TMDB = process.env.VUE_APP_TMDB

export default {
  name: 'RecommendView',
  data() {
    return {
      movie: [],
      index: 0
    }
  },
  created() {
    this.getRecommend()
  },
  computed: {
  },
  methods: {
    // vuex에 저장된 추천 작품 가져오기
    getRecommend() {
      const recommendSrc = this.$store.state.recommended
      if (recommendSrc.length > 1) {
        this.movie = _.sample(recommendSrc)
      } else {
        this.movie = recommendSrc
      }
    },

    // (다른 영화 추천받기 버튼을 클릭한 경우) 목록의 다른 영화 보여주기
    getAnother() {
      if (this.$store.state.recommended.length === 1) {
        const mvId = this.$route.params.id
        this.$store.dispatch('getRecommendByTMDB', mvId)
      }

      const shuffle = this.$store.state.recommended
      this.movie = _.sample(shuffle)
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

    // 뒤로 가기 버튼 작동
    goBack() {
      this.$router.go(-1)
    },
  },
}
</script>

<style>
.gradient-custom {
  background: #667eea;
  background: -webkit-linear-gradient(to right, rgba(102, 126, 234, 0.5), rgba(118, 75, 162, 0.5));
  background: linear-gradient(to right, rgba(102, 126, 234, 0.5), rgba(118, 75, 162, 0.5))
}
</style>
