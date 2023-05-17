<template>
<h1>Мои кастинги</h1>
  <div class="text-center my-3">
    <b-button v-b-tooltip.hover @click.prevent="this.isActiveDate=true" :variant="{ 'primary': isActiveDate }">
      Активные
    </b-button>

    <b-button id="tooltip-target-1" @click.prevent="this.isActiveDate=false" :variant="{ 'primary': !isActiveDate }">
      Завершенные
    </b-button>
  </div>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{error}}</b-alert>
    <b-list-group-item v-for="casting in filteredCastings" :key="casting.id">
  <div>
  <b-card
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-title>
      {{casting.header}}
    </b-card-title>
    <b-card-text>
      <p>{{casting.end_of_application}}</p>
    </b-card-text>

    <b-button :to="{ name: 'castingcard', params: { id: casting.id }}" variant="primary">Просмотр</b-button>
  </b-card>
</div>
    </b-list-group-item>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {useAuthStore} from "../stores/auth";
import {getCities} from "../services/api";

export default {
  name: "MyCastingsForEmployerView",
  data() {
    return {
      results: [],
      isLoading: false,
      error: null,
      isActiveDate: true,
    }
  },
  created() {
    this.load()
  },
  methods: {
    ...mapActions(useCastingsStore, ['getCastings']),
    async load() {
      this.isLoading = true
      try {
          this.results = await this.getCastings()
      } catch (e) {
        this.error = e.message
      }
      this.isLoading = false
    },
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
    ...mapState(useCastingsStore, ['isLoading', 'error', 'results']),
  ...mapState(useAuthStore, ['user']),
  filteredCastings() {
      if (this.isActiveDate) {
        return this.results.filter(casting => casting.end_of_application >= this.isDateActive());
      } else {
        return this.results.filter(casting => casting.end_of_application < this.isDateActive());
      }
    }},
}
</script>

<style scoped>

</style>