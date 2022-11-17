import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import BookView from '../views/BookView.vue'
import RegisterView from '../views/RegisterView.vue'
// import DetailView from '../views/DetailView.vue'
import InitialLogin from '../views/InitialLogin.vue'
import RecommendView from '../views/RecommendView.vue'

// 실험용 템플릿
import FlibBook from '../views/FlipBook.vue'

Vue.use(VueRouter)

// isLoggedIn = 로그인 확인용 변수(서비스 구현 시 수정 예정)
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
    // beforeEnter(to, from, next) {
    //   if (isLoggedIn === true) {
    //     console.log('이미 로그인 되어있음')
    //     next({ name: 'HomeView' })
    //   } else {
    //     next()
    //   }
    // }
  },
  {
    path: '/register',
    name: 'RegisterView',
    component: RegisterView,
  },
  {
    path: '/hello',
    name: 'InitialLogin',
    component: InitialLogin,
  },
  {
    path: '/book',
    name: 'BookView',
    component: BookView,
  },
  // {
  //   path: '/:id',
  //   name: 'DetailView',
  //   component: DetailView,
  // },
  {
    path: '/:id/recommend',
    name: 'RecommendView',
    component: RecommendView,
  },
  {
    path: '/flipbook',
    name: 'FlipBook',
    component: FlibBook,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   const isLoggedIn = to.headers
//   // console.log(isLoggedIn)
//   const authPages = ['RecommendView', 'DetailView', 'BookView', 'InitialLogin', 'HomeView',]
//   const isAuthRequired = authPages.includes(to.name)
//   if (isAuthRequired && !isLoggedIn) {
//     next({ name:'loginView'})
//   } else {
//     next()
//   }
// })

export default router
