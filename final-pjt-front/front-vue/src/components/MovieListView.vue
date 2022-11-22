<template>
  <div class="col p-3 col-12 col-sm-6 col-md-4 col-xl-3">
    <router-link 
      :to="{ name: 'DetailView', params: { id: movie.id }}"
      style="text-decoration: none; color: black;"
    >
      <b-card
      class="m-2 p-1 text-decoration-none"
      align-self="center"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
      img-alt="Poster Image"
      img-top
      style="width: 88%;"
    >
        <b-card-text>
          <p>{{ genres }}</p>
          <b-icon icon="star" class="border-warning"></b-icon>
          {{ movie.vote_average }}
        </b-card-text>
      </b-card>
    </router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'SearchListView',
  props: {
    movie : Object,
  },
  data() {
    return {
      genres: '',
    }
  },
  created() {
    this.getGenreList()
  },
  methods: {
    getGenreList() {
      axios({
        method: 'get',
        url: "http://localhost:8000/movies/genres",
      })
      .then((response) => {
        let payload = ''
        const genreIdList = response.data
        // console.log(genreIdList)
        for (const genre of this.movie.genre_ids) {
          const genreName = genreIdList.filter(genreInfo => {
            if (genre === genreInfo.id) {
              return genreInfo.name
            }
          })
          payload = payload + genreName[0].name + ','
        }
        this.genres = payload
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style>

</style>