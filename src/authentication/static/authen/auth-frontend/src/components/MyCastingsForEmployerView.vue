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
    <b-list-group-item v-for="casting in this.results" :key="casting.id">
  <div>
  <b-card
    img-src="https://picsum.photos/600/300/?image=25"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-title>
      {{casting.header}}
    </b-card-title>
    <b-card-text>
      <h2>{{ casting.fee }}</h2>
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