import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getProfile, registration as api_registration} from "../services/api";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "./auth";


export const useRegistrStore = defineStore('registration', {
    state: () => {
        return {
            access: null,
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
                const access = await api_registration(email, password);
                this.access = access;
                this.isSuccess = true;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        }
    }
})
