<template>
  <div>
    <b-alert variant="success" show v-if="isSuccess">Вы успешно зарегистрированы!</b-alert>
    <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <b-form @submit.prevent="onSubmit">
      <h1>Регистрация</h1>
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


      <b-button type="submit" variant="primary">Зарегистрироваться</b-button>
    </b-form>
  </div>
</template>

<script>
import {useRegistrStore} from "../stores/registr";
import {mapActions, mapState} from "pinia/dist/pinia";
export default {
  name: "Registration",
  data() {
    return {
      form: {
        email: "",
        password: ""
      }
    }
  },
  methods: {
    ...mapActions(useRegistrStore, ['registration']),
    async onSubmit() {
      await this.registration(this.form.email, this.form.password);
    }
  },
  computed: {
    ...mapState(useRegistrStore, ['error', 'isLoading', 'isSuccess']),

  }
}
</script>

<style scoped>

</style>
