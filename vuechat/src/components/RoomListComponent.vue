<template>
    <div v-if="rooms.length">
        <h1>Liste Rooms :</h1>
        <div v-for="room in rooms" :key="room.id">
            <span>{{ room.name }}</span> <!-- Ajustez 'name' selon le nom de la propriété dans votre objet room -->
        </div>
    </div>
</template>

<script>
import { onMounted, ref, reactive } from 'vue';
import axios from 'axios';

export default {
    name: 'RoomListComponent',
    setup() {
        const rooms = ref([]);

        const fetchRooms = async () => {
            try {
                const djangoBaseUrl = import.meta.env.VITE__DJANGO_BASE_URL;

                const response = await axios.get(djangoBaseUrl + 'api/rooms/');
                rooms.value = response.data;
                console.log(rooms.value);
            } catch (error) {
                console.error('Erreur lors de la récupération des rooms:', error);
            }
        };

        onMounted(fetchRooms);

        return { rooms };
    }
}
</script>

<style scoped></style>