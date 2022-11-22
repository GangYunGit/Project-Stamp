import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import BookView from '../views/BookView.vue'
import RegisterView from '../views/RegisterView.vue'
import DetailView from '../views/DetailView.vue'
import InitialLogin from '../views/InitialLogin.vue'
import RecommendView from '../views/RecommendView.vue'
import ModifyView from '../views/ModifyView.vue'
import AccountEdit from '../views/AccountEdit.vue'
import store from "../store/index.js"


Vue.use(VueRouter)
// const isLogIn = store.getters.isLogin
// const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/login',
    name: 'loginView',
    component: LoginView,
    beforeEnter(to, from, next) {
      const isLogIn = store.getters.isLogin
      if (isLogIn === true) {
        console.log('이미 로그인 되어있음')
        next({ name: 'HomeView' })
      } else {
        next()
      }
    }
  },
  {
    path: '/register',
    name: 'RegisterView',
    component: RegisterView,
  },
  {
    path: '/getrecommend',
    name: 'InitialLogin',
    component: InitialLogin,
  },
  {
    path: '/book',
    name: 'BookView',
    component: BookView,
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    // path: '/:id/recommend',
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView,
  },
  {
    path: '/modify/:pk',
    name: 'ModifyView',
    component: ModifyView,
  },
  {
    path: '/account',
    name: 'AccountEdit',
    component: AccountEdit,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.state.token
  // console.log(to)
  // console.log(from)
  // console.log(isLoggedIn)
  const authPages = ['RecommendView', 'DetailView', 'BookView', 'InitialLogin', 'HomeView',]
  const isAuthRequired = authPages.includes(to.name)
  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'loginView' })
  } else {
    next()
  }
})

export default router
