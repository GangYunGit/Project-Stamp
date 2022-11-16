<template>
  <div class="container p-4">
    <h1>회원가입</h1>
    <div class="justify-content-md-center m-4">
      <b-form  @submit.stop.prevent>
      <label for="feedback-user">사용자 이메일(ID)</label>
      <b-form-input v-model="userId" :state="validationId" id="feedback-user"></b-form-input>
      <b-form-invalid-feedback :state="validationId">
        올바른 형식이 아닙니다.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validationId">
        사용할 수 있습니다.
      </b-form-valid-feedback>
      </b-form>

      <hr>
      <b-form  @submit.stop.prevent>
      <label for="text-password">비밀번호</label>
      <b-form-input v-model="userPw" type="password" id="text-password" aria-describedby="password-help-block"></b-form-input>
      <b-form-text id="password-help-block">
        비밀번호는 8자 이상 20자 이하여야 하며, 문자와 숫자를 포함해야 합니다. 공백, 특수문자, 이모티콘 없어야 합니다.
      </b-form-text>
      <b-form-invalid-feedback :state="validationPw">
        올바른 형식이 아닙니다.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validationPw">
        사용할 수 있습니다.
      </b-form-valid-feedback>
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
      var regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
      if (this.userId.match(regExp) === null) {
        return false
      } else {
        return true
      }
    },
    validationPw() {
      // 비밀번호 유효성 검사

      // 이하 console.log는 유효성 검사가 잘 작동하는지 테스트하는 용도
      console.log(this.userPw)
      var passwordValid = "^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]){8,20}"  /* eslint-disable-line */
      var pwTest = new RegExp(passwordValid)
      if (pwTest.test(this.userPw) && this.userPw.length >= 8) {
        return true
      } else {
        return false
      }
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
    },
  }
}
</script>

<style>

</style>