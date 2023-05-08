import {createPinia} from 'pinia'
import Vue, {createApp} from '@vue/compat';
import BootstrapVue from "bootstrap-vue";
import App from './App.vue'
import router from './router'
// import GSignInButton from 'vue-google-signin-button'
import GAuth from "vue3-google-oauth2";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


const app = createApp(App)

app.use(createPinia())
app.use(router)
Vue.use(BootstrapVue)
// app.use(GAuth, {
//     clientId: '267190297401-qfarek568fc4mbbnem1a5b0kdm6oftvj.apps.googleusercontent.com',
//     scope: 'email',
// })
// Vue.use(GSignInButton)

app.mount('#app')
