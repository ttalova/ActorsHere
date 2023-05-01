import {ref} from 'vue'

import {defineStore} from 'pinia'
import {getActors} from "../services/api";


export const useActorsStore = defineStore('actors', {
    state: () => {
        return {
            isLoading: false,
            error: null,
            results: [],
            params: {
                search: null,
                tag_id: null
            }
        }
    },
    actions: {
        async load() {
            this.isLoading = true;
            this.error = null;
            try {
                const params = {...this.params,
                    full_name: this.params.search}
                const responseData = await getActors(params);
                this.results = responseData.results;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        setParameter(key, value) {
            this.params[key] = value;
        },
        setParameters(params) {
            this.params = params;
        }
    }
})
