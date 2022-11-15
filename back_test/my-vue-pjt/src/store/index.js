import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    moviesInfo: [],
    toWatchMovies: [],
  },
  getters: {
  },
  mutations: {
    STORE_MOVIES(state, movieURLs) {
      state.moviesInfo.push(movieURLs)
    },
    CREATE_TO_WATCH(state, toWatchMovie) {
      state.toWatchMovies.push(toWatchMovie)
    },
    CHECK_MOVIE(state, getToWatchMovie) {
      state.toWatchMovies = state.toWatchMovies.map((toWatchMovie) => {
        if (toWatchMovie === getToWatchMovie) {
          toWatchMovie.isChecked = !toWatchMovie.isChecked
        }
        return toWatchMovie
      })
    }
  },
  actions: {
    storeMovies(context, movieURLs) {
      context.commit("STORE_MOVIES", movieURLs)
    },
    createToWatch(context, payload) {
      const toWatchMovie = {
        title: payload.title,
        isChecked: payload.isChecked,
        createdAt: new Date().getTime()
      }
      context.commit("CREATE_TO_WATCH", toWatchMovie)
    },
    checkMovie(context, getToWatchMovie) {
      context.commit("CHECK_MOVIE", getToWatchMovie)
    }
  },
  modules: {
  }
})
