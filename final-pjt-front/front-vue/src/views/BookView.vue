<template>
  <div class="container p-2">
    <div class="justify-content-md-center m-4">
      <FwTurn class="d-flex justify-content-center magazine" :options="bookOptions" >
        <BookContentView
            class="container m-3" 
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
  background-color: #ccc;
  background-size: 100% 100%;
}
</style>
