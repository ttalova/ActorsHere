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


export async function changeEmail(id, current_email, new_email, password) {
    const response = await instance.put(`/api/settings/${id}/`, {current_email, new_email, password})
    if (response.status === 500) {
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    if ([400, 401].includes(response.status)) {
        throw new Error('Некорректные учетные данные');
    }
    return response.data;
}