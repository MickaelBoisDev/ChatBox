import { ref, watchEffect, onMounted } from 'vue';
export default function useWebSocket(url, token) {
    const socketRef = ref(null);
    const messages = ref([]);

    watchEffect(() => {
        // Ajoute le token à l'URL s'il est fourni
        const socketUrl = token ? `${url}?token=${token}` : url;
        console.log("Socket URL :", socketUrl);
        // Crée une nouvelle instance de WebSocket
        const socket = new WebSocket(socketUrl);
        socketRef.value = socket;
    
        // Défini le gestionnaire d'événements pour les messages entrants
        socket.onmessage = (event) => {
            console.log(event);
            const messageData = JSON.parse(event.data);
            console.log(messageData);
            messages.value.push(messageData);
        };
        
        // Défini d'autres gestionnaires d'événements (pour les fermetures, les erreurs, etc.)
        socket.onclose = (event) => {
            console.log("WebSocket closed:", event);
        };
        socket.onerror = (error) => {
            console.log("WebSocket Error:", error);
        };
    });

    // Crée une fonction pour envoyer des messages via la WebSocket
    function sendMessage(messageContent) {
        if (socketRef.value && socketRef.value.readyState === WebSocket.OPEN) {
            console.log(messageContent);
            socketRef.value.send(JSON.stringify(messageContent));
        }
    }

    return { messages, sendMessage };
}
