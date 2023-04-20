<template>
  <div>
    <p v-if="isLoading" class="alert alert-info">Загрузка...</p>
    <form class="login" @submit.prevent="login">
      <h1>Вход</h1>
      <p>{{ backendStatusText }}</p>
      <label>Email </label>
      <input required v-model="email" type="email" @change="emailHandler" placeholder="email" te/><br><br>
      <label>Password </label>
      <input required v-model="password" @change="passwordHandler" type="password" placeholder="Password"/><br><br>
      <button type="submit" @click="submitForm" :disabled="this.isLoading">Войти</button>
    </form>
  </div>
</template>

<script>

import {API_URL} from "../consts";
import axios from 'axios';

export default {
  name: "Login",
  data() {
    return {
      isLoading: false,
      backendStatusText: '',
      email: '',
      password: ''
    }
  },
  methods: {
    emailHandler(email) {
      this.email = email.target.value
    },
    passwordHandler(password) {
      this.password = password.target.value
    },
    submitForm() {
      this.isLoading = true;
      axios.post(`${API_URL}/api/login/`, {
        'email': `${this.email}`,
        'password': `${this.password}`
      })
          .then(response => {
            if (response.data == 201) {
              this.backendStatusText = 'Вы успешно вошли';
            } else {
              this.backendStatusText = 'Почта или пароль неверны';
            }
            window.location = `/castings`;
          })
          .catch(error => {
            this.backendStatusText = 'Неизвестная ошибка, попробуйте позже';
            console.log(error);
          })
          .finally(() => {
            this.isLoading = false;
          });

    }
  }
}
</script>

<style scoped>

</style>