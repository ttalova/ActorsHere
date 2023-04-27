import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getProfile, registration as api_registration} from "../services/api";
import {storeToken} from "../services/LocalData";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "./auth";


export const useRegistrStore = defineStore('registration', {
    state: () => {
        return {
            token: null,
            isLoading: false,
            error: null,
            user: null,
            isSuccess: false
        }
    },
    actions: {
        async registration(email, password) {
            this.isLoading = true;
            this.isSuccess = false;
            this.error = null;
            try {
                const token = await api_registration(email, password);
                this.token = token;
                this.isSuccess = true;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        }
    }
})
