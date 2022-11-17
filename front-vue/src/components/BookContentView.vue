<template>
  <div style="background-color:burlywood">
    <div v-if="true">
      <br>
      <h1>표지</h1>
    </div>
    <div v-else>
      <h1>페이지</h1>
      <p>{{i}}</p>
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
  name: 'BookContentView',
  props: {
  },
}
</script>

<style>

</style>