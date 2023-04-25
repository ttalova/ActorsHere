import {API_URL} from "./consts";
import axios from "axios";
const instance = axios.create({
    baseURL: API_URL,
});

export async function login(email, password) {
    const response = await fetch(`${API_URL}/login/`, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({email, password})
    })
    if (response.status === 500) {
        console.error(response);
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    const data = await response.json()
    if ([400, 401].includes(response.status)) {
        throw new Error('Некорректные учетные данные');
    }

    return data.token;
}

export async function registration(email, password) {
    const response = await instance.post('/registr/', {email, password});
    if (response.status === 500) {
        console.error(response);
        throw new Error("Произошла неизвестная ошибка, попробуйте еще раз");
    }
    // python: response.status in (400, 401)
    if ([400, 401].includes(response.status)) {
        throw new Error(response.data.detail);
    }
    return response.data.token;
}

export async function getProfile(token) {
    const response = await fetch(`${API_URL}/profile/`, {
        method: 'get',
        headers: {
            "Athorization": `Token ${token}`,
        },
    })
    return await response.json();
}