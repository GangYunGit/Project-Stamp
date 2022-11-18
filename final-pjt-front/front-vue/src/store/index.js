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
      {
        id: 1,
        title: "Hair each base dark guess garden accept.",
        popularity: 3.5,
        overview: "Religious ball another laugh light million. Federal public power another.\nDuring always recent maintain major others bank. Say place address. Wife tough outside system must. Develop road especially.",
        released_data: "1995-01-20T07:27:13Z",
        poster_path: "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F346a942a-9e1d-4add-a4f2-6d8c18b7e7b6%2Fwelldone!.png?table=block&id=9acc0d11-cfdd-4ba0-a411-e09aa855d650&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&width=250&userId=3da73d48-5c6a-457e-843d-1891bf0e354c&cache=v2"
      },
      {
        id: 2,
        title: "TEST title 1",
        popularity: 4.0,
        overview: "TEST data 1",
        released_data: "1995-01-20T07:27:13Z",
        poster_path: "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F346a942a-9e1d-4add-a4f2-6d8c18b7e7b6%2Fwelldone!.png?table=block&id=9acc0d11-cfdd-4ba0-a411-e09aa855d650&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&width=250&userId=3da73d48-5c6a-457e-843d-1891bf0e354c&cache=v2"
      },
      {
        id: 3,
        title: "TEST title 2",
        popularity: 4.0,
        overview: "Religious ball another laugh light million. Federal public power another.\nDuring always recent maintain major others bank. Say place address. Wife tough outside system must. Develop road especially.",
        released_data: "1995-01-20T07:27:13Z",
        poster_path: "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F346a942a-9e1d-4add-a4f2-6d8c18b7e7b6%2Fwelldone!.png?table=block&id=9acc0d11-cfdd-4ba0-a411-e09aa855d650&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&width=250&userId=3da73d48-5c6a-457e-843d-1891bf0e354c&cache=v2"
      },
      {
        id: 4,
        title: "TEST title 3",
        popularity: 4.0,
        overview: "TEST data 2",
        released_data: "1995-01-20T07:27:13Z",
        poster_path: "https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F346a942a-9e1d-4add-a4f2-6d8c18b7e7b6%2Fwelldone!.png?table=block&id=9acc0d11-cfdd-4ba0-a411-e09aa855d650&spaceId=f7ab64f0-6613-4035-b609-06b6865d9b61&width=250&userId=3da73d48-5c6a-457e-843d-1891bf0e354c&cache=v2"
      },
    ],
    recommended: [
    ],
    token: null,
    albums: []
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
      router.push({ name: 'loginView' })
    },
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
          console.log(error)
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

    // 상세 및 추천 페이지에서 영화를 사용자 앨범에 추가(미완성)
    addToAlbums(context, payload) {
      const newData = payload
      axios({
        method: 'post',
        url: `${API_URL}/`,
        // data에는 추가할 영화 입력
        data: {
          newData
        },
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((response) => {
          console.log(response)
          alert('추가되었습니다.')
        })
        .catch((error) => {
          console.log(error)
        })

    }
  },
  modules: {
  }
})
