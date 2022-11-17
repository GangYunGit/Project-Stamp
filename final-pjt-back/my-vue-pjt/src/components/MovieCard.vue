<template>
  <div class="col mb-4" style="width: 18rem">
    <div class="card">
      <img
        :src="imgBaseURL + movieURL.poster_path"
        class="card-img-top"
        alt="movie_poster"
      />
      <div class="card-body">
        <h5 class="card-title">{{ movieURL.name }}</h5>
        <p class="card-text">
          {{ movieURL.overview }}
          <span v-if="!movieURL.overview">표시할 내용이 없습니다.</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

export default {
  name: "MovieCard",
  data() {
    return {
      imgBaseURL: "https://image.tmdb.org/t/p/original",
    };
  },
  props: {
    movieURL: Object,
  },
};
</script>

<style>
.card-text {
  height: 70px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
img {
  height: 400px;
}
</style>