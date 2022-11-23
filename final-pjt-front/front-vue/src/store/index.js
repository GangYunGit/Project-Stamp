import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'
const VUE_APP_TMDB = process.env.VUE_APP_TMDB

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [
    ],
    // temp = 세부 정보에서 보여주는 데이터(새로고침 시 404 방지용)
    temp: null,
    recommended: [
    ],
    token: null,
    user_pk: null,
    like_genres: [],
    albums: [
    ],
    reviews: [
    ],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // // 회원가입 시 출력할 화면
    // INITIAL_LOGIN(state, token) {
    //   state.token = token
    //   router.push({ name: 'InitialLogin' })
    // },
    // 로그인 시 토큰(인증 정보) 저장
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'HomeView' })
    },
    // 사용자 정보 및 토큰 초기화(로그아웃)
    USER_LOGOUT(state) {
      state.token = null
      state.user_pk = null
      state.like_genres = null
      router.push({ name: 'loginView' })
    },

    // HomeView에 표시할 정보 업데이트
    HOME_MOVIES(state, movieData) {
      state.movies = movieData
    },

    // 사용자 로그인 시 pk 및 선호 장르 저장
    USER_ENTER(state, user_data) {
      // console.log(user_data)
      state.user_pk = user_data.id
      state.like_genres = user_data.like_genres
    },

    // 현재 접속한 사용자에 맞게 앨범 데이터 필터링
    SET_ALBUM(state, albumData) {
      state.albums = albumData
      // console.log(state.albums)
    },

    // 앨범 정보 추가
    ADD_ALBUM(state, movieData) {
      state.albums.push(movieData)
    },

    // 디테일 데이터 임시저장
    SET_DETAIL(state, dataTemp) {
      state.temp = dataTemp
    },

    // 추천 영화 목록 저장
    RECOMMEND_SERIES(state, dataSrc) {
      state.recommended = dataSrc
      // console.log(state.recommended)
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
          context.commit('SAVE_TOKEN', response.data.key)
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
      this.state.user_pk = null,
        this.state.albums = [],
        this.state.token = null,
        context.commit('USER_LOGOUT')
    },

    // 기본 페이지에 표시할 영화 정보 불러오기
    basicData(context, movieData) {
      context.commit('HOME_MOVIES', movieData)
    },

    // 사용자가 저장한 앨범 데이터 불러오기
    getAlbumData(context) {
      axios({
        method: 'get',
        url: `${API_URL}/albums/`,
      })
        .then((response) => {
          const albumSrc = response.data
          const userId = this.state.user_pk
          // const filtered = albumSrc.filter(page => page.user === userId)
          // console.log(filtered)
          // context.commit('SET_ALBUM', filtered)
          const payload = []
          for (let album of albumSrc) {
            // console.log(album)
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

    // 디테일 정보 임시 저장용
    detailTemp(context, detailData) {
      context.commit('SET_DETAIL', detailData)
    },

    // TMDB에서 추천받기
    getRecommendByTMDB (context, movieId) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${movieId}/recommendations?api_key=${VUE_APP_TMDB}&language=ko-KR` ,
      })
      .then((response) => {
        const resSrc = response.data.results
        // console.log(resSrc)

        // Django에서 작성한 DB fields에 알맞게 수정
        const payload = [];
        for (const mv of resSrc) {
          const element = {
            model: "movies.movie",
            id: mv.id,
            genre_ids: mv.genre_ids,
            overview: mv.overview,
            poster_path: mv.poster_path,
            release_date: mv.release_date,
            title: mv.title,
            vote_average: mv.vote_average,
            vote_count: mv.vote_count,
          };
          payload.push(element);
        }
        
        context.commit('RECOMMEND_SERIES', payload)
      })
      .catch((error) => {
        console.log(error)
      })
    },

    // Django에서 추천받기
    getRecommendByDjango(context) {
      const userPk = this.state.user_pk
      const userToken = this.state.token
      axios({
        method: 'get',
        url: `${API_URL}/movies/recommendation/${userPk}/`,
        headers: {
          Authorization: `Token ${userToken}`
        }
      })
      .then((response) => {
        // console.log(response.data)
        const payload = [];
        const resSrc = response.data
        // console.log(resSrc)
        for (const mv of resSrc) {
          const element = {
            id: mv.id,
            overview: mv.overview,
            title: mv.title,
            vote_count: mv.vote_count,
            vote_average: mv.vote_average,
            poster_path: mv.poster_path,
            release_date: mv.release_date
          } 
          payload.push(element);
        } 
        // console.log(payload)
        context.commit('RECOMMEND_SERIES', payload)
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  modules: {
  }
})
