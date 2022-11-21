<template>
  <div style="background-color: #BDFCFE;">
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }">Home</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'BookView' }">Album</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'RecommendView' }">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
  <div class="p-4" style="background-color: #BDFCFE; height:800px;">
    <h1 class="p-3">앨범</h1>
    <turn 
      class="d-flex wrapper container justify-content-md-center rounded-3" 
      style="background-color:brown; width:100%; height: 645px; line-height: 75%;"
      >
      <BookContentView 
        class="flip_page_double hard"
        style="width:100%; height:100%;"
        v-for="(album, pageNo) in albums"
        :key="pageNo"
        :album="album"
      />
    </turn>
    <br>
  </div>
  </div>
</template>

<script>
import { Turn } from "vue-turnjs";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
import BookContentView from '@/components/BookContentView'

import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const API_URL = 'http://localhost:8000'

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
  data() {
    return {
      albums: [],
    };
  },
  computed: {
  },
  methods: {
    testMethod() {
      this.albums = this.$store.state.albums
    },
    getAlbumData() {
      axios({
        method:'get',
        url:`${API_URL}/albums/`,
      })
      .then((response) => {
        this.albums = response.data
        // console.log(this.albums)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  created() {
    this.testMethod()
    this.getAlbumData()
  },
  updated() {
    // this.testMethod()
    // this.getAlbumData()
  },
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
