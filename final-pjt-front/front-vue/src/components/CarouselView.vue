<template>
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
</template>

<script>
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
  name: 'CarouselView',
}
</script>

<style>

</style>