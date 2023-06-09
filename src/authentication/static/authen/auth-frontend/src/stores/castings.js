import {ref} from 'vue'

import {defineStore} from 'pinia'
import {
    createCastingForm, deleteCastingForm, DisLikedCasting as DisLikedCasting_api,
    getCasting,
    getCastingbyId, getCastingLike, getFavoritesCastings,
    getListOfCastings, LikedCasting as LikedCasting_api,
    updateCastingForm
} from "../services/castings_api";
import {
    getCastingResponse,
    ListOfActorsResponseToCasting,
    removeCastingResponse,
    setResponse,
    UserCastingResponse
} from "../services/response";


export const useCastingsStore = defineStore('castings', {
    state: () => {
        return {
            isLoading: false,
            error: null,
            results: [],
            params: {
                search: null,
            },
            form: {},
            like_info: null,
            response_info: null
        }
    },
    actions: {
        async updateCasting(form) {
            this.isLoading = true;
            this.error = null;
            try {
                await updateCastingForm(form);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async getCastings() {
            this.isLoading = true;
            this.error = null;
            try {
                return await getCasting();
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async deleteCasting(form_id) {
            try {
                return await deleteCastingForm(form_id)
            } catch (e) {
                console.log(e)
            }
        },
        async getListOfCastings() {
            this.isLoading = true;
            this.error = null;
            try {
                const params = {
                    ...this.params,
                    full_name: this.params.search
                }
                const responseData = await getListOfCastings(params);
                this.results = responseData.results;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async load_favorites() {
            this.isLoading = true;
            this.error = null;
            try {
                const params = {
                    ...this.params,
                    full_name: this.params.search
                }
                const responseData = await getFavoritesCastings();
                this.results = responseData;
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async createCasting(form) {
            this.isLoading = true;
            this.error = null;
            try {
                await createCastingForm(form);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async load(id) {
            this.isLoading = true;
            this.error = null;
            try {
                return await getCastingbyId(id);
            } catch (e) {
                this.error = e.message
            }
            this.isLoading = false;
        },
        async casting_be_liked(casting) {
            this.error = null;
            try {
                const responseData = await getCastingLike(casting);
                this.like_info = responseData;
            } catch (e) {
                    this.error = e.message;
            }
        },
        async LikedCasting(casting) {
            this.error = null;
            try {
                await LikedCasting_api(casting);
            } catch (e) {
                this.error = e.message
            }
        },
        async DisLikedCasting(like) {
            this.error = null;
            try {
                await DisLikedCasting_api(like);
            } catch (e) {
                this.error = e.message
            }
        },
        async ResponseToCasting(casting) {
            this.error = null;
            try {
                await setResponse(casting);
            } catch (e) {
                this.error = e.message
            }
        },
        async casting_in_response(casting) {
            this.error = null;
            try {
                const responseData = await getCastingResponse(casting);
                this.response_info = responseData;
            } catch (e) {
                    this.error = e.message;
            }
        },
          async DisResponseCasting(casting) {
            this.error = null;
            try {
                await removeCastingResponse(casting);
            } catch (e) {
                this.error = e.message
            }
        },
        async listOfUserResponse() {
            this.error = null;
            try {
                const responseData = await UserCastingResponse();
                this.results = responseData;
            } catch (e) {
                    this.error = e.message;
            }
        },
        async listOfActorsResponse(casting) {
            this.error = null;
            try {
                const responseData = await ListOfActorsResponseToCasting(casting);
                this.results = responseData;
            } catch (e) {
                    this.error = e.message;
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
