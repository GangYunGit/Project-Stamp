<template>
    <div>
      <h1>Double display</h1>
      <turn>
        <div class="flip_page_double hard">Turn.js</div>
        <div class="flip_page_double hard"></div>
        <div class="flip_page_double hard">Page 1</div>
        <div class="flip_page_double hard">Page 2</div>
        <div class="flip_page_double hard">Page 3</div>
        <div class="flip_page_double hard">Page 4</div>
        <div class="flip_page_double hard"></div>
        <div class="flip_page_double hard"></div>
      </turn>
    </div>
  </template>
  
  <script>
  import { Turn } from "vue-turnjs";
  export default {
    components: {
      Turn
    },
    data() {
      return {
        display: "single"
      };
    }
  };
  </script>
   
  <style scoped>
  .turn-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  .flip_page_double {
    width: 100%;
    height: 100%;
    text-align: center;
    line-height: 300px;
    vertical-align: middle;
    background: url("https://miro.medium.com/max/10368/1*o8tTGo3vsocTKnCUyz0wHA.jpeg")
      no-repeat left center;
    background-size: 400px 600px;
  }
  .flip_page_single {
    width: 100%;
    height: 100%;
    text-align: center;
    line-height: 300px;
    vertical-align: middle;
    background: url("https://miro.medium.com/max/10368/1*o8tTGo3vsocTKnCUyz0wHA.jpeg")
      no-repeat left center;
    background-size: 800px 600px;
  }
  </style>