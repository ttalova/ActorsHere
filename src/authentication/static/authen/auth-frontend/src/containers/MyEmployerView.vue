<template>
  <div v-if="form">
    <h2>Наниматель: {{ form.company_name }}</h2>
    <p><b>Специализация:</b> {{ form.company_specialization }}</p>
    <p><b>Описание:</b> {{ form.description }}</p>
    <p><b>Примерное местонахождение:</b> {{ form.approximate_location }}</p>
    <p><b>Номер телефона:</b> {{ form.phone_number }}</p>
    <p><b>Дополнительный номер телефона:</b> {{ form.additional_phone_number }}</p>
    <p><b>Website:</b> <a :href="form.webside" target="_blank">{{ form.webside }}</a></p>
    <p><b>Email:</b> {{ form.email }}</p>
    <p><b>Социальные сети:</b> {{ form.social_network }}</p>
  </div>
</template>

<script>
import {getCities, getTags} from "../services/api";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useActorsStore} from "../stores/actors";
import {nextTick} from "vue";
import {useAuthStore} from "../stores/auth";
import {useEmployersStore} from "../stores/employers";

export default {
  name: "MyEmployerView",
  data() {
    return {
      form: {},
      cities: []
    }
  },
  created() {
    this.load();
  },
  methods: {
    async load() {
      try {
        if (this.user.type_of_profile === 'employer') {
          this.form = await this.getMyFormEmployer(this.user.id)
        }
        this.cities = await getCities()
      } catch (e) {
        console.log(e)
      }
    },
    ...mapActions(useEmployersStore, ['createemployer', 'getMyFormEmployer', 'updateformemployer', 'deleteMyFormEmployer']),
    async onSubmit() {
      try {
        if (this.form['id']) {
          await this.updateformemployer(this.form);
        } else {
          this.form['user'] = this.user.id
          await this.createemployer(this.form);
        }
        await nextTick(() => this.$router.push({name: 'profile'}));
        location.reload()
      } catch (e) {
        this.error = e.message
      }
    },
    async onDelete() {
      try {
        await this.deleteMyFormEmployer(this.form['id'])
        await nextTick(() => this.$router.push({name: 'menu'}));
        location.reload()
      } catch (e) {
        console.log(e)
      }
    }
  },
  computed: {
    ...mapState(useAuthStore, ['user']),
    ...mapState(useEmployersStore, ['isLoading', 'error', 'form']),
  }
}
</script>

<style scoped>

</style>