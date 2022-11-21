<template>
  <div>
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }">Home</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'BookView' }">Album</router-link></b-nav-item>
      <b-nav-item >Recommended</b-nav-item>
      </b-nav>
    </div>
  <div class="container p-4 col-md-6 rounded-3 mt-4" style="background-color:#FBFEAB;">
    <h1>회원가입</h1>
    <div offset-md="3" class="row p-3 justify-content-md-center m-4">
      <!-- <b-form  @submit.stop.prevent>
      <label for="feedback-user">사용자 이름</label>
      <b-form-input v-model="userName" :state="validationName" id="feedback-username"></b-form-input>
      <b-form-invalid-feedback :state="validationName">
        2자 이상 20자 이하여야 합니다.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validationName">
        사용할 수 있습니다.
      </b-form-valid-feedback>
      </b-form> -->

      <b-form  @submit.stop.prevent>
      <label for="feedback-user">사용자 이메일(ID)</label>
      <b-form-input v-model="userEmail" :state="validationId" id="feedback-useremail"></b-form-input>
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
      <b-form-input v-model="userPw1" type="password" id="text-password1" aria-describedby="password-help-block"></b-form-input>
      <b-form-text id="password-help-block">
        비밀번호는 8자 이상 20자 이하여야 하며, 문자와 숫자, 특수문자를 포함해야 합니다.
      </b-form-text>
      <b-form-invalid-feedback :state="validationPw1">
        올바른 형식이 아닙니다.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validationPw1">
        사용할 수 있습니다.
      </b-form-valid-feedback>
      </b-form>
      <hr>

      <b-form  @submit.stop.prevent>
      <label for="text-password">비밀번호 확인</label>
      <b-form-input v-model="userPw2" type="password" id="text-password2" aria-describedby="password-help-block"></b-form-input>
      <b-form-text id="password-help-block">
        입력한 비밀번호를 다시 한 번 입력해주세요.
      </b-form-text>
      <b-form-invalid-feedback :state="validationPw2">
        유효하지 않은 비밀번호입니다.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validationPw2">
        사용할 수 있습니다.
      </b-form-valid-feedback>
      </b-form>
    </div>
    <b-button pill variant="primary" @click="userSubmit">회원가입</b-button>
  </div>
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
      // userName: '',
      userEmail: '',
      userPw1: '',
      userPw2: '',
    }
  },
  computed: {
    // validationName() {
    //   var pattern = /^[\w\Wㄱ-ㅎㅏ-ㅣ가-힣]{2,20}$/;
    //   if (this.userName.match(pattern) === null) {
    //     return false
    //   } else {
    //     return true
    //   }
    // },
    validationId() {
      var regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
      if (this.userEmail.match(regExp) === null) {
        return false
      } else {
        return true
      }
    },
    validationPw1() {
      // 비밀번호 유효성 검사

      // console.log(this.userPw1)
      var passwordValid = /^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]){8,20}/  /* eslint-disable-line */
      var pwTest = new RegExp(passwordValid)
      if (pwTest.test(this.userPw1)) {
        return true
      } else {
        return false
      }
    },
    validationPw2() {
      if (this.validationPw1 === true && this.userPw1 === this.userPw2) {
        return true
      } else {
        return false
      }
    },
  },
  methods: {
    userSubmit() {
      // const userName = this.userName
      const userEmail = this.userEmail
      const userPw1 = this.userPw1
      const userPw2 = this.userPw2
      const payload = {
        // userName,
        userEmail,
        userPw1,
        userPw2,
      }
      // console.log('제출완료')
      this.$store.dispatch('userSubmit', payload)
    },
  }
}
</script>

<style>

</style>