<template>
<div class="m-4 p-2" style="background-color: burlywood">
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
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Vue from 'vue';
import VueCarousel from 'vue-carousel';

Vue.use(VueCarousel);

export default {
  name: 'AboutView',
  components: {

  },
  data() {
    return {
      show: true,
    }
  }
}

document.querySelector('div').style.backgroundColor = 'burlywood'
</script>


<style>

</style>
