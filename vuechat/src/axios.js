import axios from 'axios';

const instance = axios.create({
  baseURL: import.meta.env.VITE__DJANGO_BASE_URL, // L'URL de base de votre API Django
});

// Ajoute un intercepteur de requête
instance.interceptors.request.use(
  (config) => {
    // Récupère le token JWT du localStorage
    const token = localStorage.getItem('token');

    // Si le token existe, l'ajoute au header Authorization
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Retourne la configuration modifiée
    return config;
  },
  (error) => {
    // Si une erreur se produit, la rejette pour que vous puissiez la gérer dans votre code
    return Promise.reject(error);
  }
);

export default instance;
