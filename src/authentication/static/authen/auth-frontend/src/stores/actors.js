import {ref} from 'vue'

import {defineStore} from 'pinia'
import {
    actorform,
    deleteactorform,
    getActorForm,
    getActorLike,
    getActors,
    LikedActor,
    DisLikedActor,
    updateactorform
} from "../services/api";


export const useActorsStore = defineStore('actors', {
    state: () => {
        return {
            isLoading: false,
            error: null,
            results: [],
            params: {
                search: null,
                tag_id: null
            },
            form: {}
        }
    },
    actions: {
        async updateformactor(form) {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await updateactorform(form);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async getMyForm(user_id) {
            try {
                return await getActorForm(user_id)
            } catch(e) {
                console.log(e)
            }
        },
        async deleteMyForm(form_id) {
            try {
                return await deleteactorform(form_id)
            } catch(e) {
                console.log(e)
            }
        },
        async createactor(form) {
            this.isLoading = true;
            this.error = null;
            try {
                const response = await actorform(form);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async load() {
            this.isLoading = true;
            this.error = null;
            try {
                const params = {
                    ...this.params,
                    full_name: this.params.search
                }
                const responseData = await getActors(params);
                this.results = responseData.results;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async actor_be_liked(actor){
            this.error = null;
            try {
                const responseData = await getActorLike(actor);
                this.results = responseData;
            } catch (e) {
                this.error = e.message
            }
        },
        async LikedActor(actor) {
            this.error = null;
            try {
                await LikedActor(actor);
            } catch (e) {
                this.error = e.message
            }
        },
        async DisLikedActor(like) {
            this.error = null;
            try {
                await DisLikedActor(like);
            } catch (e) {
                this.error = e.message
            }
        },
        setParameter(key, value) {
            this.params[key] = value;
        },
        setParameters(params) {
            this.params = params;
        },
    }
})
