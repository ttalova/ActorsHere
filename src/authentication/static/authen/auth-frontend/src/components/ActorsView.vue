<template>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{error}}</b-alert>
  <b-list-group>
    <b-list-group-item v-for="actor in results" :key="actor.id">
  <p>{{actor.full_name}}</p>
  <p>{{actor.city}}</p>
  <p>{{actor.rating}}</p>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useActorsStore} from "../stores/actors";

export default {
  name: "ActorsView.vue",
  methods: mapActions(useActorsStore, ['load']),
  computed: mapState(useActorsStore, ['results', 'isLoading', 'error']),
  created() {
    this.load();
  }
}
</script>

<style scoped>

</style>