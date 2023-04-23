import {API_URL} from "../consts";

export async function login(email, password) {
    const response = await fetch(`${API_URL}/api/login/`, {
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