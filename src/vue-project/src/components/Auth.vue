<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Sign in</h1>
      <label>Email </label>
      <input required v-model="email" type="email" placeholder="email"/><br><br>
      <label>Password </label>
      <input required v-model="password" type="password" placeholder="Password"/><br><br>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "Auth"
}
</script>

<style scoped>

</style>