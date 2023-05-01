<template>
  <b-row>
    <b-col md="9">
      <div v-if="!user.type_of_profile" class="text-center my-5">
        <b-button>
          Создать анкету нанимателя
        </b-button>

        <b-button id="tooltip-target-1">
           Создать анкету нанимателя
        </b-button>
        <b-tooltip target="tooltip-target-1" triggers="hover">
        </b-tooltip>
      </div>
    </b-col>
    <b-col md="3">
      <p><b>Почта:</b> {{ user.email }}</p>
      <b-btn variant="outline-primary" @click="logoutClickHandler">Выйти</b-btn>
    </b-col>
  </b-row>

</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";

export default {
  name: "ProfileView",
  computed: mapState(useAuthStore, ['user']),
  methods: {
    ...mapActions(useAuthStore, ['logout']),
    logoutClickHandler() {
      this.logout();
      this.$router.push({name: "actors"});
    }
  }
}
</script>

<style scoped>

</style>