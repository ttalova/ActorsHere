<template>
  <h1>Мои отклики</h1>
  <div class="text-center my-3">
    <b-button v-b-tooltip.hover @click.prevent="this.isActiveDate=true" :variant="{ 'primary': isActiveDate }">
      Активные
    </b-button>

    <b-button id="tooltip-target-1" @click.prevent="this.isActiveDate=false" :variant="{ 'primary': !isActiveDate }">
      Завершенные
    </b-button>
  </div>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{ error }}</b-alert>
  <b-list-group>
    <b-list-group-item v-for="casting in filteredCastings" :key="casting.id">
      <img v-if="casting.photo" :src="`http://127.0.0.1:8000${casting.photo}`" style="width:50%" alt="img" class="card-img-top">
     <p>{{ casting.header }}</p>
      <p>{{ casting.city }}</p>
      <p>{{ casting.fee }}</p>
      <p>{{casting.end_of_application}}</p>
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
  data() {
    return {
      isActiveDate: true,
    }
  },
  methods: {
    ...mapActions(useCastingsStore, ['listOfUserResponse']),
    isDateActive() {
      const today = new Date();
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, '0'); // Месяцы в JavaScript нумеруются с 0, поэтому добавляем 1
      const day = String(today.getDate()).padStart(2, '0');
      const formattedDate = `${year}-${month}-${day}`;
      return formattedDate;
    },
  },
  computed: {
    ...mapState(useCastingsStore, ['results', 'isLoading', 'error']),
    ...mapState(useAuthStore, ['isAuth']),
    filteredCastings() {
      if (this.isActiveDate) {
        return this.results.filter(casting => casting.end_of_application >= this.isDateActive());
      } else {
        return this.results.filter(casting => casting.end_of_application < this.isDateActive());
      }
    }
  },
  created() {
    this.listOfUserResponse();
  }
}
</script>

<style scoped>

</style>