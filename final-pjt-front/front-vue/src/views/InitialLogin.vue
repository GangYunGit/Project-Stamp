<template>
  <div style="background-color: #BDFCFE; height:800px;">
    <div style="">
      <b-nav tabs justified>
        <b-nav-item><router-link :to="{ name: 'HomeView' }">Home</router-link></b-nav-item>
        <b-nav-item><router-link :to="{ name:'BookView' }">Album</router-link></b-nav-item>
        <b-nav-item active><router-link :to="{ name:'InitialLogin' }">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
    <div class="container col-md-8 p-4 mt-5" style="background-color: #FBFEAB; border-radius: 40px;">
      <div class="align-items-md-center">
        <h1>당신의 취향을 알려주세요.</h1>
        <br>
        <b-col class="col-7 mx-auto">
          <b-row class="p-2">
            <label for="input-default" class="p-2">영화 제목</label>
            <b-form-input v-model="movieName" placeholder="Enter your name"></b-form-input>
          </b-row>
          <b-row class="p-2">
            <label for="input-default" class="p-2">장르명</label>
            <b-form-input v-model="genreName" placeholder="Enter your name"></b-form-input>
          </b-row>
          <b-row class="p-2">
            <label for="input-default" class="p-2">배우명</label>
            <b-form-input v-model="actorName" placeholder="Enter your name"></b-form-input>
          </b-row>
        </b-col>
      <b-row align-h="end">
        <b-col cols="4">
          <b-button class="m-3" variant="primary" @click="submitTaste">확인</b-button>
        </b-col>
        <b-col cols="4" class="text-center">
          <br>
          <router-link :to="{ name:'HomeView' }"><a href="">직접 검색해 볼래요</a></router-link>
        </b-col>
      </b-row>
      </div>
    </div>
  </div>

</template>

<script>
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
const API_URL = "http://localhost:8000";

export default {
  name: 'InitialLogin',
  data() {
    return {
      movieName: null,
      genreName: null,
      actorName: null,
    }
  },
  methods: {
    submitTaste() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/genres/`,
      })
      .then((response) => {
        console.log(response.data)
        // this.$router.push({ name: 'RecommendView' })
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