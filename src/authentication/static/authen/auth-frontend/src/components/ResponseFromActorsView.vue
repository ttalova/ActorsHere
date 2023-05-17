<template>
  <h1>Актеры, откликнувшиеся на ваши кастинги</h1>
  <b-form @submit.prevent="onSubmit">
    <div>
      <b-form-group
              label="Выберите кастинг:"
          >
      <b-form-select
          v-model="selected"
          :options="castings"
          class="mb-3"
          value-field="value"
          text-field="text"
          disabled-field="notEnabled"
          @change="onSubmit"
      ></b-form-select>
        </b-form-group>
    </div>
</b-form>
  <h2 v-if="!this.results.length && this.selected">Пока никто не откликнулся на этот кастинг!</h2>
  <h2 v-if="!this.results.length && !this.selected">Выберите кастинг!</h2>
  <b-list-group>
    <b-list-group-item v-for="actor in results" :key="actor.id">
      <p>{{ actor.full_name }}</p>
      <p>{{ actor.education }}</p>
      <p>{{ actor.skills }}</p>
    <b-button :to="{ name: 'actorcard', params: { id: actor.id }}" variant="primary">Просмотр</b-button>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {useAuthStore} from "../stores/auth";

export default {
  name: "ResponseFromActorsView",
  data() {
    return {
      selected: null,
      options: []
    }
  },
  created() {
    this.load()
  },
  computed: {
    ...mapState(useCastingsStore, ['isLoading', 'error', 'results']),
  ...mapState(useAuthStore, ['user']),
  castings() {
      return [
        {value: null, text: "Выберите кастинг"},
        ...this.options.map(x => ({value: x.id, text: x.header}))
      ]
    },},
  methods: {
    ...mapActions(useCastingsStore, ['getCastings', 'listOfActorsResponse']),
    async load() {
      this.isLoading = true
      try {
          this.options = await this.getCastings()
      } catch (e) {
        this.error = e.message
      }
      this.isLoading = false
    },

    async onSubmit() {
      if (this.selected) {
        this.results = await this.listOfActorsResponse(this.selected)
      }
      }
  }
}
</script>

<style scoped>

</style>



