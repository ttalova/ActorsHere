<template>
  <div>
    <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <h1>Вход</h1>
    <b-form @submit.prevent="onSubmit">
      <b-form-group
          id="input-group-1"
          label="Электронная почта:"
          label-for="input-1"
      >
        <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            placeholder="Введите почту"
            required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Пароль:" label-for="input-2">
        <b-form-input
            id="input-2"
            v-model="form.password"
            placeholder="Введите пароль"
            type="password"
            required
        ></b-form-input>
      </b-form-group>


      <b-button type="submit" variant="primary">Войти</b-button>
    </b-form>
  </div>
</template>
<script>

import {useAuthStore} from "../stores/auth";
import {mapActions, mapState} from "pinia/dist/pinia";
import {nextTick} from "vue";


export default {
  name: "Login",
  data() {
    return {
      form: {
        email: "",
        password: ""
      },
    }
  },
  methods: {
    ...mapActions(useAuthStore, ['login', 'setAccess', 'setRefresh']),
    async onSubmit() {
      await this.login(this.form.email, this.form.password);
      await nextTick(() =>this.$router.push({name: 'profile'}));
    }
  },
  computed: {
    ...mapState(useAuthStore, ['error', 'isLoading']),

  }
}
</script>

<style scoped>

</style>