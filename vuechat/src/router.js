import { createRouter, createWebHistory } from 'vue-router'
import ChatRoomVue from './views/ChatRoom.vue'
import LoginPageVue from './views/LoginPage.vue'
import RegisterPageVue from './views/RegisterPage.vue'
import RoomsPageVue from './views/RoomsPage.vue'

const routes = [
  {
    path: '/chat',
    name: 'Chat',
    component: ChatRoomVue,
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      const isAuthenticated = !!localStorage.getItem('access_token');
      console.log("pas co", isAuthenticated);
      if (!isAuthenticated) {
        next({ name: 'Login' }); // rediriger vers la page de connexion
      } else {
        next(); // permettre la navigation
      }
    },
  },
  {
    path: '/rooms',
    name: 'Rooms',
    component: RoomsPageVue,
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      const isAuthenticated = !!localStorage.getItem('access_token');
      console.log("pas co", isAuthenticated);
      if (!isAuthenticated) {
        next({ name: 'Login' }); // rediriger vers la page de connexion
      } else {
        next(); // permettre la navigation
      }
    },
  },
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPageVue
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPageVue
  },

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
