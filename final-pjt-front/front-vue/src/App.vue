<template>
  <div id="app">
    <!-- <b-nav tabs justified>
      <b-nav-item active>Home</b-nav-item>
      <b-nav-item>Album</b-nav-item>
      <b-nav-item>Link with a long name </b-nav-item>
      <b-nav-item disabled>Disabled</b-nav-item>
    </b-nav> -->
    <router-view/>
  </div>
  <!-- <div id="app">
    <nav style="background-color:aquamarine">
      <router-link to="/" ><img src="./assets/homesm.png" alt="" style="width:40px; height:44px;"></router-link> |
      <router-link to="/book" v-if="isLogin===true"><img src="./assets/album.png" alt="" style="width:40px; height:44px;"></router-link>
      <router-link to="/login" v-if="isLogin===false">Login</router-link> |
      <router-link to="/register" v-if="isLogin===false">회원가입</router-link>
    </nav>
    <router-view/>
  </div> -->
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
  name: 'App',
  components: {
  },  
  computed: {
    isLogin() {
      if (this.$store.getters.isLogin) {
        // console.log(this.$store.getters.isLogin)
        return true
      } else {
        // console.log(this.$store.getters.isLogin)
        return false
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 10px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
