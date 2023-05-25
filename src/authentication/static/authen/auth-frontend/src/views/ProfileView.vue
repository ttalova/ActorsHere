<template>
  <b-row>
    <b-col md="9">
      <div v-if="!this.user.type_of_profile" class="text-center my-5">
        <b-button @click="createActorForm">
          Создать анкету соискателя
        </b-button>

        <b-button @click="createEmployerForm" id="tooltip-target-1">
          Создать анкету нанимателя
        </b-button>
        <b-tooltip target="tooltip-target-1" triggers="hover">
        </b-tooltip>
      </div>
    </b-col>
    <b-col md="3">
      <p class="mt-5"><b>Почта:</b> {{ user.email }}</p>
      <b-btn v-if="this.user.type_of_profile" variant="outline-primary" @click="clickHandler">Редактировать анкету</b-btn>
      <b-btn class="mt-3" variant="outline-primary" @click="logoutClickHandler">Выйти</b-btn>
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
       this.$router.push({name: "menu"});
    },
    createActorForm() {
      this.$router.push({name: "actorForm"});
    },
    createEmployerForm() {
      this.$router.push({name: "employerForm"});
    },
    clickHandler() {
      if (this.user.type_of_profile === 'actor') {
          this.$router.push({name: "actorForm"});
      } else {
        this.$router.push({name: "employerForm"});
      }
    }
  }
}
</script>

<style scoped>

</style>