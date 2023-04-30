<template>
  <b-overlay :show="isLoading">
    <b-form-select
        :value="modelValue"
        @change="$emit('update:modelValue', $event)"
        :options="options">
    </b-form-select>
  </b-overlay>
</template>

<script>
import {getTags} from "../services/api";

export default {
  name: "FilterActorContainer",
  emits: ['update:modelValue'],
  props: {
    modelValue: String
  },
  data() {
    return {
      results: [],
      isLoading: false
    }
  },
  methods: {
    async load() {
      this.isLoading = true;
      this.results = await getTags();
      this.isLoading = false
    }
  },
  created() {
    this.load()
  },
  computed: {
    options() {
      return [
        {value: null, text: "Выберите тег"},
        ...this.results.map(x => ({value: x.id, text: x.title}))
      ]
    }
  }
}
</script>

<style scoped>

</style>