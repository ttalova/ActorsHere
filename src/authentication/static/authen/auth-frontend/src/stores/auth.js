import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getProfile, login as api_login} from "../services/api";
import {clearToken, getToken, storeToken} from "../services/LocalData";


export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            token: getToken(),
            isLoading: false,
            error: null,
            user: null,
        }
    },
    getters: {
        isAuth() {
            return this.user !== null;
        }
    },
    actions: {
        async login(email, password) {
            this.isLoading = true;
            this.error = null;
            try {
                const token = await api_login(email, password);
                this.token = token;
                storeToken(token);
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
                console.log(this.user)
            }
            catch (e) {
                console.log(e.message);
            }
            if (!this.user) {
                this.logout()
            }
            this.isLoading = false;
        },
        logout() {
            this.user = null;
            this.token = null;
            clearToken();
        }
    }
})
