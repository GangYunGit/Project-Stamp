import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

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
    user_pk: null,
    albums: [
    ],
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
      console.log(token)
      router.push({ name: 'InitialLogin' })
    },
    // 로그인 시 토큰(인증 정보) 저장
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'HomeView' })
    },
    // 사용자 정보 및 토큰 초기화(로그아웃)
    USER_LOGOUT(state) {
      state.token = null
      state.user_pk = null
      router.push({ name: 'loginView' })
    },

    // HomeView에 표시할 정보 업데이트
    HOME_MOVIES(state, movieData) {
      state.movies = movieData
    },

    // 사용자 로그인 시 pk 저장
    USER_ENTER(state, pk) {
      // console.log(pk)
      state.user_pk = pk
    },

    // 현재 접속한 사용자에 맞게 앨범 데이터 필터링
    SET_ALBUM(state, albumData) {
      state.albums = albumData
      console.log(state.albums)
    }
  },
  actions: {
    // 회원가입
    userSubmit(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          // username: payload.userName,
          email: payload.userEmail,
          password1: payload.userPw1,
          password2: payload.userPw2,
        },
      })
        .then((response) => {
          context.commit('INITIAL_LOGIN', response.data.key)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    // 사용자 로그인
    userLogin(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          email: payload.username,
          password: payload.password,
        }
      })
        .then((response) => {
          context.commit('SAVE_TOKEN', response.data.key)
        })
    },

    // 회원정보 수정
    userEdit(context, payload) {
      axios({
        method: 'put',
        url: `${API_URL}/accounts/signup/`,
        data: {
          // username: payload.userName,
          email: payload.userEmail,
          password1: payload.userPw1,
          password2: payload.userPw2,
        }
      })
        .then((response) => {
          console.log(response)
          alert('수정되었습니다.')
          context.commit('SAVE_TOKEN', payload)
        })
        .catch((error) => {
          alert('아이디와 비밀번호를 확인하세요.')
          console.log(error)
        })
    },

    // 사용자 로그아웃
    userLogout(context) {
      context.commit('USER_LOGOUT')
    },

    // 기본 페이지에 표시할 영화 정보 불러오기
    basicData(context, movieData) {
      context.commit('HOME_MOVIES', movieData)
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

    // 사용자가 저장한 앨범 데이터 불러오기
    getAlbumData(context) {
      axios({
        method:'get',
        url:`${API_URL}/albums/`,
      })
      .then((response) => {
        const albumSrc = response.data
        const userId = this.state.user_pk
        // const filtered = albumSrc.filter(page => page.user === userId)
        // console.log(filtered)
        // context.commit('SET_ALBUM', filtered)
        const payload = []
        for (let album of albumSrc) {
          // console.log(album.user)
          // console.log(userId)
          if (album.user === userId) {
            payload.push(album)
          }
        }
        // console.log(payload)
        context.commit('SET_ALBUM', payload)
    })
      .catch((error) => {
        console.log(error)
      })
    },
  },
  modules: {
  }
})
