<template>
  <div style="background-color: #BDFCFE;">
    <div style="">
      <b-nav tabs justified>
      <b-nav-item active><router-link :to="{ name: 'HomeView' }">Home</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'BookView' }">Album</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'RecommendView' }">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
  <div class='p-2' style="background-color:#BDFCFE;">
    <div class="mx-auto mt-3 p-3 col-lg-6 col-md-8" style="background-color:#FBFEAB;">
      <b-card
      class="mb-2 rounded-3 mx-auto"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
      img-alt="Poster Image"
      img-top
      style="width: 30rem"
    >
      <b-card-text>
        {{ movie.overview }}
      </b-card-text>
    </b-card>
  <b-button pill variant="#667eea" class="m-2 gradient-custom" @click="addToAlbum">앨범에 추가</b-button>
  <router-link :to="{ name : 'HomeView' }"><b-button pill variant="outline-secondary" class="m-2">메인으로</b-button></router-link>
  <router-link :to="{ name: 'RecommendView' }" class="m-2"><b-button pill variant="primary">영화 추천받기</b-button></router-link>
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
      movie: [],
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    // 페이지를 열 때 영화 상세 정보 조회
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}` ,
      })
      .then((response) => {
        // 데이터 타입에 따라 this.movie에 저장할 정보 결정
        this.movie = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },

    // 앨범에 이 영화를 추가
    addToAlbum() {
      axios({
        method: 'post',
        url: `${API_URL}/albums/`,
        data: {
          // pk: movieData.pk,
          user: this.$store.state.user_pk,
          movie_poster_path: this.movie.poster_path,
          movie_title: this.movie.title,
        },
      })
      .then((response) =>{
        console.log('저장 성공!')
        console.log(response)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  

    // 추천 영화 조회(더미 데이터)
    getRecommend() {

    },
  },
}
</script>

<style>

</style>