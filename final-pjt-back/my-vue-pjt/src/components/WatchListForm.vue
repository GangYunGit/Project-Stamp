<template>
  <div>
    <h1>보고싶은 영화</h1>
    <form @submit.prevent="createToWatch">
      <input type="text" v-model="title" />
      <button>Add</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "WatchListForm",
  data() {
    return {
      title: null,
      isChecked: false,
    };
  },
  methods: {
    createToWatch() {
      const title = this.title;
      const isChecked = this.isChecked;
      const payload = {
        title,
        isChecked,
      };
      this.$store.dispatch("createToWatch", payload);
      this.title = null;
    },
  },
};
</script>

<style>
</style>