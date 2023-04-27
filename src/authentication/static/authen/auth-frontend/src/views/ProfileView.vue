<template>
  <p><b>Почта:</b> {{ user.email }}</p>
   <b-btn variant="outline-primary" @click="logoutClickHandler">Выйти</b-btn>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";

export default {
  name: "ProfileView",
  computed: mapState(useAuthStore, ['user']),
  methods: {
    ...mapActions(useAuthStore, ['logout']),
    logoutClickHandler() {
      this.logout();
      this.$router.push({name: "actors"});
    }
  }
}
</script>

<style scoped>

</style>