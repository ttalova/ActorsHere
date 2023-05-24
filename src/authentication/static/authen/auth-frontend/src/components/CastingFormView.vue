<template>
  <div>
    <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <h1>Создайте кастинг!</h1>
    <b-form @submit.prevent="onSubmit" enctype="multipart/form-data">
      <b-row>
        <b-col md="6">
          <input type="hidden" name="hidden_field" v-model="form.id">
          <b-form-group
              label="Название:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.header"
                type="text"
                placeholder="Введите название"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Фотография:">
            <b-form-file
                name="photo"
                v-model="form.photo"
                :state="Boolean(form.photo)"
                placeholder="Выберите файл или перенесите его сюда..."
                drop-placeholder="Drop file here..."
            ></b-form-file>
          </b-form-group>

          <b-form-group
              label="Тип проекта:"
              label-for="input-1"
          >
            <b-form-select v-model="form.project_type" :options="project_type"></b-form-select>
          </b-form-group>

          <b-form-group id="input-group-2" label="Гонорар:" label-for="input-2">
            <b-form-input
                v-model="form.fee"
                type="text"
                placeholder="Оплата"
                required
            ></b-form-input>
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
              label="Пол:"
              label-for="input-1"
          >
            <b-form-select v-model="form.sex" :options="sex"></b-form-select>
          </b-form-group>

          <b-form-group id="input-group-2" label="Опыт:" label-for="input-2">
            <b-form-input
                v-model="form.experience"
                type="text"
                placeholder="Требуемый опыт"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Почта:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.contact_email"
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
      </b-row>
      <hr>
      <b-row>
        <b-col md="6">
          <b-form-group id="input-group-2" label="Описание кандидатов:" label-for="input-2">
            <b-form-input
                v-model="form.actor_type_description"
                type="text"
                placeholder="Умный"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Минимальный возраст актера:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.min_actor_age"
                type="number"
                placeholder="39"
                min="1"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Максимальный возраст актера:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.max_actor_age"
                type="number"
                placeholder="99"
                min="1"
                required
            ></b-form-input>
          </b-form-group>

        </b-col>
        <b-col md="6">
          <b-form-group
              label="Тег:"
              label-for="input-1"
          >
            <b-form-select v-model="form.tag" :options="tag"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Город:"
              label-for="input-1"
          >
            <b-form-select v-model="form.city" :options="city"></b-form-select>
          </b-form-group>

          <div>
            <label for="example-datepicker">Прием заявок до:</label>
            <b-form-datepicker id="example-datepicker" v-model="form.end_of_application"
                               class="mb-2"></b-form-datepicker>
          </div>

          <div>
            <label for="example-datepicker-2">День проведения кастинга:</label>
            <b-form-datepicker id="example-datepicker-2" v-model="form.date_of_event" class="mb-2"></b-form-datepicker>
          </div>


        </b-col>
      </b-row>
      <hr>
      <b-row>
        <b-col md="6">
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
import {getCities, getProjectTypes, getTags} from "../services/api";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {nextTick} from "vue";
import {useAuthStore} from "../stores/auth";

export default {
  name: "CastingFormView",
  data() {
    return {
      form: {},
      tags: [],
      cities: [],
      types_of_project: [],

    }
  },
  props: {
    id: {
      type: String,
      required: false
    }
  },
  created() {
    this.loadthis();
  },
  methods: {
    async loadthis() {
      try {
        if (this.id) {
          this.form = await this.load(this.id)
        }
        this.cities = await getCities()
        this.tags = await getTags()
        this.types_of_project = await getProjectTypes()
      } catch (e) {
        console.log(e)
      }
    },
    ...mapActions(useCastingsStore, ['createCasting', 'getCasting', 'updateCasting', 'deleteCasting', 'load']),
    async onSubmit() {
      try {
        const formData = new FormData();
        for (const key in this.form) {
          formData.append(key, this.form[key]);
        }
        console.log('uppppp')
        if (formData.get('id')) {
          console.log('update')
          await this.updateCasting(formData);
        } else {
          console.log('create')
          formData.append('casting_owner', this.user.id);
          await this.createCasting(formData);
        }
        await nextTick(() => this.$router.push({name: 'menu'}));
      } catch (e) {
        this.error = e.message
      }
    },
    async onDelete() {
      try {
        await this.deleteCasting(this.form['id'])
        await nextTick(() => this.$router.push({name: 'menu'}));
      } catch (e) {
        console.log(e)
      }
    }
  },
  computed: {
    ...mapState(useAuthStore, ['user']),
    ...mapState(useCastingsStore, ['isLoading', 'error', 'form']),
    city() {
      return [
        {value: null, text: "Выберите город"},
        ...this.cities.map(x => ({value: x.id, text: x.name}))
      ]
    },
    tag() {
      return [
        {value: null, text: "Выберите тег"},
        ...this.tags.map(x => ({value: x.id, text: x.title}))
      ]
    },
    sex() {
      return [
        {value: null, text: "Выберите пол"},
        {value: "male", text: "Мужской"},
        {value: "female", text: "Женский"},
      ]
    },
    project_type() {
      return [
        {value: null, text: "Выберите тип проекта"},
        ...this.types_of_project.map(x => ({value: x.id, text: x.type_of_project}))
      ]
    },
  }
}
</script>

<style scoped>

</style>