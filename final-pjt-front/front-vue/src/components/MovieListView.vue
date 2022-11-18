<template>
  <div class="col p-3 col-12 col-md-6 col-lg-4 col-xl-3">
    <b-card
      class="m-2 p-1 text-decoration-none"
      align-self="center"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
      img-alt="Poster Image"
      img-top
      @click="goDetail(movie.id)"
    >
        <b-card-text>
          {{ movie.overview }}
        </b-card-text>
      </b-card>
  </div>
</template>

<script>
export default {
  name: 'SearchListView',
  props: {
    movie : Object,
  },
  methods: {
    goDetail(id) {
        console.log(id)
        this.$router.push({ name:'DetailView', paramms: {id}})
    }
  }
}
</script>

<style>

</style>