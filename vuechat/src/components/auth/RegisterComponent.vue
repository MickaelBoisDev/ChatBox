<template>
    <div class="register-container">
        <h1>Inscription</h1>

        <input class="register-input" v-model="username" placeholder="Nom d'utilisateur" />
        <input type="password" class="register-input" v-model="password" placeholder="Mot de passe" />
        <input type="password" class="register-input" v-model="passwordConfirmation"
            placeholder="Confirmation du mot de passe" />
        <button class="register-button" @click="register">S'inscrire</button>
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
            passwordConfirmation: '',
            errorMessage: ''
        };
    },
    methods: {
        async register() {
            try {
                const djangoBaseUrl = import.meta.env.VITE__DJANGO_BASE_URL;
                console.log(djangoBaseUrl + 'register/');
                const response = await axios.post(djangoBaseUrl + 'register/', {
                    username: this.username,
                    password: this.password,
                    password2: this.passwordConfirmation,
                });
                console.log(response);
                if (response.status === 200) {
                    if (response.data.token) {
                        localStorage.setItem('token', response.data.token);
                        localStorage.setItem('currentUser', JSON.stringify(response.data.user));
                    }
                } else {
                    this.errorMessage = response.data.message || 'Erreur lors de l’inscription';
                }
            } catch (error) {
                this.errorMessage = 'Une erreur est survenue';
            }
        },
        async logout() {
            localStorage.removeItem('access_token');
            localStorage.removeItem('currentUser');
        }
    },
};
</script>
  
<style scoped>
.register-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;



}

.register-input {
    width: 100%;
    max-width: 300px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

.register-button {
    width: 100%;
    max-width: 300px;
    padding: 10px;
    border: none;
    border-radius: 4px;
    background-color: #28a745;
    color: #fff;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.register-button:hover {
    background-color: #218838;
}

.error-message {
    color: #dc3545;
    margin-top: 10px;
}
</style>
  