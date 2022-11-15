<template>
  <div>
    <h1>Movie</h1>
    <div class="ms-1 row row-cols-1 row-cols-md-3">
      <MovieCard
        v-for="movieURL in movieURLs.cast"
        :key="movieURL.id"
        :movieURL="movieURL"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard";
import axios from "axios";

const API_KEY = process.env.VUE_APP_TMDB_API_KEY;
const API_URL =
  "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json";
const ACTOR_URL =
  "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json";

export default {
  name: "MovieView",
  components: {
    MovieCard,
  },
  data() {
    return {
      movieURLs: null,
      movieImgURL: null,
      movieCode: null,
    };
  },
  methods: {
    // 영화 진흥 위원회 API로 axios 요청 보내는 예시
    onInputChange() {
      axios({
        method: "get",
        url: API_URL,
        params: {
          key: API_KEY,
          itemPerPage: 100,
        },
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    searchActor() {
      axios({
        method: "get",
        url: ACTOR_URL,
        params: {
          key: API_KEY,
          peopleNm: "유아인",
        },
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    console.log("Welcom to Movie!");
    this.onInputChange();
    this.searchActor();
  },
};
</script>

<style>
</style>