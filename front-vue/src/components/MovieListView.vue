<template>
  <div>
    <b-col>
    <b-card
      class="mb-2"
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
    </b-col>
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