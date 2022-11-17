<template>
  <div clas="container p-4">
    <div class="d-flex justify-content-md-center m-4">
      <div class="container m-4 p-4" style="background-color: skyblue">
      <HeaderView />
      <b-row>
        <b-col align-self="baseline">
          <input type="text" v-model="searchInput">
          <b-button class="m-3" variant="outline-primary" @click="searchResult">검색</b-button>
        </b-col>
        <b-col align-self="baseline">
          <p>여기에 앨범으로 향하는 링크 넣기</p>
        </b-col>
      </b-row>
      </div>
    </div>
    <div class="d-flex justify-content-md-center m-4">
      <CarouselView />
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

import HeaderView from '@/components/HeaderView'
import CarouselView from '@/components/CarouselView'

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
    HeaderView,
    CarouselView,
  },
  data() {
    return {
      // show : 캐러셀 구동에 필요한 데이터
      show: true,
      // searchInput : axios 요청에 보낼 검색어
      searchInput: null,
    }
  },
  computed: {
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