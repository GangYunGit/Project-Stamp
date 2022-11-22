<template>
  <div style="background-color:#FBFEAB">
      <b-card
      class="mx-auto m-4"
      :title="album.movie_title"
      :img-src="`https://image.tmdb.org/t/p/original/${album.movie_poster_path}`"
      img-alt="Poster Image"
      img-top
      img-height="400"
      img-width="200"
      style="max-width: 24rem; object-fit: cover;"
    >
    <br>
      <b-card-text style="font-family: Gill Sans, sans-serif; line-height: 140%;">
        {{ album.review }}
      </b-card-text>
      <template #footer>
        <small class="text-muted">Last updated 3 mins ago</small>
      </template>
      <router-link :to="{ name: 'ModifyView', params: { pk: album.id }}"><b-button variant="primary">후기 수정하기</b-button></router-link>
    </b-card>
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
  data() {
    return {
    }
  },
  components: {
  },
}
</script>

<style>

</style>