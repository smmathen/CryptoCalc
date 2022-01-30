
<template>
  <div class="hello">
	<h1>{{ msg }}</h1>
  </div>
  <fast-power/>
</template>

<script>
import FastPower from "./FastPower.vue";
export default{
  components: { FastPower },
  name: "AppName",
  props: {
	msg: String,
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
