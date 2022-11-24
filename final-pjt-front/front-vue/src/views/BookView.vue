<template>
  <div style="background-color: #BDFCFE;">
    <div style="">
      <b-nav tabs justified>
        <b-nav-item ><router-link :to="{ name: 'HomeView' }" style="text-decoration: none; color: black;">Home</router-link></b-nav-item>
        <b-nav-item active><router-link :to="{ name:'BookView' }" style="text-decoration: none; color: black;">Album</router-link></b-nav-item>
        <b-nav-item ><router-link :to="{ name:'InitialLogin' }" style="text-decoration: none; color: black;">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
    <div class="p-4" style="background-color: #BDFCFE; height:140%;">
      <h1 class="">앨범</h1>
      <turn
        class="container wrapper mx-auto rounded-3" 
        style="background-color:brown; width:100%; height: 700px; line-height: 75%;"
        >
        <BookContentView 
          class="page-wrapper flip_page_double hard col"
          align-v="center"
          style="width:100%; height:100%;"
          v-for="album in albumList"
          :key="album.id"
          :album="album"
        />
      </turn>
      <br>
    </div>
    <FooterView />
  </div>
</template>

<script>
import { Turn } from "vue-turnjs";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import axios from 'axios'
import BookContentView from '@/components/BookContentView'
import FooterView from '@/components/FooterView'

import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// const API_URL = 'http://localhost:8000'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: "BookView",
  components: {
    BookContentView,
    FooterView,
    Turn,
  },
  data() {
    return {
      albumList: [],
      reviewList: [],
    };
  },
  computed: {
    albums: function() {
      // console.log(this.$store.state.albums)
      return this.$store.state.albums
    },
    reviews() {
      return this.$store.state.reviews
    },
  },
  methods: {
    testMethod() {
      this.albums = this.$store.state.albums
    },
    getAlbumData() {
      this.$store.dispatch('getAlbumData')
      this.albumList = this.$store.state.albums
      console.log(Turn, this.albumList)
    },
    getCommentData() {
      this.$store.dispatch('getCommentData')
    },
  },
  created() {
    this.getAlbumData()
    // console.log(Turn, this.albumList)
  },
  mounted() {
  if (localStorage.getItem('reloaded')) {
    // The page was just reloaded. Clear the value from local storage
    // so that it will reload the next time this page is visited.
    localStorage.removeItem('reloaded');
  } else {
    // Set a flag so that we know not to reload the page twice.
    localStorage.setItem('reloaded', '1');
    location.reload();
  }
}
};
</script>

<style>
.wrapper {
  align-items: center;
  display: flex;
  height: 100%;
  justify-content: center;
  width: 90%;
}
</style>
