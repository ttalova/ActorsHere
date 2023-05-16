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
            path: '/forgetPassword',
            name: 'forgetPassword',
            component: () => import('../components/ChangePasswordView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/changePassword/:token',
            name: 'changePassword',
            component: () => import('../components/UpdatePasswordView.vue'),
            meta: {unauthorizedAccess: true},
            props: true,
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue')
        },
        {
            path: '/menu',
            name: 'menu',
            component: () => import('../views/MainView.vue'),
            meta: {unauthorizedAccess: true}
        },
        {
            path: '/castingcard/:id',
            name: 'castingcard',
            component: () => import('../containers/CastingContainer.vue'),
            meta: {unauthorizedAccess: true},
            props: true,
        },
        {
            path: '/actorcard/:id',
            name: 'actorcard',
            component: () => import('../containers/ActorContainer.vue'),
            meta: {unauthorizedAccess: true},
            props: true,
        },
         {
            path: '/actorform',
            name: 'actorForm',
            component: () => import('../components/ActorFormComponent.vue'),
        },
        {
            path: '/employerform',
            name: 'employerForm',
            component: () => import('../components/EmployerFormComponent.vue'),
        },
        {
            path: '/castingform/',
            name: 'castingform',
             props: true,
            component: () => import('../components/CastingFormView.vue'),
        },
        {
            path: '/castingform/:id',
            name: 'castingformbyid',
             props: true,
            component: () => import('../components/CastingFormView.vue'),
        },
        {
            path: '/favorites',
            name: 'favorites',
            component: () => import('../components/FavoritesView.vue'),
        },
        {
            path: '/notifications',
            name: 'notifications',
            component: () => import('../components/NotificationsView.vue'),
        },
        {
            path: '/moderation',
            name: 'moderation',
            component: () => import('../components/ModerationView.vue'),
        },
        {
            path: '/mycastings',
            name: 'mycastings',
            component: () => import('../components/MyCastingsForEmployerView.vue'),
        },
        {
            path: '/myresponses',
            name: 'myResponses',
            component: () => import('../components/ActorsResponse.vue'),
        },
        {
            path: '/moderation',
            name: 'moderation',
            component: () => import('../components/ModerationView.vue'),
        },
        {
            path: '/responsefromactors',
            name: 'responsefromactors',
            component: () => import('../components/ResponseFromActorsView.vue'),
        },
        {
            path: '/settings',
            name: 'settings',
            component: () => import('../components/SettingsView.vue'),
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
