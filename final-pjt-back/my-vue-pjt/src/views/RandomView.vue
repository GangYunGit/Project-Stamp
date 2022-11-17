<template>
  <div>
    <button
      type="button"
      class="btn btn-success btn-lg btn-block"
      @click="getMovieURL()"
    >
      Pick
    </button>
    <br />
    <br />
    <img :src="imgBaseURL + movieURL.poster_path" alt="movie_poster" />
    <br />
    <br />
    <h2>{{ movieURL.title }}</h2>
  </div>
</template>

<script>
import _ from "lodash";

export default {
  name: "RandomView",
  data() {
    return {
      movieURL: null,
      imgBaseURL: "https://image.tmdb.org/t/p/w200",
    };
  },
  methods: {
    getMovieURL() {
      const storedMovieURLs = this.$store.state.moviesInfo;
      this.movieURL = _.sample(storedMovieURLs[0]);
      // console.log(this.movieURL);
    },
  },
  created() {
    console.log("Recommend Random Movie!");
    this.getMovieURL();
  },
};
</script>

<style>
</style>