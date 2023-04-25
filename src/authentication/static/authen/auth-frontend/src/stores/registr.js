import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getProfile, registration as api_registration} from "../services/api";
import {storeToken} from "../services/LocalData";


export const useRegistrStore = defineStore('registration', {
    state: () => {
        return {
            token: null,
            isLoading: false,
            error: null,
            user: null
        }
    },
    actions: {
        async registration(email, password) {
            this.isLoading = true;
            this.error = null;
            try {
                const token = await api_registration(email, password);
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
            const data = await getProfile(this.token);
            this.user = data;
            this.isLoading = false;
        }
    }
})
