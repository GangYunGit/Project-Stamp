<template>
  <div>
    <div class="container m-4 p-4" style="background-color: skyblue">
      <b-row>
      <b-col align-self="baseline">
        <h3>사용자님 환영합니다.</h3>
        <input type="text" v-model="searchInput">
        <b-button class="m-3" variant="outline-primary">검색</b-button>
      </b-col>
      <b-col align-self="baseline">
        <p>여기에 앨범으로 향하는 링크 넣기</p>
      </b-col>
    </b-row>
    </div>
    <div class="container m-4 p-4" style="background-color: burlywood">
        <carousel
          :navigation-enabled="true"
        >
          <slide>
            Slide 1 Content
          </slide>
          <slide>
            Slide 2 Content
          </slide>
          <slide>
            Slide 3 Content
          </slide>
          <slide>
            Slide 4 Content
          </slide>
        </carousel>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue from 'vue';
import VueCarousel from 'vue-carousel';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VueCarousel);

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      show: true,
      searchInput: null,
    }
  },
}
</script>

<style>

</style>