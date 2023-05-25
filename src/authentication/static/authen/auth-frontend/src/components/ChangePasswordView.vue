<template>
  <div>
    <b-alert variant="danger" show v-if="error">Такой аккаунт не существует!</b-alert>
    <b-alert variant="success" show v-if="success">{{ success }}</b-alert>
    <h1>Восстановление пароля</h1>
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
      <b-button type="submit" variant="primary">Ввод</b-button>
    </b-form>
  </div>
</template>
<script>
import {inject} from 'vue';
import {useAuthStore} from "../stores/auth";
import {mapActions, mapState} from "pinia/dist/pinia";
import {nextTick} from "vue";


export default {
  name: "ChangePasswordView",
  data() {
    return {
      form: {
        email: "",
      },
    }
  },
  methods: {
    ...mapActions(useAuthStore, ['forgetUserPassword']),
    async onSubmit() {
      this.error = null
      await this.forgetUserPassword(this.form.email);
     },
  },
  computed: {
    ...mapState(useAuthStore, ['error', 'isLoading', 'success']),

  }
}
</script>

<style scoped>

</style>