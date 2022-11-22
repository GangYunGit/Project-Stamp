<template>
  <div style="background-color: #bdfcfe">
    <!-- <NavBar /> -->
    <div style="">
      <b-nav tabs justified>
        <b-nav-item active
          ><router-link :to="{ name: 'HomeView' }"
            >Home</router-link
          ></b-nav-item
        >
        <b-nav-item active
          ><router-link :to="{ name: 'BookView' }"
            >Album</router-link
          ></b-nav-item
        >
        <b-nav-item active
          ><router-link :to="{ name: 'InitialLogin' }"
            >Recommended</router-link
          ></b-nav-item
        >
      </b-nav>
    </div>
    <br />
    <div class="col-8 justify-content-md-center mx-auto">
      <div class="p-4" style="background-color: skyblue; border-radius: 40px">
        <HeaderView />
        <hr />
        <b-row>
          <b-col align-self="baseline" class="col-md-8 mx-auto text-white">
            <h3>어떤 작품을 찾으시나요?</h3>
            <input
              type="text"
              @keyup.enter="searchResult"
              v-model.trim="searchInput"
            />
            <b-button
              class="m-3"
              variant="outline-primary"
              @click="searchResult"
              >검색</b-button
            >
            <b-button class="m-1" variant="outline-secondary" @click="basicData">필터 초기화</b-button>
            <router-link :to="{ name:'InitialLogin' }"><b-button class="m-1" variant="outline-secondary">영화 추천 받기</b-button></router-link>
          </b-col>
          <!-- <b-col class="col-md-3 mx-auto">
          <img src="../assets/album.png" style="width:80px; height:96px;" alt="" @click="viewAlbum">
        </b-col> -->
        </b-row>
      </div>
    </div>
    <br />
    <div>
      <h1>추천 영화 목록</h1>
      <b-row
        class="mx-auto m-3 p-3 round-3 col-11"
        style="background-color: #fbfeab"
      >
        <MovieListView
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
        />
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
import Vue from "vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import axios from "axios";

import HeaderView from "@/components/HeaderView";
import MovieListView from "@/components/MovieListView.vue";
// import NavBar from '@/components/NavBar.vue'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

// API_URL = "http://127.0.0.1:8000/"
const API_URL = "http://localhost:8000";

export default {
  name: "HomeView",
  components: {
    HeaderView,
    MovieListView,
    // NavBar,
  },
  data() {
    return {
      // show : 캐러셀 구동에 필요한 데이터
      show: true,
      // searchInput : axios 요청에 보낼 검색어
      searchInput: null,
      movies: [],
    };
  },
  created() {
    // 페이지 초기화 시 작동
    this.basicData();
    this.getMovieData();
    this.userData();
  },
  computed: {
  },
  methods: {
    // django에 저장된 기본 데이터 가져오기
    getMovieData() {
      axios({
        method: "get",
        url: `${API_URL}/movies/`,
      })
        .then((response) => {
          const movieData = response.data;
          // console.log(movieData)
          this.$store.dispatch("basicData", movieData);
          this.movies = this.$store.state.movies.slice(0, 36);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getAlbumData() {
      this.$store.dispatch('getAlbumData')
      // this.albums = this.$store.state.albums
    },
    // TMDB에서 영화 정보 가져오기(최초 로딩 시)
    basicData() {
      // axios({
      //   method: 'get',
      // url: `https://api.themoviedb.org/3/movie/popular?api_key=${process.env.VUE_APP_TMDB}&language=ko-KR&page=1`,
      // parmas: {
      //   api_key: process.env.API_KEY_TMDB,
      //   language: 'ko-KR',
      // }
      // })
      // .then((response) => {
      //   const movies = response.data.results
      //   console.log(movies)
      //   this.$store.dispatch('basicData', movies)
      //   this.movies = this.$store.state.movies
      //   return this.movies
      // })
      // .catch((error) => {
      //   console.log(error)
      // })
      // this.$store.dispatch('basicData')
      // this.movies = this.$store.state.movies.slice(0,30)
    },

    // 검색 필터 결과 표시
    searchResult() {
      const movieSrc = this.$store.state.movies;
      if (this.searchInput !== null) {
        const filtered = movieSrc.filter((movie) => {
          return movie.title.includes(this.searchInput);
        });
        this.movies = filtered;
      } else {
        alert("검색어를 입력해 주세요.");
      }
    },

    // 사용자의 앨범 페이지로 이동
    viewAlbum() {
      this.$router.push({ name: "BookView" });
    },

    userData() {
      const token = this.$store.state.token;
      // console.log(token)
      axios({
        method: "get",
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          // console.log(response)
          this.$store.commit("USER_ENTER", response.data.pk);
          // console.log(this.$store.state.user_pk)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>