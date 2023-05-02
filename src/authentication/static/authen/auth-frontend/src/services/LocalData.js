export function storeAccess(access) {
localStorage.setItem('access', access);
}

export function storeRefresh(refresh) {
localStorage.setItem('refresh', refresh);
}

export function getToken(type) {
return localStorage.getItem(type);
}

export function clearToken(type) {
localStorage.setItem(type, null);
}