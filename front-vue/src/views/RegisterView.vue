<template>
  <div class="container p-4">
    <h1>회원가입</h1>
    <div class="justify-content-md-center m-4">
      <b-form  @submit.stop.prevent>
      <label for="feedback-user">User ID</label>
      <b-form-input v-model="userId" :state="validationId" id="feedback-user"></b-form-input>
      <b-form-invalid-feedback :state="validationId">
        Your user ID must be 5-12 characters long.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validationId">
        Looks Good.
      </b-form-valid-feedback>

      <hr>

      <label for="text-password">Password</label>
      <b-form-input v-model="userPw" type="password" id="text-password" aria-describedby="password-help-block"></b-form-input>
      <b-form-text id="password-help-block">
        비밀번호는 8자 이상 20자 이하여야 하며, 문자와 숫자를 포함해야 합니다. 공백, 특수문자, 이모티콘 없어야 합니다.
      </b-form-text>
      <hr>
     </b-form>
    </div>
    <b-button pill variant="primary" @click="userSubmit">회원가입</b-button>
  </div>
</template>

<script>
import Vue from 'vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name: 'RegisterView',
  data() {
    return {
      userId: '',
      userPw: '',
    }
  },
  computed: {
    validationId() {
      return this.userId.length > 4 && this.userId.length < 13
    },
    validationPw() {
      // var passwordValid = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$";
      return this.userPw.length > 8 && this.userPw.length < 21 // && passwordValid.test(this.userPw)
    },
  },
  methods: {
    userSubmit() {
      const userId = this.userId
      const userPw = this.userPw
      const payload = {
        userId,
        userPw,
      }
      console.log(payload)
      // this.$store.dispatch('userSubmit', payload)
    }
  }
}
</script>

<style>

</style>