<template>
  <div>
    <FwTurn class="d-flex justify-content-center magazine m-4" :options="bookOptions">
      <div v-for="i in 7" :key="i" style="background-color:burlywood;">
        <div class="container m-3" >
          <div v-if="i === 1">
            <h1>표지</h1>
          </div>
          <div v-else>
            <h1>페이지</h1>
            <p>{{i}}</p>
          </div>
        </div>
      </div>
    </FwTurn>
  </div>
</template>

<script>
import { FwTurn } from "vue-turnjs";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
  name: "BookView",
  components: {
    FwTurn,
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
