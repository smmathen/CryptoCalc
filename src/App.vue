<template>
  <img alt="Vue logo" src="./assets/logo.png" height="100" >
  <AppName msg="CryptoCalc"/>
  <div style="display: flex; justify-content: center;">
    <Floater title="Cryptography Calculator"/>
  </div>
</template>


<script>
import AppName from './components/AppName.vue'
import Floater from './components/Floater.vue'

export default {
  name: 'App',
  components: {
    AppName,
    Floater
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
