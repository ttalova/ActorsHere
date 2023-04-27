<script setup>
import {RouterView} from 'vue-router';
import MainHeader from "./components/MainHeader.vue";
</script>

<template>
  <MainHeader/>
  <b-container>
      <RouterView/>
  </b-container>
</template>

<style scoped>
</style>

<script>


import {useAuthStore} from "./stores/auth";
import {mapActions} from "pinia/dist/pinia";


export default {
    name: "App",
    created() {
        this.load()
    },
    methods: mapActions(useAuthStore, ['load'])
}
</script>
