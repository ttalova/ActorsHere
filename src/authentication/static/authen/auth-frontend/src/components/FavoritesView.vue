<template>
<h1>Избранное</h1>
   <b-button @click.prevent="getList = 'actors'">
    Актеры
  </b-button>

  <b-button @click.prevent="getList = 'castings'">
    Кастинги
  </b-button>
  <main>
    <b-row>
      <b-col md="9">
            <ActorsView v-if="getList==='actors'" :favorites="true"/>
        <CastingsView v-if="getList==='castings'" :favorites="true"/>
      </b-col>
<!--      <b-col md="3">-->
<!--        <SearchActorContainer v-if="getList==='actors'" @submit="submit"/>-->
<!--      </b-col>-->
    </b-row>
  </main>
</template>

<script>
import ActorsView from "./ActorsView.vue";
import CastingsView from "./CastingsView.vue";
import {mapState} from "pinia/dist/pinia";
import {useActorsStore} from "../stores/actors";
import FilterActorContainer from "../containers/FilterActorContainer.vue";
import SearchActorContainer from "../containers/SearchActorContainer.vue";
import {useAuthStore} from "../stores/auth";
export default {
  name: "FavoritesView",
  data() {
    return {
      getList: 'actors'
    }
  },
  components: {SearchActorContainer, FilterActorContainer, CastingsView, ActorsView},
  computed: {...mapState(useActorsStore, ['isLoading']),
  ...mapState(useAuthStore, ['user']),
  },
  methods: {
    submit(params) {
      this.$router.push({query: params})
    }
  }
}
</script>

<style scoped>

</style>