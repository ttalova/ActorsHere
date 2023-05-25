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
        <p>{{ this.results.city }}</p>
      </b-card-text>
      <b-button v-if="this.canEdit===this.results.user" :to="{ name: 'actorForm'}"
                variant="primary">Редактировать
      </b-button>
      <LikeButtonComponent v-if="isAuth" @clickLike="clickLike" :like="this.like"/>
    </b-card>
  </div>
</template>

<script>
import LikeButtonComponent from "../components/LikeButtonComponent.vue";
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";
import {useActorsStore} from "../stores/actors";

export default {
  name: "ActorContainer",
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
    this.getEditMode()
    this.loading()
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
    getEditMode() {
      if (this.user) {
        this.canEdit = this.user.id
      } else {
        this.canEdit = false
      }
    },
      async clickLike() {
        if (!this.like) {
          try {
            this.like_info = await this.LikedActor(this.id)
            await this.loading()
          } catch (e) {
            this.error = e.message
          }
        } else {
          try {
            this.like_info = await this.DisLikedActor(this.like_id)
            await this.loading()
          } catch (e) {
            this.error = e.message
          }
        }
      },
      async loading() {
        this.like_info = await this.actor_be_liked(this.id)
        if (this.like_info) {
            this.like = true
            this.like_id = this.like_info.id
          } else {
            this.like = false
          }
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