<template>
  <div>
    <p @click="checkMovie" :class="{ 'is-checked': toWatchMovie.isChecked }">
      {{ toWatchMovie.title }}
    </p>
  </div>
</template>

<script>
export default {
  name: "WatchListItem",
  props: {
    toWatchMovie: Object,
  },
  methods: {
    checkMovie() {
      this.$store.dispatch("checkMovie", this.toWatchMovie);
    },
  },
  created() {
    console.log("To-Watch Movie List");
  },
};
</script>

<style>
.is-checked {
  text-decoration: line-through;
}
</style>