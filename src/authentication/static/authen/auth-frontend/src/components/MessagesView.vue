<template>
  <form @submit.prevent="connect">
    <div>
      <b-card title="Какой кастинг вы хотите обсудить?">
      <b-form-group
      >
        <b-form-select
            v-model="noteId"
            :options="castings"
            class="mb-3"
            value-field="value"
            text-field="text"
            disabled-field="notEnabled"
        ></b-form-select>
      </b-form-group>
        <b-button type="submit" variant="primary">Подключиться</b-button>
      </b-card>
    </div>
  </form>
  <hr>
  <b-card title="Чат">
  <pre>{{ messages }}</pre>
    </b-card>
    <b-card class="page-footer" title="Введите ваше сообщение">
  <form @submit.prevent="sendMessage">
    <b-input placeholder="Сообщение" v-model="message"/>
    <br>
    <b-button type="submit" variant="primary" >Отправить</b-button>
  </form>
    </b-card>
</template>

<script>
import {initMessages} from "../services/messages_api";
import {useCastingsStore} from "../stores/castings";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";

export default {
  name: "MessagesView",
  data() {
    return {
      noteId: null,
      message: null,
      messages: '',
      options: []
    };
  },
  created() {
    this.load()
  },
  computed: {
    ...mapState(useCastingsStore, ['isLoading', 'error', 'results']),
    ...mapState(useAuthStore, ['user']),
    castings() {
      return [
        {value: null, text: "Выберите кастинг"},
        ...this.options.map(x => ({value: x.id, text: x.header}))
      ]
    },
  },
  methods: {
    ...mapActions(useCastingsStore, ['getListOfCastings', 'listOfActorsResponse']),
    async load() {
      this.isLoading = true
      try {
        await this.getListOfCastings()
        this.options = this.results
      } catch (e) {
        this.error = e.message
      }
      this.isLoading = false
    },

    connect() {
      this.send = initMessages(this.noteId, (message) => {
        this.messages += message.message + "\n";
      })
    },
    sendMessage() {
      this.send({message: this.message});
      this.message = null;
    }
  }
}
</script>

<style scoped>
.page-footer {
  position: fixed;
  bottom: 0;
  width: 62%;
  left: 19%;
}
</style>

