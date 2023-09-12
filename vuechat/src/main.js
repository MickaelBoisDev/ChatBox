import { createApp } from 'vue';
import router from './router'
import './style.css'

import App from './App.vue';


import 'font-awesome/css/font-awesome.min.css';

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
    const isAuthenticated = !!localStorage.getItem('access_token');
  
    if (requiresAuth && !isAuthenticated) {
      next({ name: 'Login' });
    } else {
      next();
    }
  });

createApp(App).use(router).mount('#app')
