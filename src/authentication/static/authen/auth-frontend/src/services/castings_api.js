import {API_URL} from "../consts";
import axios from "axios";
import {useAuthStore} from "../stores/auth";
const instance = axios.create({
    baseURL: API_URL,
});

instance.interceptors.request.use(function (config) {
    const auth = useAuthStore();
    if (auth.access) {
        config.headers['Authorization'] = `JWT ${auth.access}`;
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});

export async function getCasting() {
     const response = await instance.get(`/api/castings/get_users_castings/`);
     return response.data;
}

export async function getListOfCastings() {
     const response = await instance.get(`/api/castings/`);
     return response.data;
}
export async function getFavoritesCastings() {
     const response = await instance.get(`/api/castings/get_favorite_castings_by_user_id/`);
     return response.data;
}

export async function getCastingbyId(id) {
     const response = await instance.get(`/api/castings/${id}/`);
     return response.data;
}

export async function createCastingForm(params) {
    const response = await instance.post('/api/castings/', params);
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}

export async function updateCastingForm(params) {
    const response = await instance.put(`/api/castings/${params.get('id')}/`, params);
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}

export async function deleteCastingForm(form_id) {
    const response = await instance.delete(`/api/castings/${form_id}/`);
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}

export async function getCastingLike(casting) {
     const response = await instance.get(`/api/favorite-casting/${casting}/get_like_by_user_and_casting`);
     return response.data;
}
export async function LikedCasting(casting) {
     const response = await instance.post("/api/favorite-casting/", {casting});
     return response.data;
}
export async function DisLikedCasting(like) {
     const response = await instance.delete(`/api/favorite-casting/${like}`);
    return response.data;
}