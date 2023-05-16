<template>
<h1>Мои отклики</h1>
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
import {useAuthStore} from "../stores/auth";

export default {
  name: "ActorsResponse",
  methods: {...mapActions(useCastingsStore, ['listOfUserResponse']),
  },
  computed: {...mapState(useCastingsStore, ['results', 'isLoading', 'error']),
  ...mapState(useAuthStore, ['isAuth'])
  },
  created() {
       this.listOfUserResponse();
  }
}
</script>

<style scoped>

</style>