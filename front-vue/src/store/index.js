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
      router.push({ name: 'HomeView' })
    }
  },
  actions: {
    userSubmit(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password,
          password2: payload.password,
        }
      })
      .then((response) => {
        console.log(response)
        context.commit('SAVE_TOKEN', payload)
      })
      .catch(error => {
        if (!error.response) {
            // network error
            this.errorStatus = 'Error: Network Error';
        } else {
            this.errorStatus = error.response.data.message;
        }
      })
    },
  },
  modules: {
  }
})
