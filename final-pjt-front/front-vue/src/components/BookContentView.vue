<template>
  <div style="background-color:#FBFEAB">
      <b-card
      class="mx-auto mt-4"
      :title="album.movie_title"
      :img-src="`https://image.tmdb.org/t/p/original/${album.movie_poster_path}`"
      img-alt="Poster Image"
      img-top
      img-height="420"
      img-width="240"
      style="max-width: 26rem; object-fit: cover;"
    >
    <br>
      <b-card-text style="font-family: Gill Sans, sans-serif; line-height: 140%;">
        {{ album.review }}
      </b-card-text>
      <template #footer>
        <small class="text-muted"></small>
      </template>
      <router-link :to="{ name: 'ModifyView', params: { pk: album.id }}"><b-button class="m-4" variant="outline-primary">후기 수정하기</b-button></router-link>
      <p>추가된 날짜 : {{ createdAt }}</p>
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
  computed: {
    createdAt() {
      return  this.album.created_at.substring(0,10)
    }
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