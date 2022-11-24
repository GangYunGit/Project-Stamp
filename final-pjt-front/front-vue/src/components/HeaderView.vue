<template>
  <div class="container position-relative">
    <div class="text-center mx-auto col-md-8">
      <div v-if="isLogin">
        <b-row align-self="baseline">
            <h5>{{ hello }}</h5>
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
import _ from 'lodash'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: 'HeaderView',
  data() {
    return {
      hello: '',
      randomHello: [
        '감동적인 순간 기록해 두세요.',
        '놀라웠던 감정을 기억하세요.',
        '재미있고 행복한 경험을 남기세요.',
      ]
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
      // return true
    }
  },
  created() {
    this.getRandomHello()
  },
  methods: {
    userLogout() {
      this.$store.dispatch('userLogout')
    },
    getRandomHello() {
      const msgSrc = this.randomHello
      this.hello = _.sample(msgSrc)
      // console.log(this.hello)
    }
  },
}
</script>

<style>

</style>