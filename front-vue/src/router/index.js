import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import BookView from '../views/BookView.vue'
import RegisterView from '../views/RegisterView.vue'
import SearchView from '../views/SearchView.vue'
import DetailView from '../views/DetailView.vue'

Vue.use(VueRouter)

// isLoggedIn = 로그인 확인용 변수(서비스 구현 시 수정 예정)
const isLoggedIn = false

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
  },
  {
    path: '/book',
    name: 'book',
    component: BookView,
  },
  {
    path: '/search/:q',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
