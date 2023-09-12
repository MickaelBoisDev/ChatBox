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
    
  },
  {
      path: '/room/:roomId',
      name: 'ChatRoom',
      component: ChatRoomVue,
      props: true,
      meta: { requiresAuth: true },
  },
  {
    path: '/rooms',
    name: 'Rooms',
    component: RoomsPageVue,
    meta: { requiresAuth: true },
   
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
