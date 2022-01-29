<template>
  <img alt="Vue logo" src="./assets/logo.png" height="100" >
  <AppName msg="CryptoCalc"/>
</template>


<script>
import AppName from './components/AppName.vue'

export default {
  name: 'App',
  components: {
    AppName
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
