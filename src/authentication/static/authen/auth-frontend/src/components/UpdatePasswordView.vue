<template>
  <div>
    <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <b-alert variant="success" show v-if="success">{{ success }}</b-alert>
    <h1>Придумаейте новый пароль</h1>
    <b-form @submit.prevent="onSubmit">
      <b-form-group id="input-group-2" label="Введите новый пароль:" label-for="input-2">
        <b-form-input
            v-model="form.password_first"
            placeholder="Введите пароль"
            type="password"
            required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Повторите пароль:" label-for="input-2">
        <b-form-input
            v-model="form.password_second"
            placeholder="Повторите пароль"
            type="password"
            required
        ></b-form-input>
      </b-form-group>
<b-button type="submit" variant="primary">Сохранить пароль</b-button>
            <b-button type="submit" variant="primary" :to="{name: 'login'}">Войти</b-button>
    </b-form>
  </div>
</template>
<script>
import {useAuthStore} from "../stores/auth";
import {mapActions, mapState} from "pinia/dist/pinia";
import {nextTick} from "vue";


export default {
  name: "UpdatePasswordView",
   props: {
    token: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      form: {
        password_first: "",
        password_second: ""
      },
    }
  },
  methods: {
    ...mapActions(useAuthStore, ['changePassword']),
    async onSubmit() {
      await this.changePassword(this.token, this.form.password_first, this.form.password_second);
      },
    // async handlerSignInGoogle() {
    //   try {
    //     const googleUser = await this.$gAuth.signIn();
    //     if (!googleUser) {
    //       return null;
    //     } else {
    //       // this.email = googleUser.getBasicProfile().getEmail();
    //     }
    //   } catch(error) {
    //     console.log(error);
    //     return null
    //   }
    // }
  },
  computed: {
    ...mapState(useAuthStore, ['error', 'isLoading', 'success']),

  }
}
</script>

<style scoped>

</style>