<template>
  <h1 v-if="!favorites">Актеры</h1>
  <b-spinner v-if="isLoading"/>
  <b-alert v-if="error" variant="danger" show>{{ error }}</b-alert>
  <b-row>
  <b-col md="4" v-for="actor in results" :key="actor.id">
    <b-list-group-item>
      <img v-if="actor.photo && favorites" :src="`http://127.0.0.1:8000${actor.photo}`" style="width:100%" alt="img" class="card-img-top">
       <img v-if="actor.photo && !favorites" :src="`${actor.photo}`" style="width:100%" alt="img" class="card-img-top">

<!--      <img v-if="actor.photo" :src="`${actor.photo}`" style="width:100%; height:220px; object-fit: cover;" alt="img" class="card-img-top">-->
      <p>{{ actor.full_name }}</p>
      <p>{{ actor.education }}</p>
      <p>{{ actor.skills }}</p>
      <b-button :to="{ name: 'actorcard', params: { id: actor.id }}" variant="primary">Просмотр</b-button>
    </b-list-group-item>
  </b-col>
</b-row>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useActorsStore} from "../stores/actors";
import LikeButtonComponent from "./LikeButtonComponent.vue";
import {useAuthStore} from "../stores/auth";
export default {
  name: "ActorsView.vue",
  props: {
    favorites: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  components: {LikeButtonComponent},
  methods: {...mapActions(useActorsStore, ['load', 'load_favorites']),
  },
  computed: {...mapState(useActorsStore, ['results', 'isLoading', 'error']),
  ...mapState(useAuthStore, ['isAuth'])
  },
  created() {
    if (this.favorites) {
      this.load_favorites()
    } else {
       this.load();
    }
  }
}
</script>

<style scoped>

</style>