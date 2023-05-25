export const API_URL = import.meta.env.API_URL || 'http://127.0.0.1:8000/api';

export const WEBSOCKET_URL = (
    API_URL.replace("http", "ws").replace("/api", '/ws')
);