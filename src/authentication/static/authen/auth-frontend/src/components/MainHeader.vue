<template>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">ActorsHere</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item :to="{name: 'menu'}">Актеры и Кастинги</b-nav-item>
        <b-nav-item v-if="isAuth && isEmployer" :to="{name: 'castingform'}">Создать кастинг</b-nav-item>
        <b-nav-item v-if="!isAuth" :to="{name: 'login'}">Вход</b-nav-item>
        <b-nav-item v-if="!isAuth" :to="{name: 'registration'}">Регистрация</b-nav-item>


      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <b-nav-item v-if="isAuth">Профиль</b-nav-item>
          </template>
          <b-dropdown-item :to="{name: 'profile'}">Профиль</b-dropdown-item>
          <b-dropdown-item v-if="isAuth" :to="{name: 'favorites'}">Избранное</b-dropdown-item>
          <b-dropdown-item v-if="isAuth" :to="{name: 'notifications'}">Уведомления</b-dropdown-item>
          <b-dropdown-item v-if="isAuth && isStaff" :to="{name: 'moderation'}">Модерация</b-dropdown-item>
          <b-dropdown-item v-if="isAuth && isActor" :to="{name: 'myResponses'}">Мои отклики</b-dropdown-item>
          <b-dropdown-item v-if="isAuth && isEmployer" :to="{name: 'mycastings'}">Мои кастинги</b-dropdown-item>
          <b-dropdown-item v-if="isAuth && isEmployer" :to="{name: 'responsefromactors'}">Отклики</b-dropdown-item>
          <b-dropdown-item v-if="isAuth" :to="{name: 'settings'}">Настройки</b-dropdown-item>
          <b-dropdown-item v-if="isAuth" v-on:click="logoutClickHandler">Выход</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import {useAuthStore} from "../stores/auth";
import {mapActions, mapState} from "pinia/dist/pinia";

export default {
  name: "MainHeader",
  computed: {
    ...mapState(useAuthStore, ['user', 'isAuth', 'isStaff', 'isActor', 'isEmployer'])
  },
  methods: {
    ...mapActions(useAuthStore, ['logout']),
    logoutClickHandler() {
      this.logout();
      this.$router.push({name: "login"});
    }
  }
}
</script>

<style scoped>

</style>