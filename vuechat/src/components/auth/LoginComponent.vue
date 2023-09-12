<template>
    <div class="login-container">
        <input class="login-input" v-model="username" placeholder="Nom d'utilisateur" />
        <input type="password" class="login-input" v-model="password" placeholder="Mot de passe" />
        <button class="login-button" @click="login">Se connecter</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            username: '',
            password: '',
            errorMessage: ''
        }
    },

    methods: {
        async login() {
            try {
                const router = this.$router; 
                const djangoBaseUrl = import.meta.env.VITE__DJANGO_BASE_URL;
                let response = await axios.post(djangoBaseUrl + 'login/', {
                    username: this.username,
                    password: this.password
                });

                let data = response.data;
                if (response.status === 200) {
                    if (data.access_token) {
                        localStorage.setItem('access_token', data.access_token);
                        console.log(data);
                        localStorage.setItem('currentUser', JSON.stringify(data.user));
                        this.errorMessage = null;
                        router.push({ name: 'Rooms'});
                    }

                } else {
                    this.errorMessage = data.message;
                }
            } catch (error) {
                this.errorMessage = "Une erreur est survenue.";
                console.error(error);
            }
        },

    }
}
</script>

<style scoped>
.login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: #f0f0f0;
    padding: 20px;
    box-sizing: border-box;
}

.login-input {
    width: 100%;
    max-width: 300px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

.login-button {
    width: 100%;
    max-width: 300px;
    padding: 10px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.login-button:hover {
    background-color: #0056b3;
}

.error-message {
    color: #dc3545;
    margin-top: 10px;
}
</style>
