<template>
  <h1 v-if="!favorites">Кастинги</h1>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{ error }}</b-alert>
  <b-list-group>
    <b-row>
  <b-col md="4" v-for="casting in results" :key="casting.id">
    <b-list-group-item>
       <img v-if="casting.photo && favorites" :src="`http://127.0.0.1:8000${casting.photo}`" style="width:100%" alt="img" class="card-img-top">
       <img v-if="casting.photo && !favorites" :src="`${casting.photo}`" style="width:100%" alt="img" class="card-img-top">
      <p>{{ casting.header }}</p>
      <p>Гонорар: {{ casting.fee }}</p>
      <p>Прием заявок до {{ casting.end_of_application }}</p>
      <b-button :to="{ name: 'castingcard', params: { id: casting.id }}" variant="primary">Просмотр</b-button>
    </b-list-group-item>
  </b-col>
</b-row>
<!--    <b-list-group-item v-for="casting in results" :key="casting.id">-->
<!--       <img v-if="casting.photo && favorites" :src="`http://127.0.0.1:8000${casting.photo}`" style="width:50%" alt="img" class="card-img-top">-->
<!--       <img v-if="casting.photo && !favorites" :src="`${casting.photo}`" style="width:50%" alt="img" class="card-img-top">-->
<!--      <p>{{ casting.header }}</p>-->
<!--      <p>{{ casting.city }}</p>-->
<!--      <p>{{ casting.fee }}</p>-->
<!--      <p>{{ casting.end_of_application }}</p>-->
<!--      <b-button :to="{ name: 'castingcard', params: { id: casting.id }}" variant="primary">Просмотр</b-button>-->
<!--    </b-list-group-item>-->
  </b-list-group>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {useAuthStore} from "../stores/auth";

export default {
  name: "CastingsView",
  props: {
    favorites: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  methods: {
    ...mapActions(useCastingsStore, ['getListOfCastings', 'load_favorites']),
  },
  computed: {
    ...mapState(useCastingsStore, ['results', 'isLoading', 'error']),
    ...mapState(useAuthStore, ['isAuth'])
  },
  created() {
    if (this.favorites) {
      this.load_favorites();
    } else {
      this.getListOfCastings();
    }
  }
}
</script>

<style scoped>

</style>