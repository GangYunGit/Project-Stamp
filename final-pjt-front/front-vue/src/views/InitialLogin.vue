<template>
  <div class="container col-md-8 p-4" style="background-color: #FBFEAB; border-radius: 40px;">
    <div offset-md="4" class="row d-flex justify-content-center align-items-center">
      <h1>당신의 취향을 알려주세요.</h1>
      <br>
      <b-row class="col-7 p-3" offset-md="3">
      <b-col sm="3">
        <label for="input-default">영화 제목</label>
      </b-col>
      <b-col sm="9">
        <b-form-input v-model="movieName" placeholder="Enter your name"></b-form-input>
      </b-col>
    </b-row>
    <b-row class="col-7 p-3" offset-md="3">
      <b-col sm="3">
        <label for="input-default">장르명</label>
      </b-col>
      <b-col sm="9">
        <b-form-input v-model="genreName" placeholder="Enter your name"></b-form-input>
      </b-col>
    </b-row>
    <b-row class="col-7 p-3" offset-md="3">
      <b-col sm="3">
        <label for="input-default">배우명</label>
      </b-col>
      <b-col sm="9">
        <b-form-input v-model="actorName" placeholder="Enter your name"></b-form-input>
      </b-col>
    </b-row>
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
const API_URL = process.env.VUE_APP_API_KEY

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
        method: 'post',
        url: `${API_URL}/`,
      })
      .then((response) => {
        console.log(response)
        this.$router.push({ name: 'HomeView' })
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