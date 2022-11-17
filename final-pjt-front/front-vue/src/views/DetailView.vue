<template>
  <div>
    <h2>상세 설명</h2>
    <b-button @click="addAlbum" class="m-2">앨범에 추가</b-button>
    <b-button @click="getRecommend" class="m-2">영화 추천 받기</b-button>
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
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
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