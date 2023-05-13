import {ref} from 'vue'

import {defineStore} from 'pinia'
import {
    getProfile,
    login as api_login,
    getAccess as api_getAccess,
    forgetPassword,
    changePassword as api_changePassword
} from "../services/api";
import {clearToken, getToken, getUser, setUser, storeAccess, storeRefresh} from "../services/LocalData";


export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            access: null,
            refresh: null,
            isLoading: false,
            error: null,
            user: getUser(),
            success: null
        }
    },
    getters: {
        isAuth() {
            return this.user !== null
        },
        isStaff() {
                return this.user.role === 'staff';
        },
        isActor() {
                return this.user.type_of_profile === 'actor';
        },
        isEmployer() {
                return this.user.type_of_profile === 'employer';
        },
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
                setUser(JSON.stringify(this.user))
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
            this.access = null;
            this.refresh = null
            clearToken('access');
            clearToken('refresh');
            clearToken('user');
        },
         async forgetUserPassword(email) {
            this.isLoading = true;
            try {
                const response = await forgetPassword(email)
                this.success = 'Инструкции по восстановлению пароля отправлена вам на почту'
                return response;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async changePassword(token, password_first, password_second) {
            this.isLoading = true;
            try {
                const response = await api_changePassword(token, password_first, password_second)
                this.success = 'Пароль успешно обновлен!'
                return response;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
    },
})
