import {ref} from 'vue'

import {defineStore} from 'pinia'
import {actorform, deleteactorform, getActorForm, getActors, updateactorform} from "../services/api";
import {deleteemployerform, employerform, getEmployerForm, updateemployerform} from "../services/employer_api";


export const useEmployersStore = defineStore('employers', {
    state: () => {
        return {
            isLoading: false,
            error: null,
            results: [],
            params: {
                search: null,
            },
            form: {}
        }
    },
    actions: {
        async updateformemployer(form) {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await updateemployerform(form);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async getMyFormEmployer(user_id) {
            try {
                return await getEmployerForm(user_id)
            } catch(e) {
                console.log(e)
            }
        },
        async deleteMyFormEmployer(form_id) {
            try {
                return await deleteemployerform(form_id)
            } catch(e) {
                console.log(e)
            }
        },
        async createemployer(form) {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await employerform(form);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        // async load() {
        //     this.isLoading = true;
        //     this.error = null;
        //     try {
        //         const params = {
        //             ...this.params,
        //             full_name: this.params.search
        //         }
        //         const responseData = await getActors(params);
        //         this.results = responseData.results;
        //     } catch (e) {
        //         this.error = e.message
        //     }
        //     this.isLoading = false;
        // },
        setParameter(key, value) {
            this.params[key] = value;
        },
        setParameters(params) {
            this.params = params;
        },
    }
})
