<template>
  <div class="container">
    <div class="justify-content-md-center">
      <FwTurn class="d-flex magazine" :options="bookOptions" >
        <BookContentView
            class="container" 
            v-for="(album, pageNo) in albums"
            :key="pageNo"
            :album="album"
          />
    </FwTurn>
    </div>
  </div>
</template>

<script>
import { FwTurn } from "vue-turnjs";
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
    FwTurn,
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
      bookOptions: {
        display: "double",
        acceleration: true,
        elevation: 50,
      },
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.magazine {
  width: 1152px;
  height: 752px;
}
.magazine .turn-page {
  background-color: #FBFEAB;
  background-size: 100% 100%;
}
</style>
