import {WEBSOCKET_URL} from "./consts";

let ws;

function open(roomId) {
    ws = new WebSocket(`${WEBSOCKET_URL}/server/${roomId}/`);
}

export function initMessages(roomId, onMessage) {
    function send(data) {
        ws.send(JSON.stringify(data));
    }

    open(roomId);

    ws.onopen = () => {
        console.log('open');
    };
    ws.onclose = () => {
        open(roomId);
    };
    ws.onerror = () => {
        open(roomId);
    };
    ws.onmessage = (message) => {
        const data = JSON.parse(message.data);
        onMessage(data);
    };

    return send;
}