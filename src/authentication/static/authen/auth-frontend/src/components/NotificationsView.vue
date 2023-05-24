<template>
  <h1 v-if="!favorites">Уведомления</h1>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{ error }}</b-alert>
 <p>{{ this.notifications }}</p>
  <b-list-group>
    <b-list-group-item v-for="notification in notifications" :key="notification.id">
      <p>{{ notification.text }}</p>
   </b-list-group-item>
  </b-list-group>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {useAuthStore} from "../stores/auth";

export default {
  name: "CastingsView",
  methods: {
    ...mapActions(useAuthStore, ['getNotes']),
  },
  computed: {
   ...mapState(useAuthStore, ['isActor', 'notifications'])
  },
  created() {
   this.notifications = this.getNotes()
  }
}
</script>

<style scoped>

</style>