import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = process.env.VUE_APP_API_KEY

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [
    ],
    recommended: [
    ],
    token: null,
    albums: [
      {
        content: 'content1',
      },
      {
        content: 'content2',
      },
      {
        content: 'content3',
      },
      {
        content: 'content4',
      },
    ]
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // 회원가입 시 출력할 화면
    INITIAL_LOGIN(state, token) {
      state.token = token
      router.push({ name: 'InitialLogin' })
    },
    // 토큰(인증 정보) 저장
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'HomeView' })
    },
    // 토큰 초기화(로그아웃)
    USER_LOGOUT(state) {
      state.token = null
      router.push({ name: 'LoginView'})
    }
  },
  actions: {
    // 회원가입
    userSubmit(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.userName,
          useremail: payload.userEmail,
          password1: payload.userPw1,
          password2: payload.userPw2,
        }
      })
      .then((response) => {
        console.log(response)
        context.commit('INITIAL_LOGIN', payload)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    // 사용자 로그인(기능 검증 필요)
    userLogin(context, payload) {
      axios({
        method:'post',
        url: `${API_URL}/accounts/login`,
        data: {
          username: payload.username,
          password: payload.password
        }
      })
      .then((response) => {
        context.commit('SAVE_TOKEN', response.data.key)
      })
    },
    // 사용자 로그아웃
    userLogout(context) {
      context.commit('USER_LOGOUT')
    },
    // 추천 영화 데이터 불러오기(미완성)
    getRecommendMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/`,
        // 사용자 토큰을 headers에 추가
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((response) => {
        console.log(response)
      })
        .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
  }
})
