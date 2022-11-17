<template>
  <div>
    <b-col>
    <b-card
      class="mb-2"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
      img-alt="Poster Image"
      img-top
      style="width: 25rem"
    >
      <b-card-text>
        {{ movie.overview }}
      </b-card-text>
    </b-card>
  </b-col>
  <b-button @click="addAlbum">앨범에 추가</b-button>
  <b-button @click="getRecommend">다른 영화 보기</b-button>
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
const API_URL = process.env.VUE_APP_API_KEY

export default {
  name: 'DetailView',
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getRecommendMovies()
  },
  // methods는 추가 작업 필요할 수 있음
  methods: {
    getRecommendMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/` ,
      })
      .then((response) => {
        console.log(response)
        // 데이터 타입에 따라 this.movie에 저장할 정보 결정
        // this.movie = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    },
    addAlbum() {

    },
    getRecommend() {

    },
  },
}
</script>

<style>

</style>