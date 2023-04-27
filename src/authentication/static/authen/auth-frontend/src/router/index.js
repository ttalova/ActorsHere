import {createRouter, createWebHistory} from 'vue-router'
import Registration from '../views/Registration.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/registr',
            name: 'registration',
            component: Registration
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/Login.vue')
        },
    ]
})

export default router
