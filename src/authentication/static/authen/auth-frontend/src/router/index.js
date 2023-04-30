import {createRouter, createWebHistory} from 'vue-router'
import Registration from '../views/RegistrationView.vue'
import {useAuthStore} from "../stores/auth";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/registr',
            name: 'registration',
            component: Registration,
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue')
        },
        {
            path: '/actors',
            name: 'actors',
            component: () => import('../views/MainView.vue'),
            meta: {unauthorizedAccess: true}
        },
    ]
});
router.beforeEach((to, from) => {
    const authStore = useAuthStore();
    const isUnauthorizedAccessAllowed = to.meta?.unauthorizedAccess === true
    if (!authStore.isAuth && !isUnauthorizedAccessAllowed && from.name !== 'login') {
        return ({name: 'login'});
    }
})

export default router
