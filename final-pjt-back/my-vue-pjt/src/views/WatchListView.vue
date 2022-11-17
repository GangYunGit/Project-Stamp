<template>
  <div>
    <WatchListForm />
    <br />
    <WatchListItem
      v-for="toWatchMovie in toWatchMovies"
      :key="toWatchMovie.createdAt"
      :toWatchMovie="toWatchMovie"
    />
  </div>
</template>

<script>
import WatchListForm from "@/components/WatchListForm";
import WatchListItem from "@/components/WatchListItem";

export default {
  name: "WatchListView",
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    toWatchMovies() {
      return this.$store.state.toWatchMovies;
    },
  },
};
</script>

<style>
</style>