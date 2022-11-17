<template>
  <div>
    <input type="text" v-model="searchInput">
    <h3>검색 결과</h3>
    <SearchListView 
      v-for="result in results"
      :key="result.id"
      :result="result"
    />
  </div>
</template>

<script>
import SearchListView from '@/components/SearchListView';

export default {
  name: 'SearchView',
  components: {
    SearchListView,
  },
  data() {
    return {
      searchInput: null,
    }
  },
  computed: {
    results() {
      return this.$store.dispatch()
    },
  },
  methods: {
    
  }
}
</script>

<style>

</style>