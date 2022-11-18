<template>
  <div class="container">
    <h2>후기 수정하기</h2>
    <div class="container justify-content-md-center p-2 col-md-6" style="background-color:#FBFEAB">
      <textarea name="" id="" cols="30" rows="10" v-model="newReview"></textarea>
      <br>
      <b-button class='m-3' variant="outline-primary"  @click="modifyReview">수정</b-button>
      <router-link :to="{ name:'BookView' }"><b-button class='m-3' variant="outline-dark">취소</b-button></router-link>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

const API_URL = process.env.VUE_APP_API_KEY

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
    name: 'ModifyView',
    data() {
        return {
            newReview: null,
        }
    },
    methods: {
        modifyReview() {
            axios({
                method: 'put',
                url: `${API_URL}/`,
                data: {
                    review: this.newReview,
                }
            })
            .then((response) => {
                console.log(response)
                this.$router.push({ name: 'BookView' })
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
}
</script>

<style>

</style>