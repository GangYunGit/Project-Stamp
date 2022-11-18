<template>
  <div id="app">
    <nav style="background-color:aquamarine">
      <router-link to="/" ><img src="./assets/homesm.png" alt="" style="width:30px; height:32px;"></router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/book"><img src="./assets/album.png" alt="" style="width:30px; height:32px;"></router-link> |
      <router-link to="/register">회원가입</router-link> |
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
