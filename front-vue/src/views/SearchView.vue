<template>
  <div>
    <input type="text" v-model="searchInput">
    <br>
    <br>
    <h3>검색 결과</h3>
  </div>
</template>

<script>
export default {
  name: 'SearchView',
  data() {
    return {
      searchInput: null,
    }
  },
  methods: {
    
  }
}
</script>

<style>

</style>