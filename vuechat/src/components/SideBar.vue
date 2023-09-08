<template>
    <div class="sidebar">
      <ul class="sidebar-menu">
        <li>
          <RouterLink to="/chat" active-class="active" class="sidebar-link">
            <i class="fas fa-comments"></i> Chat Rooms
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/login" active-class="active" class="sidebar-link">
            <i class="fas fa-sign-in-alt"></i> Sign In
          </RouterLink>
        </li>
        <li>
          <RouterLink to="/register" active-class="active" class="sidebar-link">
            <i class="fas fa-user-plus"></i> Sign Up
          </RouterLink>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  </script>
  
  <style scoped>
  .sidebar {
    width: 200px; /* Agrandi la largeur pour accueillir les icônes et le texte */
    background-color: #2c3e50; /* Utilise une couleur de fond plus sombre pour un meilleur contraste */
    color: #ecf0f1;
    padding: 20px;
    border-radius: 1rem;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s; /* Rend les transitions un peu plus lentes pour un effet plus lisse */
  }
  
  .sidebar-menu {
    list-style-type: none;
    padding: 0;
  }
  
  .sidebar-menu li {
    margin-bottom: 20px; /* Augmente l'espacement pour une meilleure lisibilité */
  }
  
  .sidebar-link {
    display: flex;
    align-items: center;
    color: #ecf0f1; /* Assure que le texte et les icônes sont de la même couleur */
    text-decoration: none; /* Supprime le soulignement des liens */
    font-size: 1.2rem; /* Augmente la taille de la police pour une meilleure lisibilité */
    transition: color 0.3s ease, transform 0.3s ease; /* Applique les transitions au lien lui-même plutôt qu'au li */
    padding: 10px; /* Ajoute un peu de padding autour des liens pour une meilleure apparence et une sensation au survol */
    border-radius: 10px; /* Arrondit les coins du fond au survol */
  }
  
  .sidebar-link:hover {
    background-color: #34495e; /* Ajoute une couleur de fond au survol pour un effet de mise en surbrillance */
    transform: scale(1.05); /* Réduit un peu l'effet de mise à l'échelle pour un look plus subtil */
  }
  
  .sidebar-link .fas {
    margin-right: 10px; /* Ajoute un peu d'espace entre l'icône et le texte */
    font-size: 1.5em; /* Augmente la taille des icônes pour qu'elles se démarquent davantage */
  }
  
  .active {
    color: #1abc9c; /* Change la couleur des liens actifs pour une meilleure indication visuelle */
  }
  </style>
  