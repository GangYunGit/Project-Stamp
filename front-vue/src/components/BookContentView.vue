<template>
  <div style="background-color:#FBFEAB">
    <h1>페이지</h1>
    <p>{{ album.content }}</p>
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
  name: 'BookContentView',
  props: {
    album: Object,
  },
}
</script>

<style>

</style>