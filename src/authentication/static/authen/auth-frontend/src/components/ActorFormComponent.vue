<template>
  <div>
    <h1>Заполните анкету актера!</h1>
    <b-form @submit="onSubmit" @reset="onReset">
      <b-row>
        <b-col md="6">
          <b-form-group
              label="ФИО:"
              label-for="input-1"
          >
            <b-form-input
                v-model="form.email"
                type="text"
                placeholder="Введите ваше полное имя"
                required
            ></b-form-input>
          </b-form-group>
          <b-form-group
              label="Ваша фотография:">
            <b-form-file
                v-model="file1"
                :state="Boolean(file1)"
                placeholder="Выберите файл или перенесите его сюда..."
                drop-placeholder="Drop file here..."
            ></b-form-file>
          </b-form-group>

          <div>
            <label for="example-datepicker">Дата рождения:</label>
            <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
          </div>

          <b-form-group id="input-group-2" label="Параметры фигуры:" label-for="input-2">
            <b-form-input
                v-model="form.name"
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
                v-model="form.weight"
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
                v-model="form.weight"
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
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Телосложение:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Пол:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Тип лица:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Цвет волос:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Длина волос:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>
        </b-col>
        <b-col md="6">

          <b-form-group
              label="Тембр голоса:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Цвет кожи:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Город:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Наличие татуировок:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

          <b-form-group
              label="Наличие пирсинга:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
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
                v-model="form.email"
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
                v-model="form.email"
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
                v-model="form.email"
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
                v-model="form.email"
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
                v-model="form.email"
                type="text"
                placeholder=""
            ></b-form-input>
          </b-form-group>

        </b-col>
        <b-col md="6">
          <b-form-group label="Теги">
            <b-form-select v-model="selected" :options="options" multiple :select-size="4"></b-form-select>
          </b-form-group>
          <b-form-group
              label="Готов к переезду:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>
          <b-form-group
              label="Загран. паспорт:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>
          <b-form-group
              label="Водительские права:"
              label-for="input-1"
          >
            <b-form-select v-model="selected" :options="options"></b-form-select>
          </b-form-group>

        </b-col>

      </b-row>

      <b-button type="submit" variant="primary">Сохранить</b-button>
      </b-form>
  </div>
</template>

<script>
export default {
  name: "ActorFormComponent",
  data() {
    return {
      form: {
        email: '',
        name: '',
        food: null,
        checked: []
      },
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.name = ''
      this.form.food = null
      this.form.checked = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>
