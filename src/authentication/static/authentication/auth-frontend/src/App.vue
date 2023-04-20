<script setup>
import {RouterLink, RouterView} from 'vue-router';
import {ref} from "vue";
import TabMenu from 'primevue/tabmenu';

const items = ref([
  {
    label: 'Вход',
    to: '/login'
  },
  {
    label: 'Регистрация',
    to: '/registr'
  },
    {
    label: 'Выход',
    to: '/logout'
  }
]);
</script>

<template>
  <div class="main">
    <div class="card">
      <TabMenu :model="items"/>
      <router-view/>
    </div>
  </div>
</template>

<style scoped>
</style>
