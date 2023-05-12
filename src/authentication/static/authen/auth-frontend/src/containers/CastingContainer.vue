<template>
  <div>
    <b-card
        img-src="https://picsum.photos/600/300/?image=25"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 200rem;"
        class="mb-2"
    >
      <b-card-title>
        {{ this.results.header }}
      </b-card-title>
      <b-card-text>
        <p>{{ this.results.fee }}</p>
      </b-card-text>
      <b-button v-if="this.canEdit===this.results.casting_owner" :to="{ name: 'castingformbyid', params: { id: this.results.id }}"
                variant="primary">Редактировать
      </b-button>
    </b-card>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {useAuthStore} from "../stores/auth";
import {getCastingbyId} from "../services/castings_api";

export default {
  name: "CastingContainer",
  data() {
    return {
      results: [],
      isLoading: false,
      error: null,
      canEdit: false
    }
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  created() {
    this.load(this.id)
    this.getEditMode()
    console.log(this.canEdit)
  },
  methods: {
    ...mapActions(useCastingsStore, ['load']),
    async load(id) {
      this.isLoading = true;
      this.error = null;
      try {
        this.results = await getCastingbyId(id);
      } catch (e) {
        this.error = e.message
      }
      this.isLoading = false;
    },
    getEditMode() {
      if (this.user) {
        this.canEdit = this.user.id
      } else {
        this.canEdit = false
      }
    }
  },
  computed: {
    ...mapState(useCastingsStore, ['isLoading', 'error',]),
    ...mapState(useAuthStore, ['user'])
  },
}
</script>

<style scoped>

</style>