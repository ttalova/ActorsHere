<template>
  <b-card>
    <b-form action="" @submit.prevent="load">
      <b-input v-model="search" placeholder="Поиск"/>
      <FilterActorContainer class="mt-3"
                            :model-value="tagId"
                            @update:model-value="tagId=$event"/>
      <b-button block class="mt-3" type="submit" variant="outline-primary">Найти</b-button>
    </b-form>
  </b-card>
</template>

<script>
import FilterActorContainer from "./FilterActorContainer.vue";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useActorsStore} from "../stores/actors";

export default {
  name: "SearchActorContainer",
  components: {FilterActorContainer},
  methods: {
    ...mapActions(useActorsStore, ['setParameter', 'setParameters', 'load']),
    submit() {
      const params = {}
      Object.keys(this.params).forEach(key => {
        if (this.params[key]) {
          params[key] = this.params[key];
        }
      })
      this.$router.push({query: params})
    },
    loadDataFromRoute(route) {
      this.setParameters(route.query)
      this.load()
    }
  },
  created() {
    this.loadDataFromRoute(this.$route)
  },
  watch: {
    '$route': function (route) {
      this.loadDataFromRoute(route)
    }
  },
  computed: {
    ...mapState(useActorsStore, ['params']),
    search: {
      get() {
        return this.params.search;
      },
      set(value) {
        this.setParameter('search', value)
      }
    },
    tagId: {
      get() {
        return this.params.tag_id || null;
      },
      set(value) {
        this.setParameter('tag_id', value)
      }
    }
  }
}
</script>

<style scoped>

</style>