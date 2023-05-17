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


export async function setResponse(casting) {
     const response = await instance.post("/api/response/", {casting});
    return response.data;
}

export async function getCastingResponse(casting) {
     const response = await instance.get(`/api/response/${casting}/get_response_by_actor/`);
     return response.data;
}

export async function removeCastingResponse(casting) {
     const response = await instance.delete(`/api/response/${casting}`);
    return response.data;
}

export async function UserCastingResponse() {
     const response = await instance.get(`/api/castings/get_response_actors_by_user_id`);
     return response.data;
}

export async function ListOfActorsResponseToCasting(casting) {
     const response = await instance.get(`/api/actors/${casting}/get_list_of_actors_to_casting`);
     return response.data;
}
