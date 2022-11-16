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
      <!-- <b-form-input v-model="userPw" type="password" id="text-password" aria-describedby="password-help-block"></b-form-input> -->
      <b-form-input v-model="userPw" id="text-password" aria-describedby="password-help-block"></b-form-input>
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
      console.log(this.userPw)
      // 한글 입력을 제외한 후
      const notPhoneticSymbolExp = /[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
      if (notPhoneticSymbolExp.test(this.userPw)) {
          // 한글이 빠른 시간에 여러개 들어오는 경우도 있으니,한글이 없을 때까지 삭제하고, 검사
          let text = text.slice(0, -1);
          let condition = notPhoneticSymbolExp.test(text);
          while (condition) {
            text = text.slice(0, -1);
            condition = notPhoneticSymbolExp.test(text);
          }
          this.userPw = text;
        }
      // 비밀번호 유효성 검사
      var passwordValid = "^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]){8,20}"  /* eslint-disable-line */
      var pwTest = new RegExp(passwordValid)
      if (pwTest.test(this.userPw)) {
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