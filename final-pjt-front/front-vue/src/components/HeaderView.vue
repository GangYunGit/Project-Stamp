<template>
  <div class="container position-relative">
    <div class="row justify-content-center">
      <div class="text-center text-white col-md-5">
        <div v-if="isLogin">
          <h3>{{ userName }}님 환영합니다.</h3>
          <b-button variant="light" @click="userLogout">로그아웃</b-button>
        </div>
        <div v-else>
          <h3>로그인하세요.</h3>
          <router-link :to="{ name: 'loginView'}">로그인</router-link>
        </div>
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
      userName: this.$route.params.userName
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
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  }
}
</script>

<style>

</style>