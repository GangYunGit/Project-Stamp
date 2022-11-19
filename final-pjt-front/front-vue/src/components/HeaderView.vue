<template>
  <div class="container position-relative">
    <div class="text-center text-white col-md-10">
      <div v-if="isLogin">
        <b-row align-self="baseline">
          <b-col class="col-md-9 p-2 mx-auto">
            <h5>안녕하세요!</h5>
            <b-button variant="light" @click="userLogout">로그아웃</b-button>
          </b-col>
          <b-col class="col-md-3 mx-auto">
            <router-link :to="{ name:'AccountEdit' }"><img src="../assets/user.png" style="width:64px; height:64px;" alt=""></router-link>
            <p>회원정보 수정</p>
          </b-col>
        </b-row>
      </div>
      <div v-else>
        <h3>로그인하세요.</h3>
        <router-link :to="{ name: 'loginView'}">로그인</router-link>
      </div>
    </div>
  </div>
</template>

<script>

import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: 'HeaderView',
  data() {
    return {
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
      // return true
    }
  },
  methods: {
    userLogout() {
      this.$store.dispatch('userLogout')
    }
  },
}
</script>

<style>

</style>