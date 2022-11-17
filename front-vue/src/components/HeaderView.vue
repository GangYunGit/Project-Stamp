<template>
    <div class="masthead">
      <div class="container position-relative">
          <div class="row justify-content-center">
              <div class="col-xl-6">
                  <div class="text-center text-white">
                    <div v-if="isLogin">
                      <h3>사용자님 환영합니다.</h3>
                    </div>
                    <div v-else>
                      <h3>로그인하세요.</h3>
                      <router-link :to="{ name: 'LoginView'}">로그인</router-link>
                    </div>
                  </div>
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
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  }
}
</script>

<style>

</style>