import { createRouter, createWebHistory,type RouteRecordRaw } from 'vue-router'
 
const routes: Array<RouteRecordRaw> = [
    {
      path: '/',
      redirect: '/Search'
    },
    {

      path: '/Search',
      name: '/Search',
      component: () => import('../views/search.vue')
    },
    {
      path: '/Adminstration/:user',
      name: '/Adminstration',
      component: () => import('../views/Adminstration.vue')
    },
    {
      path: '/detail/:id',
      name: '/detail',
      component: () => import('../views/detail.vue')
    }, {
      path: '/login',
      name: '/login',
      component: () => import('../views/login.vue')
    }, {
      path: '/delete',
      name: '/delete',
      component: () => import('../views/delete.vue')
    }, {
      path: '/user_login',
      name: '/user_login',
      component: () => import('../views/user_login.vue')
    }, {
      path: '/register',
      name: '/register',
      component: () => import('../views/register.vue')
    }, {
      path: '/user/:user',
      name: '/user',
      component: () => import('../views/user.vue')
    }
  
  
  
 
]
 
const router = createRouter({
  history: createWebHistory(),
  routes
})
 
export default router
