<template>
  <div class="row d-flex justify-content-center align-items-center h-70 m-4">
    <div class="container m-4 p-4" style="background-color: skyblue">
      <b-row>
      <b-col align-self="baseline">
        <h3>사용자님 환영합니다.</h3>
        <input type="text" v-model="searchInput">
        <b-button class="m-3" variant="outline-primary" @click="searchResult">검색</b-button>
      </b-col>
      <b-col align-self="baseline">
        <p>여기에 앨범으로 향하는 링크 넣기</p>
      </b-col>
    </b-row>
    </div>
    <div class="container m-4 p-4" style="background-color: burlywood">
        <carousel
          :navigation-enabled="true"
        >
          <slide>
            Slide 1 Content
          </slide>
          <slide>
            Slide 2 Content
          </slide>
          <slide>
            Slide 3 Content
          </slide>
          <slide>
            Slide 4 Content
          </slide>
        </carousel>
    </div>
  </div>
</template>

<script>
// bootstrap, vuecarousel 관련 라이브러리
// @ is an alias to /src
import Vue from 'vue';
import VueCarousel from 'vue-carousel';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

Vue.use(VueCarousel);

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

// API_URL = "http://127.0.0.1:8000/"
const API_URL = process.env.VUE_APP_API_KEY

export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      // show : 캐러셀 구동에 필요한 데이터
      show: true,
      // searchInput : axios 요청에 보낼 검색어
      searchInput: null,
    }
  },
  methods: {
    // 검색 페이지로 이동
    searchResult() {
      // this.$router.push({ name: 'SearchView', params: { q: this.searchInput }})
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