<template>
<h1>Мои кастинги</h1>
  <div class="text-center my-3">
  <b-button v-b-tooltip.hover>
    Активные
  </b-button>

  <b-button id="tooltip-target-1">
    Завершенные
  </b-button>
</div>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{error}}</b-alert>
  <b-list-group>
    <b-list-group-item v-for="casting in this.results" :key="casting.id">
  <h1>{{casting.header}}</h1>
      <h2>casting.fee</h2>
    </b-list-group-item>
  </b-list-group>
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
      error: null
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
          this.results = await this.getCastings(this.user.id)
      } catch (e) {
        this.error = e.message
      }
      this.isLoading = false
    },
  },
  computed: {
    ...mapState(useCastingsStore, ['isLoading', 'error', 'results']),
  ...mapState(useAuthStore, ['user'])},
}
</script>

<style scoped>

</style>