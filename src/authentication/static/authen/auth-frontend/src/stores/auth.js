import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getProfile, login as api_login} from "../services/api";
import {getToken, storeToken} from "../services/LocalData";


export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            token: getToken(),
            isLoading: false,
            error: null,
            user: null
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
            const data = await getProfile();
            this.user = data;
            console.log(data)
            this.isLoading = false;
        }
    }
})
