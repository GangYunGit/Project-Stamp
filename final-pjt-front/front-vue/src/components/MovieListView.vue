<template>
  <div class="col p-3 m-2">
    <b-card
      class="m-3 p-2 col-md-6"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/original/${movie.poster_path}`"
      img-alt="Poster Image"
      img-top
      style="width: 25rem"
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
  }
}
</script>

<style>

</style>