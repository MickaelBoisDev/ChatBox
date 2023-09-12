<script setup>
import { RouterView } from 'vue-router'
import SidebarComponent from './components/SideBar.vue';
import PopUpComponent from './components/PopUpComponent.vue';
import { ref } from 'vue';



</script>

<template>
  <div class="app-container">
    <SidebarComponent />
    <router-view class="content-view" />
  </div>
</template>

<style>
html {
  background: rgb(28, 27, 28);


}

h1 {
  color: white;

}



.app-container {
  display: flex;
  height: 95vh;
  gap: 0.5rem;

}

.content-view {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
  border-radius: 1rem;
  background: rgb(69, 40, 88);
  background: linear-gradient(180deg, rgb(76, 60, 86) 0%, rgb(63, 56, 72) 100%);
}
</style>
