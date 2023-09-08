<script setup>
import { RouterView } from 'vue-router'
import SidebarComponent from './components/SideBar.vue';

</script>
<template>
  <div class="app-container">
    <SidebarComponent />
    <router-view class="content-view" />
  </div>
</template>

<style>
.app-container {
  display: flex;
  height: 100vh;
  /* Utilise toute la hauteur de la fenêtre */
}

.content-view {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>
