<template>
  <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <b-alert variant="success" show v-if="success">{{ success }}</b-alert>
  <h1>Настройки</h1>
  <b-card title="Изменить почту">
  <p>Текущая почта: {{ this.user.email }}</p>
  <b-form @submit="updateEmail">
    <b-form-group label="Новая почта">
      <b-form-input v-model="newEmail" type="email" required></b-form-input>
    </b-form-group>
    <b-form-group label="Текущий пароль">
      <b-form-input v-model="currentPassword" type="password" required></b-form-input>
    </b-form-group>
    <b-button type="submit" variant="primary">Сохранить</b-button>
  </b-form>
</b-card>

<b-card title="Изменить пароль">
  <b-form @submit="changePassword">
    <b-form-group label="Нажмите, для получения инструкций на почту">
    </b-form-group>
    <b-button type="submit" variant="primary">Изменить пароль</b-button>
  </b-form>
</b-card>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";
import {changeEmail} from "../services/user_api";

export default {
  name: "SettingsView",
  data() {
    return {
      newEmail: '',
      currentPassword: '',
    }
  },
  computed: mapState(useAuthStore, ['user', 'error', 'isLoading', 'success']),
   methods: {
        ...mapActions(useAuthStore, ['forgetUserPassword', 'changeEmail', 'load']),
    async updateEmail(event) {
      event.preventDefault();
      await this.changeEmail(this.user.id, this.user.email, this.newEmail, this.currentPassword)
      await this.load()
    },
    async changePassword(event) {
      event.preventDefault();
      this.error = null
      await this.forgetUserPassword(this.user.email);
    },
  },
}
</script>

<style scoped>

</style>