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


export async function getNotifications() {
    const response = await instance.get('/api/notifications/')
    return await response.data;
}