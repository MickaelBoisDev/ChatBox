<template>
    <div class="chat-box">
        <div class="messages">
            <div class="message" v-for="message in messages" :key="message.id">
                <div class="message-content">
                    {{ message.message  }}
                </div>
                <div class="message-timestamp">
                    {{ message.timestamp }}
                </div>
            </div>
        </div>
        <div class="message-input">
            <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Entrez votre message ici">
            <button @click="sendMessage">Envoyer</button>
        </div>
    </div>
</template>

<script>
import useWebSocket from '../websocket'
export default {

    props: {
        roomId: {
            type: String,
            required: true,
        }
    },
    data() {
        return {
            newMessage: '',
        };
    },
    setup(props) {
        const djangoBaseUrl = import.meta.env.VITE__DJANGO_BASE_URL_WEBSOCKET;
        console.log(props.roomId);
        const url = `${djangoBaseUrl}/ws/rooms/${props.roomId}/`;
        const access_token = localStorage.getItem('access_token');

        const { messages, sendMessage } = useWebSocket(url, access_token);
        console.log(messages.value);

        return { messages, sendMessage };
    },
    methods: {
        handleSendMessage() {
            if (this.newMessage.trim()) {
                this.sendMessage(this.newMessage.trim());
                this.newMessage = '';
            }
        },
    },
    mounted() {
        // Initialize WebSocket connection
        const djangoBaseUrl = import.meta.env.VITE__DJANGO_BASE_URL_WEBSOCKET;

        this.socket = new WebSocket(`${djangoBaseUrl}/ws/rooms/` + this.roomId + '/');

        // Listen for new messages
        this.socket.addEventListener('message', this.receiveMessage);
    },
    beforeDestroy() {
        this.socket.close();
    },
};
</script>
<style scoped>
.chat-box {
    display: flex;
    flex-direction: column;
    height: 100%;
}

.messages {
    flex: 1;
    overflow-y: scroll;
}

.message {
    margin-bottom: 10px;
}

.message-content {
    background-color: #f0f0f0;
    padding: 10px;
    border-radius: 5px;
}

.message-timestamp {
    font-size: 0.8em;
    color: #888;
    margin-top: 5px;
}

.message-input {
    display: flex;
    padding: 10px;
}

.message-input input {
    flex: 1;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.message-input button {
    margin-left: 10px;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #28a745;
    color: #fff;
    cursor: pointer;
}
</style>

