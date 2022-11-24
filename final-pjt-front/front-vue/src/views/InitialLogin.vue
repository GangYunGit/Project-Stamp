<template>
  <div style="background-color: #bdfcfe; height: 100%">
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
            <span>
              <!-- <label for="input-default" class="p-2">장르명</label> -->
              <h5 class="p-2">장르명</h5>
              <b-button 
                variant="warning"
                v-for="genre_id in userLikeGenreData"
                :key="genre_id"
                class="m-1 mb-2"
                @click="deleteLikeGenre(genre_id)"
              >
                {{ getGenreName(genre_id) }} x
              </b-button>
            </span>
            <b-form-input
              v-model="genreName"
              @keyup.enter="addLikeGenre"
              placeholder="예) 코미디"
            ></b-form-input>
          </b-row>
          <b-row class="p-2">
            <!-- <label for="input-default" class="p-2">배우명</label> -->
            <h5 class="p-2">배우명</h5>
            <span>
              <b-button
                variant="warning"
                class="m-1 mb-2"
                v-for="actor_id in userLikeActorData"
                :key="actor_id"
                @click="deleteLikeActor(actor_id)"
              >
                {{ getActorName(actor_id) }} x
              </b-button>
            </span>
            <b-form-input
              v-model="actorName"
              @keyup.enter="addLikeActor"
              placeholder="예) 브래드 피트"
            ></b-form-input>
          </b-row>
        </b-col>
        <b-row align-h="end">
          <b-col cols="4">
            <b-button class="m-3" variant="primary" @click="submitTaste()"
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
    <br />
    <br />
    <FooterView />
  </div>
</template>

<script>
import Vue from "vue";
import VueCarousel from "vue-carousel";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import FooterView from "@/components/FooterView.vue";

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
  components: {
    FooterView,
  },
  data() {
    return {
      genreList: [],
      actorList: [],
      userLikeGenreData: null,
      userLikeActorData: null,
      genreName: null,
      actorName: null,
    };
  },
  created() {
    this.getGenreList();
    this.getUserLikes();
  },
  methods: {
    pushGenre(genre) {
      this.$store.state.like_genres.push(genre);
      this.genreName = null;
    },
    pushActor(actor) {
      this.$store.state.like_actors.push(actor);
      this.actorName = null;
    },
    deleteLikeGenre(genre) {
      const index = this.$store.state.like_genres.indexOf(genre);
      this.$store.state.like_genres.splice(index, 1);
    },
    deleteLikeActor(actor) {
      const index = this.$store.state.like_actors.indexOf(actor);
      this.$store.state.like_actors.splice(index, 1);
    },
    getGenreList() {
      axios
        .all([
          axios.get(`${API_URL}/movies/genres/`),
          axios.get(`${API_URL}/movies/actors/`),
        ])
        .then(
          axios.spread((genreResponse, actorResponse) => {
            this.genreList.push(genreResponse.data);
            this.actorList.push(actorResponse.data);
          })
        )
        .catch((error) => {
          console.log(error);
        });
    },
    getUserLikes() {
      this.userLikeGenreData = this.$store.state.like_genres;
      this.userLikeActorData = this.$store.state.like_actors;
    },
    getGenreName(genreId) {
      const genreName = this.genreList[0].filter(
        (genre) => genre.id === genreId
      );
      return genreName[0].name;
    },
    getActorName(actorId) {
      const actorName = this.actorList[0].filter(
        (actor) => actor.id === actorId
      );
      return actorName[0].name;
    },
    addLikeGenre() {
      const userGenre = this.genreList[0].filter(
        (genre) => genre.name === this.genreName
      );
      if (userGenre.length === 0) {
        alert("없는 장르 입니다.\n유효한 장르명을 입력하세요");
        return;
      }
      this.getUserLikes();
      const myGenre = userGenre[0].id;
      for (const genreId of this.$store.state.like_genres) {
        if (myGenre === genreId) {
          alert("이미 입력된 장르 입니다.");
          return;
        }
      }
      this.pushGenre(myGenre);
    },
    addLikeActor() {
      const userActor = this.actorList[0].filter(
        (actor) => actor.name === this.actorName
      );
      if (userActor.length === 0) {
        alert("없는 배우 입니다.\n유효한 배우명을 입력하세요");
        return;
      }
      this.getUserLikes();
      const myActor = userActor[0].id;
      for (const actorId of this.$store.state.like_actors) {
        if (myActor === actorId) {
          alert("이미 입력된 배우 입니다.");
          return;
        }
      }
      this.pushActor(myActor);
    },
    submitTaste() {
      const userGenre = this.$store.state.like_genres;
      const userActor = this.$store.state.like_actors;
      if (userGenre.length === 0 && userActor.length === 0) {
        alert(
          "장르명이나 배우명 중 하나는 입력해야 합니다.\n유효한 장르명을 입력하고 Enter를 눌러주세요."
        );
        return;
      } else {
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
          .then(() => {
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
      }
    },
  },
};
</script>

<style>
</style>