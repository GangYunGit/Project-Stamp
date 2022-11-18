<template>
  <div clas="container m-4 p-4">
    <div class="d-flex justify-content-md-center m-4">
      <div class="p-4 col-md-11" style="background-color: skyblue; border-radius: 40px;">
      <HeaderView />
      <hr>
      <b-row>
        <b-col align-self="baseline" class="col-md-8">
          <h3>영화 검색하기</h3>
          <input type="text" @keyup.enter="searchResult" v-model.trim="searchInput">
          <b-button class="m-3" variant="outline-primary" @click="searchResult">검색</b-button>
          <b-button class="m-1" variant="outline-secondary" @click="initializeData">필터 초기화</b-button>
        </b-col>
        <b-col class="col-md-2">
          <img src="../assets/album.png" style="width:80px; height:96px;" alt="" @click="viewAlbum">
          <p>앨범 보기</p>
        </b-col>
      </b-row>
      </div>
    </div>
    <div>
      <h1>추천 영화 목록</h1>
      <b-row class="justify-content-md-center m-4 round-3" style="background-color: #FBFEAB;">
      <MovieListView v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
      </b-row>
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
      movies : [],
      dataSrc : [],
    }
  },
  created() {
    // 페이지 초기화 시 작동
    this.basicData()
  },
  computed: {
  },
  methods: {
    // 기본 영화 정보 가져오기(최초 로딩 시)
    basicData() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`
      })
      .then((response) => {
        this.dataSrc = response.data
        this.movies = response.data.slice(0,30)
        console.log(this.movies)
      })
      .catch((error) => {
        console.log(error)
      })
    },

    // 검색 필터 결과 표시
    searchResult() {
      if (this.searchInput !== null) {
        const filtered = this.dataSrc.filter((movie) => {
        return (movie.title.includes(this.searchInput))
      })
      this.movies = filtered
      } else {
        alert('검색어를 입력해 주세요.')
      }
    },

    // 사용자의 앨범 페이지로 이동
    viewAlbum() {
      this.$router.push({ name:'BookView' })
    },
    initializeData() {
      this.movies = this.dataSrc.slice(0,30)
    },
  }
}
</script>

<style>

</style>