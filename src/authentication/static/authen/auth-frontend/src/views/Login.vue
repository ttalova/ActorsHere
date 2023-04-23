<template>
<div>
  <b-alert variant="danger" show v-if="error">{{error}}</b-alert>
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

import {API_URL} from "../consts";
import axios from 'axios';
import {login} from "../services/api";

export default {
  name: "Login",
  data() {
    return {
      isLoading: false,
      error: null,
      form: {
          email: "",
          password: ""
        },
    }
  },
  methods: {
    async onSubmit() {
      this.isLoading = true;
      try {
        const token = await login(this.form.email, this.form.password);
        storeToken(token);
      }
      catch (e) {
        this.error = e.message;
      }
      this.isLoading = false;


    }
  }
}
</script>

<style scoped>

</style>