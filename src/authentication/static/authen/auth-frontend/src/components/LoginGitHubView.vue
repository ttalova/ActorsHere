<script>
import axios from "axios";
import {loginGitHub as loginGitHub_api} from "../services/api";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";
import {nextTick} from "vue";
export default {
  name: "LoginGitHubView",
  data() {
    return {
      email: this.loginGitHub(),
      password: '',
    }
  },
  methods: {
    ...mapActions(useAuthStore, ['login', 'registration', 'setAccess', 'setRefresh']),
    async loginGitHub() {
      const code = new URLSearchParams(window.location.search).get('code');
      const response = await loginGitHub_api(code)
      this.email = response.email
      console.log(this.email)
      if (this.email !== 'error') {
        this.password = response.password
        try {
          await axios.post('http://127.0.0.1:8000/api/registr/', {
          email: this.email,
          password: this.password,
        })
        } catch(e) {
        }
        await this.login(this.email, this.password);
      await nextTick(() => this.$router.push({name: 'profile'}));
      }
    }
  },
  computed: {
    ...mapState(useAuthStore, ['error', 'isLoading', 'isSuccess']),

  }
}
</script>

<template>
<h1 style="text-align: center;">Сейчас вас перенаправят на страницу профиля!</h1>
<b-spinner style="text-align: center;"></b-spinner>
</template>

<style scoped>
</style>