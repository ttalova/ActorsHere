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
