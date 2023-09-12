<template>
    <div>
        <div class="login-container">
            <h1>Connexion</h1>
            <input class="login-input" v-model="username" placeholder="Nom d'utilisateur" />
            <input type="password" class="login-input" v-model="password" placeholder="Mot de passe" />
            <button class="login-button" @click="login">Se connecter</button>
            <!-- <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p> -->
        </div>
        <PopUpComponent :show="showPopup" :message="message" @close="closeErrorPopup" />
    </div>
</template>

<script>
import axios from 'axios';
import PopUpComponent from '../PopUpComponent.vue';

export default {
    data() {
        return {
            username: '',
            password: '',
            errorMessage: '',
            message: '',
            showPopup: false
        }
    },
    components: {
        PopUpComponent
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
                        this.errorMessage = "Connexion réussi";
                        this.showError(this.errorMessage, true)
                        router.push({ name: 'Rooms' });
                    }

                } else {
                    this.errorMessage = data.message;
                    this.showError(this.errorMessage, true)
                }
            } catch (error) {
                this.errorMessage = "Une erreur est survenue.";
                this.showError(this.errorMessage, true)
                console.error(error);

            }
        },
        showError(messageInput, showPopup) {
            console.log("Okokokok");
            this.message= messageInput;
            this.showPopup = showPopup
        },

        closeErrorPopup() {
            this.showPopup = false;
        }


    }
}
</script>

<style scoped>
.login-container {

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;


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
