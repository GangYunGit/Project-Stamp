<template>
<section class="vh-100">
    <div style="">
      <b-nav tabs justified>
      <b-nav-item ><router-link :to="{ name: 'HomeView' }" style="text-decoration: none;">Home</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'BookView' }" style="text-decoration: none;">Album</router-link></b-nav-item>
      <b-nav-item ><router-link :to="{ name:'InitialLogin' }" style="text-decoration: none;">Recommend</router-link></b-nav-item>
      </b-nav>
    </div>
  <div class="mx-auto m-3 col-md-6 rounded-3" style="background-color:#FBFEAB;">
    <div class="row d-flex justify-content-center align-items-center h-70 m-3">
      <div class="col-md-8 col-lg-10">
        <h1 class="m-4">로그인</h1>
        <br>
        <form>
          <!-- Email input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="form3Example3">이메일 주소</label>

            <input v-model="userEmail" type="email" id="form3Example3" class="form-control form-control-lg"
              placeholder="이메일 주소를 입력하세요" />
          </div>

          <!-- Password input -->
          <div class="form-outline mb-3">
            <label class="form-label" for="form3Example4">비밀번호</label>

            <input v-model="userPw" type="password" id="form3Example4" class="form-control form-control-lg"
              placeholder="비밀번호를 입력하세요" />
          </div>

          <div class="d-flex justify-content-between align-items-center">
            <!-- Checkbox -->
            <!-- <div class="form-check mb-0">
              <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3" />
              <label class="form-check-label" for="form2Example3">
                Remember me
              </label>
            </div> -->
            <!-- <a href="#!" class="text-body">Forgot password?</a> -->
          </div>

          <div class="text-center text-lg-start mt-4 pt-2">
            <button @click="userLogin" type="button" class="btn btn-primary btn-lg"
              style="padding-left: 2.5rem; padding-right: 2.5rem;">Login</button>
            <p class="small fw-bold mt-2 pt-1 mb-4">계정이 없으신가요? 
              <router-link :to="{ name:'RegisterView' }">회원가입</router-link></p>
          </div>
        </form>
      </div>
    </div>
    <br>
    <FooterView />
  </div>
</section>
</template>

<script>
import FooterView from "@/components/FooterView.vue"

export default {
  name: 'LoginView',
  components: {
    FooterView,
  },
  data() {
    return {
      userEmail: null,
      userPw: null,
    }
  },
  methods: {
    userLogin() {
      const username = this.userEmail
      const password = this.userPw

      const payload = {
        username,
        password,
      }
      this.$store.dispatch("userLogin", payload)
    },
  },
}
</script>

<style>
.divider:after,
.divider:before {
content: "";
flex: 1;
height: 1px;
background: #eee;
}
.h-custom {
height: calc(100% - 73px);
}
@media (max-width: 450px) {
.h-custom {
height: 100%;
}
}
</style>