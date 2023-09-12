<template>
    <div v-if="rooms && rooms.length">
        <h1 class="title">Rooms</h1>
        <div class="room-list">
            <div v-for="room in rooms" :key="room.id" class="room-card" @click="joinRoom(room.id)">
                <h2>{{ room.name }}</h2>
            </div>
        </div>
    </div>
    <div v-else>
        <p>Aucune room disponible.</p>
    </div>
</template>

<script>
import { onMounted, ref, reactive } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';


export default {
    name: 'RoomListComponent',
    setup() {
        const rooms = ref([]);
        const router = useRouter(); // Ajoutez cette ligne
        const route = useRoute();

        const fetchRooms = async () => {
            try {
                const djangoBaseUrl = import.meta.env.VITE__DJANGO_BASE_URL;

                const response = await axios.get(djangoBaseUrl + 'api/rooms/');
                rooms.value = response.data;
                console.log(rooms.value);
            } catch (error) {
                console.error('Erreur lors de la récupération des rooms:', error);
            }
        }
        const joinRoom = (roomId) => {
            console.log(`Joining room with ID: ${roomId}`);
            router.push({ name: 'ChatRoom', params: { roomId } });
        };

        onMounted(fetchRooms);
        return { rooms, joinRoom };
    }
}
</script>


<style scoped>
.title {
    text-align: start;
}

.room-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.room-card {
    background: #aa81bb49;
    border-radius: 12px;
    padding: 1.2rem;
    color: rgb(192, 192, 192);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    text-align: center;
    transition: all 0.3s ease;

}

.room-card:hover {
    background: #140c1849;
    color: white;

    font-size: 1.5rem;
}



.room-card h2 {
    margin: 0 0 10px;
    font-size: 1.5em;

}

.room-card p {
    margin: 0;
    color: #555;
}

h1 {
    font-size: 2em;
    margin-bottom: 20px;
}
</style>