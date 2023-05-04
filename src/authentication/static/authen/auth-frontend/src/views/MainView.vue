<template>
  <div class="text-center my-3">
  <b-button @click.prevent="getList = 'actors'">
    Актеры
  </b-button>

  <b-button @click.prevent="getList = 'castings'">
    Кастинги
  </b-button>
</div>
  <main>
    <b-row>
      <b-col md="9">
            <ActorsView v-if="getList==='actors'"/>
        <CastingsView v-if="getList==='castings'"/>
      </b-col>
      <b-col md="3">
        <FiltersActorContainer v-if="getList==='actors'" @submit="submit"/>
      </b-col>
    </b-row>
  </main>
</template>

<script>
import ActorsView from "../components/ActorsView.vue";
import {useActorsStore} from "../stores/actors";
import {mapState} from "pinia/dist/pinia";
import FiltersActorContainer from "../containers/SearchActorContainer.vue";
import CastingsView from "../components/CastingsView.vue";
export default {
  name: "MainView",
  data() {
    return {
      getList: 'actors'
    }
  },
  components: {CastingsView, FiltersActorContainer, ActorsView},
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