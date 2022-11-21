<template>
  <div class="col p-3 col-12 col-sm-6 col-md-4 col-xl-3">
    <router-link :to="{ name: 'DetailView', params: { id: movie.id }}">
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
          {{ movie.vote_average }}
        </b-card-text>
      </b-card>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'SearchListView',
  props: {
    movie : Object,
  },
}
</script>

<style>

</style>