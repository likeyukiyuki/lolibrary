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
      path: '/Adminstration',
      name: '/Adminstration',
      component: () => import('../views/Adminstration.vue'),
      props: { default: true, sidebar: false }
    },
    {
      path: '/detail/:id',
      name: '/detail',
      component: () => import('../views/detail.vue'),
      props: { default: true, sidebar: false }
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
      path: '/user',
      name: '/user',
      component: () => import('../views/user.vue'),
      props: { default: true, sidebar: false }
    }, {
      path: '/audit/:id/:user',
      name: '/audit',
      component: () => import('../views/audit.vue'),
      props: { default: true, sidebar: false }
    }
  
  
  
 
]
 
const router = createRouter({
  history: createWebHistory(),
  routes
})
 
export default router
