<template>
  <div>
    <b-alert variant="danger" show v-if="error">{{ error }}</b-alert>
    <h1>Заполните анкету актера!</h1>
    <b-form @submit.prevent="onSubmit" enctype="multipart/form-data">
      <b-row>
        <b-col md="6">
          <input type="hidden" name="hidden_field" v-model="form.id">
          <b-form-group
              label="ФИО:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.full_name"
                type="text"
                placeholder="Введите ваше полное имя"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Ваша фотография:">
            <b-form-file
                name="photo"
                v-model="form.photo"
                :state="Boolean(form.photo)"
                placeholder="Выберите файл или перенесите его сюда..."
                drop-placeholder="Drop file here..."
            ></b-form-file>
          </b-form-group>

          <div>
            <label for="example-datepicker">Дата рождения:</label>
            <b-form-datepicker id="example-datepicker" v-model="form.birthdate" class="mb-2"></b-form-datepicker>
          </div>

          <b-form-group id="input-group-2" label="Параметры фигуры:" label-for="input-2">
            <b-form-input
                v-model="form.figure_parameters"
                placeholder="90 60 90"
                required
            ></b-form-input>
          </b-form-group>
        </b-col>
        <b-col md="6">
          <b-form-group
              label="Рост:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.height"
                type="number"
                placeholder="170"
                min="1"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Вес:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.weight"
                type="number"
                placeholder="65"
                min="1"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Размер одежды:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.clothing_size"
                type="number"
                placeholder="42"
                min="1"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Размер обуви:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.shoe_size"
                type="number"
                placeholder="39"
                min="1"
                required
            ></b-form-input>
          </b-form-group>
        </b-col>
      </b-row>
      <hr>
      <b-row>
        <b-col md="6">
          <b-form-group
              label="Цвет глаз:"
              label-for="input-1"
          >
            <b-form-select v-model="form.eye_color" :options="eye_color"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Телосложение:"
              label-for="input-1"
          >
            <b-form-select v-model="form.body_type" :options="body_type"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Пол:"
              label-for="input-1"
          >
            <b-form-select v-model="form.sex" :options="sex"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Тип лица:"
              label-for="input-1"
          >
            <b-form-select v-model="form.face_type" :options="face_type"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Цвет волос:"
              label-for="input-1"
          >
            <b-form-select v-model="form.hair_color" :options="hair_color"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Длина волос:"
              label-for="input-1"
          >
            <b-form-select v-model="form.hair_length" :options="hair_length"></b-form-select>
          </b-form-group>
        </b-col>
        <b-col md="6">

          <b-form-group
              label="Тембр голоса:"
              label-for="input-1"
          >
            <b-form-select v-model="form.voice_timbre" :options="voice_timbre"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Цвет кожи:"
              label-for="input-1"
          >
            <b-form-select v-model="form.skin_color" :options="skin_color"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Город:"
              label-for="input-1"
          >
            <b-form-select v-model="form.city" :options="city"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Наличие татуировок:"
              label-for="input-1"
          >
            <b-form-select v-model="form.tattoo" :options="is_not"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Наличие пирсинга:"
              label-for="input-1"
          >
            <b-form-select v-model="form.piercing" :options="is_not"></b-form-select>
          </b-form-group>


        </b-col>
      </b-row>
      <hr>
      <b-row>
        <b-col md="6">
          <b-form-group
              label="Образование:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.education"
                type="text"
                placeholder="Название образовательной огранизации"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Владение иностранными языками:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.language_proficiency"
                type="text"
                placeholder="Английский В1"
                required
            ></b-form-input>
          </b-form-group>

          <b-form-group
              label="Профессиональный навыки:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.skills"
                type="text"
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
<!--          <b-form-group label="Теги">-->
<!--            <b-form-select v-model="form.tag" :options="tag" multiple :select-size="4"></b-form-select>-->
<!--          </b-form-group>-->
          <b-form-group
              label="Тег:"
              label-for="input-1"
          >
            <b-form-select v-model="form.tag" :options="tag"></b-form-select>
          </b-form-group>
          <b-form-group
              label="Готов к переезду:"
              label-for="input-1"
          >
            <b-form-select v-model="form.willing_to_relocate" :options="bool_choices"></b-form-select>
          </b-form-group>
          <b-form-group
              label="Загран. паспорт:"
              label-for="input-1"
          >
            <b-form-select v-model="form.international_passport" :options="bool_choices"></b-form-select>
          </b-form-group>
          <b-form-group
              label="Водительские права:"
              label-for="input-1"
          >
            <b-form-select v-model="form.driver_license" :options="bool_choices"></b-form-select>
          </b-form-group>

        </b-col>

      </b-row>

      <b-button type="submit" variant="primary" @click.prevent="onSubmit">Сохранить</b-button>
      <b-button v-if="this.form['id']" type="submit" variant="primary" @click.prevent="onDelete">Удалить анкету</b-button>
    </b-form>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";
import {nextTick} from "vue";
import {useActorsStore} from "../stores/actors";
import {getActorForm, getCities, getTags} from "../services/api";

export default {
  name: "ActorFormComponent",
  data() {
    return {
      form: {
      },
      tags: [],
      cities: []
    }
  },
  created() {
    this.load();
  },
  methods: {
    async load() {
      try {
        if (this.user.type_of_profile === 'actor') {
          this.form = await this.getMyForm(this.user.id)
        }
        this.tags = await getTags();
        this.cities = await getCities()
      } catch(e) {
        console.log(e)
      }
    },
    ...mapActions(useActorsStore, ['createactor', 'getMyForm', 'updateformactor', 'deleteMyForm']),
    // async onSubmit() {
    //   try {
    //     const formData = new FormData();
    //     for (const key in this.form) {
    //       formData.append(key, this.form[key]);
    //     }
    //     if (formData.get('id')) {
    //       await this.updateformactor(formData);
    //     } else {
    //       formData.append('user', this.user.id);
    //       await this.createactor(formData);
    //     }
    //     await nextTick(() => this.$router.push({name: 'profile'}));
    //   } catch(e) {
    //     this.error = e.message
    //   }
    //   },
    async onSubmit() {
      try {
        if (this.form['id']) {
          await this.updateformactor(this.form);
        } else {
          this.form['user'] = this.user.id
          await this.createactor(this.form);
        }
        await nextTick(() => this.$router.push({name: 'profile'}));
        location.reload()
      } catch(e) {
        this.error = e.message
      }
      },
    async onDelete() {
      try {
        await this.deleteMyForm(this.form['id'])
        await nextTick(() =>this.$router.push({name: 'menu'}));
        location.reload()
      } catch(e) {
        console.log(e)
      }
    }
  },
  computed: {
    ...mapState(useAuthStore, ['user']),
    ...mapState(useActorsStore, ['isLoading', 'error', 'form']),
    tag() {
      return [
        {value: null, text: "Выберите тег"},
        ...this.tags.map(x => ({value: x.id, text: x.title}))
      ]
    },
    city() {
      return [
        {value: null, text: "Выберите город"},
        ...this.cities.map(x => ({value: x.id, text: x.name}))
      ]
    },
    eye_color() {
      return [
        {value: null, text: "Выберите цвет"},
        {value: "blue", text: "Голубые"},
        {value: "gray", text: "Серые"},
        {value: "green", text: "Зеленые"},
        {value: "brown", text: "Карие"},
      ]
    },
    body_type() {
      return [
        {value: null, text: "Выберите тип"},
        {value: "thin", text: "Худощавое"},
        {value: "sports", text: "Спортивное"},
        {value: "average", text: "Среднее"},
        {value: "dense", text: "Плотное"},
        {value: "fat", text: "Полное"},
      ]
    },
    face_type() {
      return [
        {value: null, text: "Выберите тип"},
        {value: "oval", text: "Овальное"},
        {value: "round", text: "Круглое"},
        {value: "square", text: "Квадратное"},
      ]
    },
    sex() {
      return [
        {value: null, text: "Выберите пол"},
        {value: "male", text: "Мужской"},
        {value: "female", text: "Женский"},
      ]
    },
    hair_color() {
      return [
        {value: null, text: "Выберите цвет"},
        {value: "blonde", text: "Блонд"},
        {value: "chestnut", text: "Каштан"},
        {value: "dark_blonde", text: "Русые"},
        {value: "dark", text: "Темные"},
        {value: "redhead", text: "Рыжие"},
      ]
    },
    hair_length() {
      return [
        {value: null, text: "Выберите длину"},
        {value: "bald", text: "Лысый"},
        {value: "short", text: "Короткие"},
        {value: "long", text: "Длинные"},
      ]
    },
    voice_timbre() {
      return [
        {value: null, text: "Выберите тип"},
        {value: "high", text: "Высокий"},
        {value: "low", text: "Низкий"},
      ]
    },
    skin_color() {
      return [
        {value: null, text: "Выберите цвет"},
        {value: "white", text: "Белая"},
        {value: "swarthy", text: "Смуглая"},
        {value: "dark", text: "Темная"},
      ]
    },
    is_not() {
      return [
        {value: null, text: "Ответ"},
        {value: "exist", text: "Есть"},
        {value: "not_exist", text: "Нет"},
      ]
    },
    bool_choices() {
      return [
        {value: true, text: "Да"},
        {value: false, text: "Нет"},
      ]
    },
  }
}
</script>
