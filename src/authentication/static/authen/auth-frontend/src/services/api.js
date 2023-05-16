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

export async function login(email, password) {
    const response = await instance.post('/auth/jwt/create/', {email, password})
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    if ([400, 401].includes(response.status)) {
        throw new Error('Некорректные учетные данные');
    }

    return response.data;
}
export async function forgetPassword(email) {
    const response = await instance.post('/api/forget-password', {email})
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    if ([400, 401].includes(response.status)) {
        throw new Error('Некорректные учетные данные');
    }
    console.log(response)
    return response.data;
}

export async function changePassword(token, password_first, password_second) {
    const response = await instance.post(`/api/change-password/${token}/`, {password_first, password_second})
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    if ([400, 401].includes(response.status)) {
        throw new Error('Некорректные учетные данные');
    }
    console.log(response)
    return response.data;
}

export async function registration(email, password) {
    const response = await instance.post('/api/registr/', {email, password});
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data.access;
}

export async function getProfile() {
    const response = await instance.get('/api/profile/')
    return await response.data;
}

export async function getTags() {
     const response = await instance.get("/api/tags/", );
    return response.data;
}

export async function getProjectTypes() {
     const response = await instance.get("/api/projecttype/", );
    return response.data;
}

export async function getCities() {
     const response = await instance.get("/api/cities/", );
    return response.data;
}

export async function getAccess(params) {
     const response = await instance.post('/auth/jwt/refresh/', params);
     if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data.access;
}

// actors
export async function getActors(params) {
     const response = await instance.get("/api/actors/", {params});
    return response.data;
}

export async function getFavorites() {
     const response = await instance.get("/api/actors/get_favorite_actors_by_user_id", );
     return response.data;
}
export async function getActorById(id) {
       const response = await instance.get(`/api/actors/${id}/`);
     return response.data;
}

export async function getActorLike(actor) {
     const response = await instance.get(`/api/favorite-actor/${actor}/get_like_by_user_and_actor`);
     return response.data;
}
export async function LikedActor(actor) {
     const response = await instance.post("/api/favorite-actor/", {actor});
    return response.data;
}
export async function DisLikedActor(like) {
     const response = await instance.delete(`/api/favorite-actor/${like}`);
    return response.data;
}

export async function getActorForm(user_id) {
     const response = await instance.get(`/api/actors/${user_id}/get_form_by_user_id/`);
    return response.data;
}

export async function actorform(params) {
    const response = await instance.post('/api/actors/', params);
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}

export async function updateactorform(params) {
    const response = await instance.put(`/api/actors/${params.id}/`, params);
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}

export async function deleteactorform(form_id) {
    const response = await instance.delete(`/api/actors/${form_id}/`);
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}



// export async function getClientId() {
//      const response = await instance.get("/api/clientid/", );
//      console.log(11111111, response.data[0]['client_id'])
//      return response.data[0]['client_id'];
// }