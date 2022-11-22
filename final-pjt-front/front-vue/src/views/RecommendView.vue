<template>
  <div style="background-color: #BDFCFE;">
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }">Home</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'BookView' }">Album</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'InitialLogin' }">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
    <div class="p-4" style="background-color:#BDFCFE;">
      <div class="mx-auto mt-3 p-3 col-lg-6 col-md-8" style="background-color:#FBFEAB">
        <b-card
          class="mb-2 rounded-3 mx-auto m-3 p-3"
          :title="movie[0].title"
          :img-src="`https://image.tmdb.org/t/p/original/${movie[0].poster_path}`"
          img-alt="Poster Image"
          img-top
          style="width: 30rem"
        >
          <b-card-text>
            {{ movie[0].overview }}
          </b-card-text>
        </b-card>
        <b-button v-if="alreadyAdded" pill variant="#667eea" class="m-2 gradient-custom" @click="addAlbum">앨범에 추가하기</b-button>
        <b-button v-else pill disabled class="m-2 gradient-custom" @click="addToAlbum">앨범에 추가됨</b-button>
        <b-button pill variant="outline-secondary" class="m-2" @click="getRecommend">다른 영화 보기</b-button>
        <b-button @click="goBack" pill variant="outline-warning" class="m-2">뒤로</b-button>
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
      // 테스트용 데이터
      movie: [
      {
        title: "Hair each base dark guess garden accept.",
        popularity: 4.0,
        overview: "Religious ball another laugh light million. Federal public power another.\nDuring always recent maintain major others bank. Say place address. Wife tough outside system must. Develop road especially.",
        released_data: "1995-01-20T07:27:13Z",
        poster_path: "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F346a942a-9e1d-4add-a4f2-6d8c18b7e7b6%2Fwelldone!.png?table=block&id=9acc0d11-cfdd-4ba0-a411-e09aa855d650&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&width=250&userId=3da73d48-5c6a-457e-843d-1891bf0e354c&cache=v2"
      },
    ],
      alreadyInAlbum: false
    }
  },
  created() {
    console.log(this.movie[0])
    // getRecommend()
  },
  computed: {
    // 앨범 중복 체크
    alreadyAdded() {
      const albums = this.$store.state.albums
      if (this.movies in albums) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    // 서버에서 추천 작품 받기
    // user_pk는 어디에서 얻을지 고민해야 함
    getRecommend() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/recommendation/` ,
      })
      .then((response) => {
        console.log(response)
        // 데이터 타입에 따라 this.movie에 저장할 정보 결정
        // this.movie = response.data.results
      })
      .catch((error) => {
        console.log(error)
      })
    },

    // 앨범에 이 영화 추가
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
