<template>
  <main>
    <h1>Актеры </h1>
    <b-row>
      <b-col md="9">
            <ActorsView/>
      </b-col>
      <b-col md="3">
        <FiltersActorContainer @submit="submit"/>
      </b-col>
    </b-row>
  </main>
</template>

<script>
import ActorsView from "../components/ActorsView.vue";
import {useActorsStore} from "../stores/actors";
import {mapState} from "pinia/dist/pinia";
import FiltersActorContainer from "../containers/SearchActorContainer.vue";
export default {
  name: "MainView",
  components: {FiltersActorContainer, ActorsView},
  computed: mapState(useActorsStore, ['isLoading']),
  methods: {
    submit(params) {
      this.$router.push({query: params})
    }
  }
}
</script>

<style scoped>

</style>