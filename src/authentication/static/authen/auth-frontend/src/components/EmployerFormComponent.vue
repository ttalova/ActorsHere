<template>
  <div>
    <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <h1>Заполните анкету нанимателя!</h1>
    <b-form @submit.prevent="onSubmit">
      <b-row>
        <b-col md="6">
          <input type="hidden" name="hidden_field" v-model="form.id">
          <b-form-group
              label="Название организации:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.company_name"
                type="text"
                placeholder="Введите название"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Специализация компании:"
              label-for="input-1"
          >
            <b-form-select v-model="form.company_specialization" :options="company_specialization"></b-form-select>
          </b-form-group>

          <b-form-group id="input-group-2" label="Описание:" label-for="input-2">
            <b-form-input
                v-model="form.description"
                  type="text"
                placeholder="Краткое описание организации"
                required
            ></b-form-input>
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group
              label="Примерное местоположение:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.approximate_location"
                type="text"
                placeholder="Южное Бутово"
                required
            ></b-form-input>
          </b-form-group>
        </b-col>
      </b-row>
      <hr>
      <b-row>
        <b-col md="6">
        </b-col>
        <b-col md="6">
          <b-form-group
              label="Город:"
              label-for="input-1"
          >
            <b-form-select v-model="form.city" :options="city"></b-form-select>
          </b-form-group>
        </b-col>
      </b-row>
      <hr>
      <b-row>
        <b-col md="6">
          <b-form-group
              label="Веб-сайт:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.webside"
                type="url"
                placeholder=""
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Номер телефона:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.phone_number"
                type="text"
                placeholder=""
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Дополнительный номер телефона:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.additional_phone_number"
                type="text"
                placeholder=""
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Почта:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.email"
                type="email"
                placeholder="example@gmail.com"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Социальные сети:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.social_network"
                type="text"
                placeholder=""
            ></b-form-input>
          </b-form-group>

        </b-col>
        <b-col md="6">

        </b-col>

      </b-row>

      <b-button type="submit" variant="primary" @click.prevent="onSubmit">Сохранить</b-button>
      <b-button v-if="this.form['id']" type="submit" variant="primary" @click.prevent="onDelete">Удалить анкету
      </b-button>
    </b-form>
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
  name: "EmployerFormComponent",
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
    city() {
      return [
        {value: null, text: "Выберите город"},
        ...this.cities.map(x => ({value: x.id, text: x.name}))
      ]
    },
    company_specialization() {
      return [
        {value: null, text: "Выберите специализацию"},
        {value: "acting_agency",text: "Актерское агенство"},
        {value: "film_company", text: "Кинокомпания"},
        {value: "film_studio", text: "Киностудия"},
        {value: "casting_agency", text: "Кастинг агенство"},
        {value: "concert_agency", text: "Концертное агенство"},
        {value: "casting_director", text: "Кастинг-директор"},
        {value: "modeling_agency", text: "Модельное агенство"},
        {value: "music_studio", text: "Музыкальная студия"},
        {value: "selection", text: "Подбор кадров"},
        {value: "producer", text: "Продюсер"},
        {value: "director", text: "Режиссер"},
        {value: "advertising_agency", text: "Рекламное агенство"},
        {value: "tv_channel", text: "Телеканал"},
        {value: "photo_studio", text: "Фото студия"},
        {value: "other", text: "Другое"},
      ]
    }
  }
}
</script>

<style scoped>

</style>