<template>
  <div>
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


      <b-button type="submit" variant="primary">Зарегистрироваться</b-button>
      <p>{{ backendStatusText }}</p>
    </b-form>
  </div>
</template>

<script>

import {API_URL} from "../consts";
import axios from 'axios';

export default {
  name: "Auth",
  data() {
    return {
      isLoading: false,
      backendStatusText: '',
      form: {
        email: '',
        password: ''
      },
    }
  },
  methods: {
    onSubmit() {
      this.isLoading = true;
      console.log(this.form['email'])
      axios.post(`${API_URL}/api/registr/`, {
        'email': `${this.form['email']}`,
        'password': `${this.form['password']}`
      })
          .then(response => {
            if (response.status == 201) {
              this.backendStatusText = 'Вы успешно зарегистрированы';
              window.location = `/castings`;
            } else {
              this.backendStatusText = 'Аккаунт с такой почтой уже существует';
            }
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
