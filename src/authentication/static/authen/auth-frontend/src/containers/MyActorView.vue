<template>
  <div>
    <b-card
        img-top
        tag="article"
        style="max-width: 200rem;"
        class="mb-2"
    >
      <img v-if="this.results.photo" :src="`${this.results.photo}`" style="width:50%" alt="img" class="card-img-top">
      <b-card-title>
        {{ this.results.full_name }}
      </b-card-title>
      <b-card-text>
        <p><strong>Дата рождения:</strong> {{ this.results.birthdate }}</p>
        <p><strong>Параметры фигуры:</strong> {{ this.results.figure_parameters }}</p>
        <p><strong>Рост:</strong> {{ this.results.height }} см</p>
        <p><strong>Вес:</strong> {{ this.results.weight }} кг</p>
        <p><strong>Размер одежды:</strong> {{ this.results.clothing_size }}</p>
        <p><strong>Размер обуви:</strong> {{ this.results.shoe_size }}</p>
        <p><strong>Цвет глаз:</strong> {{ this.results.eye_color }}</p>
        <p><strong>Тип телосложения:</strong> {{ this.results.body_type }}</p>
        <p><strong>Пол:</strong> {{ this.results.sex }}</p>
        <p><strong>Тип лица:</strong> {{ this.results.face_type }}</p>
        <p><strong>Цвет волос:</strong> {{ this.results.hair_color }}</p>
        <p><strong>Длина волос:</strong> {{ this.results.hair_length }}</p>
        <p><strong>Тембр голоса:</strong> {{ this.results.voice_timbre }}</p>
        <p><strong>Цвет кожи:</strong> {{ this.results.skin_color }}</p>
        <p><strong>Татуировки:</strong> {{ this.results.tattoo }}</p>
        <p><strong>Пирсинг:</strong> {{ this.results.piercing }}</p>
        <p><strong>Образование:</strong> {{ this.results.education }}</p>
        <p><strong>Владение языками:</strong> {{ this.results.language_proficiency }}</p>
        <p><strong>Навыки:</strong> {{ this.results.skills }}</p>
        <p><strong>Готовность к переезду:</strong> {{ this.results.willing_to_relocate ? 'Да' : 'Нет' }}</p>
        <p><strong>Наличие загранпаспорта:</strong> {{ this.results.international_passport ? 'Да' : 'Нет' }}</p>
        <p><strong>Наличие водительских прав:</strong> {{ this.results.driver_license ? 'Да' : 'Нет' }}</p>
        <p><strong>Телефон:</strong> {{ this.results.phone_number }}</p>
        <p><strong>Email:</strong> {{ this.results.email }}</p>
        <p><strong>Социальные сети:</strong> {{ this.results.social_network }}</p>
        <p><strong>Теги:</strong> {{ this.results.tag }}</p>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import LikeButtonComponent from "../components/LikeButtonComponent.vue";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";
import {useActorsStore} from "../stores/actors";

export default {
  name: "MyActorView",
  components: {LikeButtonComponent},
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      results: [],
      isLoading: false,
      error: null,
      canEdit: false,
      like: false,
      like_id: null
    }
  },
  created() {
    this.load(this.id)
  },
  methods: {
    ...mapActions(useActorsStore, ['load', 'actor_be_liked', 'LikedActor', 'DisLikedActor', 'getActorById']),
    async load(id) {
      this.isLoading = true;
      this.error = null;
      try {
        this.results = await this.getActorById(id);
      } catch (e) {
        this.error = e.message
      }
      this.isLoading = false;
    },
  },
  computed: {
    ...mapState(useActorsStore, ['isLoading', 'error', 'results', 'like_info']),
    ...mapState(useAuthStore, ['user', 'isAuth'])
  },
}
</script>

<style scoped>

</style>