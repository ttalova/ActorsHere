import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getProfile, login as api_login, getAccess as api_getAccess} from "../services/api";
import {clearToken, getToken, storeAccess, storeRefresh} from "../services/LocalData";


export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            // token: getToken(),
            access: null,
            refresh: null,
            isLoading: false,
            error: null,
            user: null,
            type_of_profile: false
        }
    },
    getters: {
        isAuth() {
            return this.user !== null;
        }
    },
    actions: {
        async getAccess(refresh) {
            const accessData = {
                refresh: refresh
            }
            const access = await api_getAccess(accessData)
            storeAccess(access);
            this.setAccess(access)
        },
        async initializeStore() {
            if (localStorage.getItem('access')) {

                this.access = getToken('access')
                this.refresh = getToken('refresh')
            } else {
                this.access = ''
                this.refresh = ''
            }
        },
        async setAccess(access) {
            this.access = access
        },
        async setRefresh(refresh) {
            this.refresh = refresh
        },
        async login(email, password) {
            this.isLoading = true;
            this.error = null;
            try {
                const data = await api_login(email, password);
                this.access = data.access;
                this.refresh = data.refresh;
                storeAccess(this.access);
                storeRefresh(this.refresh);
                this.setAccess(this.access)
                this.setRefresh(this.refresh)
                this.load();
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async load() {
            this.isLoading = true;
            try {
                this.user = await getProfile();
                this.type_of_profile = this.user.type_of_profile
            } catch (e) {
                console.log(e.message);
            }
            if (!this.user) {
                this.logout()
            }
            this.isLoading = false;
        },
        logout() {
            this.user = null;
            // this.token = null;
            this.access = null;
            this.refresh = null
            clearToken('access');
            clearToken('refresh');
        }
    }
})
