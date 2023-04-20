import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';
import App from './App.vue'
import router from './router'
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import TabMenu from 'primevue/tabmenu';
import Button from "primevue/button"


import './assets/main.css'
import "primevue/resources/themes/lara-light-indigo/theme.css";
import "primevue/resources/primevue.min.css";

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue);
app.use(ToastService);
app.mount('#app')
app.component('TabMenu', TabMenu);
app.component('Button', Button);