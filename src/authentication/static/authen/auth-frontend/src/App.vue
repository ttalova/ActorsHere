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
import {mapActions, mapState} from "pinia/dist/pinia";


export default {
  name: "App",
  beforeCreate() {
    useAuthStore().initializeStore();
    const access = this.access
  },
  created() {
    this.load()
  },
  methods: {
    ...mapActions(useAuthStore, ['initializeStore', 'load', 'getAccess']),

  },
  computed: {
    ...mapState(useAuthStore, ['error', 'isLoading', 'access', 'refresh']),
  },
  mounted() {
  setInterval(() => {
    if (this.refresh) {
      this.getAccess(this.refresh)
    }
}, 5000)
  },

}
</script>
