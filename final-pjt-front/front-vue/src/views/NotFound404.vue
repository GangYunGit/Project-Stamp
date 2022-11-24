<template>
  <div>
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }" style="text-decoration: none; color: black;">Home</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'BookView' }" style="text-decoration: none; color: black;">Album</router-link></b-nav-item>
      <b-nav-item active><router-link :to="{ name:'InitialLogin' }" style="text-decoration: none; color: black;">Recommended</router-link></b-nav-item>
      </b-nav>
    </div>
    <div class='p-4' style="background-color:#BDFCFE;">
      <h1>404 Error</h1>
      <p>페이지를 찾을 수 없습니다.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound404',
}
</script>

<style>

</style>