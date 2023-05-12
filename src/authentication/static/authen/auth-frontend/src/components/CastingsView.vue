<template>
<h1>Castings</h1>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{error}}</b-alert>
  <b-list-group>
    <b-list-group-item v-for="casting in results" :key="casting.id">
  <p>{{casting.header}}</p>
  <p>{{casting.city}}</p>
  <p>{{casting.fee}}</p>
      <b-button :to="{ name: 'castingcard', params: { id: casting.id }}" variant="primary">Просмотр</b-button>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";

export default {
  name: "CastingsView",
  methods: mapActions(useCastingsStore, ['getListOfCastings']),
  computed: mapState(useCastingsStore, ['results', 'isLoading', 'error']),
  created() {
    this.getListOfCastings();
  }
}
</script>

<style scoped>

</style>