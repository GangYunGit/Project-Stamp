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
    movies: [],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'LoginView' })
    }
  },
  actions: {
    userSubmit(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.userName,
          useremail: payload.userId,
          password1: payload.userPw1,
          password2: payload.userPw2,
        }
      })
      .then((response) => {
        console.log(response)
        context.commit('SAVE_TOKEN', payload)
      })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
  }
})
