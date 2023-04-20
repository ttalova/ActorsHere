<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from "vue";
import TabMenu from 'primevue/tabmenu';

const items = ref([
    {
        label: 'Вход',
        icon: 'pi pi-fw pi-home',
        to: '/login'
    },
    {
        label: 'Регистрация',
        icon: 'pi pi-fw pi-calendar',
        to: '/registr'
    }
]);
</script>

<template>
   <div class="card">
        <TabMenu :model="items" />
        <router-view />
    </div>
</template>

<style scoped>
</style>
