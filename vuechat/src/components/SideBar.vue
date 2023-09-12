<template>
  <div class="sidebar">
    <ul class="sidebar-menu">
      <li>
        <RouterLink to="/rooms" active-class="active" class="sidebar-link">
          <i class="fas fa-comments"></i> Rooms
        </RouterLink>
      </li>
    </ul>
    <ul class="sidebar-menu-down">
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
  width: 10rem;
  background-color: #8e66828a;
  color: #ecf0f1;
  padding: 1rem;
  border-radius: 1rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
  display: flex;
  flex-flow: column;
  justify-content: space-between;

}

.sidebar-menu {
  list-style-type: none;
  padding: 0;

}

.sidebar-menu-down {
  list-style-type: none;
  padding: 0;
  justify-self: end;

}

.sidebar-menu li {
  margin-bottom: 20px;
}

.sidebar-link {
  display: flex;
  align-items: center;
  color: rgb(151, 151, 151);
  text-decoration: none;
  font-size: 1.2rem;
  transition: color 0.3s ease, transform 0.3s ease;
  padding: 1rem;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;


}

.sidebar-link:hover {
  background-color: #dd8a8f9d;
  -webkit-font-smoothing: subpixel-antialiased;
  color: #ecf0f1;
  box-shadow: 0 0 20px 10px #e586869f, 0 0 20px 2px
}

.sidebar-link .fas {
  margin-right: 10px;
  font-size: 1.5em;
}

.active {
  color: #ffffff;
}
</style>
  