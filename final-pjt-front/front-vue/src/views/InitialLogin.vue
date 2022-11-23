<template>
  <div style="background-color: #bdfcfe; height: 800px">
    <div style="">
      <b-nav tabs justified>
        <b-nav-item
          ><router-link
            :to="{ name: 'HomeView' }"
            style="text-decoration: none; color: black"
            >Home</router-link
          ></b-nav-item
        >
        <b-nav-item
          ><router-link
            :to="{ name: 'BookView' }"
            style="text-decoration: none; color: black"
            >Album</router-link
          ></b-nav-item
        >
        <b-nav-item active
          ><router-link
            :to="{ name: 'InitialLogin' }"
            style="text-decoration: none; color: black"
            >Recommended</router-link
          ></b-nav-item
        >
        <b-nav-item>
          <router-link
            :to="{ name: 'AccountEdit' }"
            style="text-decoration: none; color: black"
            >회원정보</router-link
          >
        </b-nav-item>
      </b-nav>
    </div>
    <div
      class="container col-md-8 col-lg-6 p-4 mt-5"
      style="background-color: #fbfeab; border-radius: 40px"
    >
      <div class="align-items-md-center">
        <h1>당신의 취향을 알려주세요.</h1>
        <br />
        <b-col class="col-7 mx-auto">
          <b-row class="p-2">
            <label for="input-default" class="p-2">영화 제목</label>
            <b-form-input
              v-model="movieName"
              placeholder="추후 지원 예정"
            ></b-form-input>
          </b-row>
          <b-row class="p-2">
            <label for="input-default" class="p-2">장르명</label>
            <b-form-input
              v-model="genreName"
              placeholder="예) 코미디"
            ></b-form-input>
          </b-row>
          <b-row class="p-2">
            <label for="input-default" class="p-2">배우명</label>
            <b-form-input
              v-model="actorName"
              placeholder="추후 지원 예정"
            ></b-form-input>
          </b-row>
        </b-col>
        <b-row align-h="end">
          <b-col cols="4">
            <b-button class="m-3" variant="primary" @click="submitTaste"
              >확인</b-button
            >
          </b-col>
          <b-col cols="4" class="text-center">
            <br />
            <router-link :to="{ name: 'HomeView' }"
              ><a href="">직접 검색해 볼래요</a></router-link
            >
          </b-col>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import VueCarousel from "vue-carousel";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import axios from "axios";

Vue.use(VueCarousel);

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

// API_URL = "http://127.0.0.1:8000/"
const API_URL = "http://localhost:8000";

// axios.defaults.xsrfCookieName = 'csrftoken';
// axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export default {
  name: "InitialLogin",
  data() {
    return {
      movieName: null,
      genreName: null,
      actorName: null,
    };
  },
  methods: {
    submitTaste() {
      axios
        .all([
          axios.get(`${API_URL}/movies/genres/`),
          axios.get(`${API_URL}/movies/actors/`),
        ])
        .then(
          axios.spread((genreResponse, actorResponse) => {
            const genreList = genreResponse.data;
            const userGenre = genreList.filter((genre) => {
              return genre.name === this.genreName;
            });
            const actorList = actorResponse.data;

            const userActor = actorList.filter((actor) => {
              return actor.name === this.actorName;
            });
            return [userGenre[0].id, userActor[0].id];
          })
        )
        .then((response) => {
          console.log(this.$store.state.user_pk);
          console.log(response);
          const userGenre = response[0];
          const userActor = response[1];
          this.$store.state.like_genres.push(userGenre);
          this.$store.state.like_actors.push(userActor);
          axios({
            method: "put",
            url: `${API_URL}/movies/user/likes/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`,
            },
            data: {
              id: this.$store.state.user_pk,
              like_genres: this.$store.state.like_genres,
              like_actors: this.$store.state.like_actors,
            },
          })
            .then((response) => {
              console.log(response);
              this.$store.dispatch("getRecommendByDjango");
              const movieId = this.$store.state.recommended.id;
              this.$router.push({
                name: "RecommendView",
                params: { id: `${movieId}` },
              });
            })
            .catch((error) => {
              console.log(error);
            });
        })
        .catch((error) => {
          console.log(error);
        }, []);
    },
  },
};
</script>

<style>
</style>