<template>
  <button @click.prevent="$emit('clickLike')"
          :class="{ 'btn-liked': like, 'btn-like': !like }">
    <i class="fa fa-heart"></i> like
  </button>
</template>

<script>
import {mapActions, mapState} from "pinia/dist/pinia";
import {useAuthStore} from "../stores/auth";
import {useActorsStore} from "../stores/actors";
import {useCastingsStore} from "../stores/castings";

export default {
  name: "LikeButtonComponent",
  props: {
    like: {
      type: Boolean,
      required: true
    }
  },
  // data() {
  //   return {
  //     like: false,
  //     like_id: null
  //   }
  // },
  // computed: {
  //   ...mapState(useActorsStore, ['results', 'error']),
  //   ...mapState(useCastingsStore, ['results', 'error'])
  // },
  // methods: {
  //   ...mapActions(useActorsStore, ['LikedActor', 'actor_be_liked', 'DisLikedActor']),
  //   ...mapActions(useCastingsStore, ['LikedCasting', 'casting_be_liked', 'DisLikedCasting']),
  //   async LikeHandler() {
  //     console.log('vjnvvmf,v')
  //   },}
  //   async load() {
  //     if (this.actor) {
  //       this.results = await this.actor_be_liked(this.actor)
  //       if (this.results.results.length === 0) {
  //         this.like = false
  //       } else {
  //         this.like = true
  //         this.like_id = this.results.results[0].id
  //       }
  //     } else {
  //       this.results = await this.casting_be_liked(this.casting)
  //       console.log(this.results)
  //       if (this.results.length === 0) {
  //         this.like = false
  //       } else {
  //         this.like = true
  //         this.like_id = this.results.results[0].id
  //       }
  //     }
  //   },
  //   async LikeHandlerActor() {
  //     if (!this.like) {
  //       try {
  //         this.results = await this.LikedActor(this.actor)
  //         await this.load()
  //       } catch (e) {
  //         this.error = e.message
  //       }
  //     } else {
  //       try {
  //         this.results = await this.DisLikedActor(this.like_id)
  //         await this.load()
  //       } catch (e) {
  //         this.error = e.message
  //       }
  //     }
  //   },
  //   async LikeHandlerCasting() {
  //     if (!this.like) {
  //       try {
  //         this.results = await this.LikedCasting(this.casting)
  //         await this.load()
  //       } catch (e) {
  //         this.error = e.message
  //       }
  //     } else {
  //       try {
  //         this.results = await this.DisLikedCasting(this.like_id)
  //         await this.load()
  //       } catch (e) {
  //         this.error = e.message
  //       }
  //     }
  //   },
  // },
  // created() {
  //   this.load()
  // }
}
</script>

<style>
.btn-like {
  position: relative;
  background-color: transparent;
  border: none;
  color: #555;
  cursor: pointer;
}

.btn-liked {
  background-color: #17a2b8;
  border-color: #17a2b8
}

.fa-heart {
  margin-right: 5px;
}

.fa-heart:before {
  content: "\1F90D";
}
</style>