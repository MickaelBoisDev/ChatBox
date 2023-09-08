<template>
    <div>
        <input v-model="roomName" placeholder="Enter room name" />
        <button @click="joinRoom">Join Room</button>

        <ul v-if="joinedRoom">
            <li v-for="message in messages" :key="message.timestamp">{{ message.message }}</li>
        </ul>
        <textarea v-if="joinedRoom" v-model="newMessage"></textarea>
        <button v-if="joinedRoom" @click="send">Send</button>
    </div>
</template>
<script setup>
import useWebSocket from '../websocket.js';
import { ref, watch } from 'vue';

const roomName = ref("");
const joinedRoom = ref(false);
const messages = ref([]);
let sendMessage = null;
const newMessage = ref("");

watch(joinedRoom, (newVal) => {
    const token = localStorage.getItem('token');
    if (newVal) {
        const { messages: newMessages, sendMessage: sendMsg } = 
        useWebSocket(`ws://localhost:8000/ws/chat/${roomName.value}/`, token);
        console.log(newMessages);
        console.log(newMessages.value);
        messages.value = newMessages.value;
        sendMessage = sendMsg;
    }
});

function joinRoom() {
    if (roomName.value) {
        joinedRoom.value = true;
    }
}

function send() {
    if (sendMessage) {
        sendMessage(newMessage.value);
        newMessage.value = "";
    } else {
        console.error("WebSocket n'est pas initialisé.");
    }
}
</script>

  