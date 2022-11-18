<template>
  <div clas="container m-4 p-4">
    <div class="d-flex justify-content-md-center m-4 p-4">
      <div class="m-4 p-4 col-md-7" style="background-color: skyblue; border-radius: 40px;">
      <HeaderView />
      <br>
      <hr>
      <b-row>
        <b-col align-self="baseline">
          <h3>영화 검색하기</h3>
          <input type="text" v-model="searchInput">
          <b-button class="m-3" variant="outline-primary" @click="searchResult">검색</b-button>
        </b-col>
        <b-col>
          <router-link :to="{ name:'BookView' }"><img src="../assets/album.png" style="width:80px; height:96px;" alt=""></router-link>
          <p>앨범 보기</p>
        </b-col>
      </b-row>
      </div>
      <div class="m-4 p-4 col-md-4">
      </div>
    </div>
    <div class="d-flex justify-content-md-center m-4" style="background-color: #FBFEAB;">
      <MovieListView v-for="(movie, pk) in movies" :key="pk" :movie="movie" />
    </div>
  </div>
</template>

<script>
// Vue 캐러셀 코드(더미 데이터)
// import VueCarousel from 'vue-carousel';
// Vue.use(VueCarousel);

// bootstrap, axios 관련 라이브러리
// @ is an alias to /src
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

import HeaderView from '@/components/HeaderView'
import MovieListView from '@/components/MovieListView.vue'


// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

// API_URL = "http://127.0.0.1:8000/"
const API_URL = process.env.VUE_APP_API_KEY

export default {
  name: 'HomeView',
  components: {
    HeaderView,
    MovieListView,
  },
  data() {
    return {
      // show : 캐러셀 구동에 필요한 데이터
      show: true,
      // searchInput : axios 요청에 보낼 검색어
      searchInput: null,
      
    }
  },
  // 사이트 접속(템플릿 초기화)시 영화 정보 가져오기
  created() {
    this.getMovieData()
  },
  computed: {
    // // getMovieData : 백엔드 서버에 저장된 영화 정보 가져오기
    getMovieData() {
      return this.$store.state.movies
    },
  },
  methods: {
    searchResult() {
      const searchInput = this.searchInput
      axios({
        method:'get',
        url: API_URL,
        params: {
          searchInput,
        }
      })
      .then((request) => {
        console.log(request)
        // 서버에서 받은 영화 정보로 대체
        // this.movies = request.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>