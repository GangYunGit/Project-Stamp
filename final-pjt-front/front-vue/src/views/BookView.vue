<template>
  <div>
      <h1>앨범 목록</h1>
      <turn class="container justify-content-md-center rounded-3" style="background-color:brown; width:100%; height: 100%; line-height: 400%;">
        <BookContentView 
          class="flip_page_double hard"
          v-for="(album, pageNo) in albums"
          :key="pageNo"
          :album="album"
        />
      </turn>
    </div>
</template>

<script>
import { Turn } from "vue-turnjs";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BookContentView from '@/components/BookContentView'

import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: "BookView",
  components: {
    // FwTurn,
    Turn,
    BookContentView,
  },
  computed: {
    albums() {
      return this.$store.state.albums
    }
  },
  props: {
    msg: String,
  },
  data() {
    return {
      // bookOptions: {
      //   display: "double",
      // },
    };
  },
};
</script>

<style>

</style>
