<template>
  <div>
    <b-card
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
      <LikeButtonComponent v-if="isAuth" @clickLike="clickLike" :like="this.like"/>
    </b-card>
  </div>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useCastingsStore} from "../stores/castings";
import {useAuthStore} from "../stores/auth";
import {getCastingbyId} from "../services/castings_api";
import LikeButtonComponent from "../components/LikeButtonComponent.vue";

export default {
  name: "CastingContainer",
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
    ...mapActions(useCastingsStore, ['load', 'casting_be_liked', 'LikedCasting', 'DisLikedCasting']),
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
    },
    async clickLike() {
      if (!this.like) {
        try {
          this.like_info = await this.LikedCasting(this.id)
          await this.loading()
        } catch (e) {
          this.error = e.message
        }
      } else {
        try {
          this.like_info = await this.DisLikedCasting(this.like_id)
          await this.loading()
        } catch (e) {
          this.error = e.message
        }
      }
    },
    async loading() {
      this.like_info = await this.casting_be_liked(this.id)
      if (this.like_info) {
          this.like = true
          this.like_id = this.like_info.id
        } else {
          this.like = false
        }
    },
  },
  computed: {
    ...mapState(useCastingsStore, ['isLoading', 'error', 'results', 'like_info']),
    ...mapState(useAuthStore, ['user', 'isAuth'])
  },
}
</script>

<style scoped>

</style>