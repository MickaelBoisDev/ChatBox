<template>
    <div class="chat-room">
        <ChatBoxComponent :roomId="roomId" />
    </div>
</template>
  
<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import ChatBoxComponent from '../components/ChatBoxComponent.vue';  // Ajustez le chemin selon votre structure de projet

export default {
    components: {
        ChatBoxComponent,
    },
    setup() {
        const route = useRoute();
        const roomId = ref(route.params.roomId);
        onMounted(() => {
            roomId.value = route.params.roomId;
            console.log(roomId);
        });
        console.log(roomId);
        return { roomId };
    },
};
</script>
  
<style>
.chat-room {
    display: flex;
    flex-direction: column;
    height: 100%;
}
</style>
  