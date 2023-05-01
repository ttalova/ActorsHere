import {API_URL} from "./consts";
import axios from "axios";
import {useAuthStore} from "../stores/auth";
const instance = axios.create({
    baseURL: API_URL,
});

instance.interceptors.request.use(function (config) {
    const auth = useAuthStore();
    if (auth.token) {
        config.headers['Authorization'] = `Token ${auth.token}`;
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});


export async function login(email, password) {
    const response = await instance.post('/login/', {email, password})
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    if ([400, 401].includes(response.status)) {
        throw new Error('Некорректные учетные данные');
    }

    return response.data.token;
}

export async function registration(email, password) {
    const response = await instance.post('/registr/', {email, password});
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data.token;
}

export async function getProfile() {
    const response = await instance.get('/profile/')
    return await response.data;
}


export async function getActors(params) {
     const response = await instance.get("/actors/", {params});
    return response.data;
}

export async function getTags() {
     const response = await instance.get("/tags/", );
    return response.data;
}

export async function getCities() {
     const response = await instance.get("/cities/", );
    return response.data;
}

export async function actorform(params) {
    const response = await instance.post('/actors/', {params});
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data;
}

