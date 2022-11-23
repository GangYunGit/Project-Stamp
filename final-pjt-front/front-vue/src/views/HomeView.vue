<template>
  <div style="background-color: #bdfcfe">
    <!-- <NavBar /> -->
    <div class="" style="background-color: white">
      <b-nav tabs justified>
        <b-nav-item active
          ><router-link
            :to="{ name: 'HomeView' }"
            style="text-decoration: none; color: black"
            >Home</router-link
          ></b-nav-item
        >
        <b-nav-item active
          ><router-link
            :to="{ name: 'BookView' }"
            style="text-decoration: none; color: black"
            >Album</router-link
          ></b-nav-item
        >
        <b-nav-item active
          ><router-link
            :to="{ name: 'InitialLogin' }"
            style="text-decoration: none; color: black"
            >Recommended</router-link
          ></b-nav-item
        >
        <b-nav-item v-if="isLogin" active>
          <p style="text-decoration: none; color: black" @click="userLogout">
            로그아웃
          </p>
        </b-nav-item>
        <b-nav-item v-else>
          <router-link :to="{ name: 'LoginView' }">로그인</router-link>
        </b-nav-item>
      </b-nav>
    </div>
    <br />
    <div class="col-8 justify-content-md-center mx-auto">
      <div class="p-4" style="background-color: #fbfeab; border-radius: 40px">
        <HeaderView />
        <hr />
        <b-row>
          <h3>어떤 작품을 찾으시나요?</h3>
          <b-col align-self="baseline" class="col-md-8 mx-auto">
            <!-- <select name="selectType" v-model="searchType" id="">
              <option value="title" selected  >제목으로 검색</option>
              <option value="genre">장르로 검색</option>
            </select> -->
            <b-form-input
              placeholder="제목으로 찾기"
              @keyup.enter="searchResult"
              v-model.trim="searchInput"
              class="m-1"
              size="sm"
            >
            </b-form-input>
            <b-button
              class="m-2"
              variant="outline-primary"
              @click="searchResult"
              >검색</b-button
            >
            <b-button class="m-2" variant="outline-secondary" @click="basicData"
              >필터 초기화</b-button
            >
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
        <MovieListView v-for="movie in movies" :key="movie.id" :movie="movie" />
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
const VUE_APP_TMDB = process.env.VUE_APP_TMDB;

export default {
  name: "HomeView",
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
      movies: [],
      searchType: "",
    };
  },
  created() {
    // 페이지 초기화 시 작동
    this.basicData();
    this.userData();
    this.getAlbumData();
  },
  computed: {
    isLogin() {
      if (this.$store.token !== null) {
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {
    getAlbumData() {
      this.$store.dispatch("getAlbumData");
      // this.albums = this.$store.state.albums
    },
    // TMDB에서 영화 정보 가져오기(최초 로딩 시)
    basicData() {
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/popular?api_key=${VUE_APP_TMDB}&language=ko-KR&page=1`,
        parmas: {
          api_key: process.env.API_KEY_TMDB,
          language: "ko-KR",
        },
      })
        .then((response) => {
          const movieSrc = response.data.results;
          // console.log(movieSrc)

          const payload = [];
          for (const mv of movieSrc) {
            const element = {
              model: "movies.movie",
              id: mv.id,
              genre_ids: mv.genre_ids,
              overview: mv.overview,
              poster_path: mv.poster_path,
              release_date: mv.release_date,
              title: mv.title,
              vote_average: mv.vote_average,
              vote_count: mv.vote_count,
            };
            payload.push(element);
          }
          this.$store.dispatch("basicData", payload);
          this.movies = this.$store.state.movies;
          // console.log(this.movies)
        })
        .catch((error) => {
          console.log(error);
        });
      // this.$store.dispatch('basicData')
      // this.movies = this.$store.state.movies.slice(0,30)
    },

    // 검색 필터 결과 표시(TMDB에 검색 요청 전송)
    searchResult() {
      console.log(this.searchType);
      if (this.searchInput) {
        axios({
          method: "get",
          url: `https://api.themoviedb.org/3/search/movie?api_key=${VUE_APP_TMDB}&query=${this.searchInput}&language=ko-KR&include_adult=false`,
        })
          .then((response) => {
            const responseData = response.data.results;
            const payload = [];
            for (const mv of responseData) {
              if (mv.poster_path !== null && mv.adult === false) {
                const element = {
                  model: "movies.movie",
                  id: mv.id,
                  genre_ids: mv.genre_ids,
                  overview: mv.overview,
                  poster_path: mv.poster_path,
                  release_date: mv.release_date,
                  title: mv.title,
                  vote_average: mv.vote_average,
                  vote_count: mv.vote_count,
                };
                payload.push(element);
              }
            }
            // console.log(responseData)
            if (payload.length === 0) {
              alert("검색된 결과가 없습니다.");
            } else {
              this.$store.dispatch("basicData", payload);
              this.movies = this.$store.state.movies;
            }
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        alert("검색어를 입력하세요.");
      }
    },

    // 사용자의 앨범 페이지로 이동
    viewAlbum() {
      this.$router.push({ name: "BookView" });
    },

    // 사용자 pk 및 선호 장르 가져오기
    userData() {
      const token = this.$store.state.token;
      // console.log(token)
      axios({
        method: "get",
        url: `${API_URL}/movies/user/likes/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => {
          // console.log(response);
          this.$store.commit("USER_ENTER", response.data);
          // console.log(this.$store.state.user_pk)
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // 로그아웃
    userLogout() {
      this.$store.dispatch("userLogout");
    },

    // 사용자 앨범 정보 가져오기(데이터 초기화용)
    getAlbumData() {
      this.$store.dispatch('getAlbumData')
      // console.log(this.albums)
    },
  },
};
</script>

<style>
</style>