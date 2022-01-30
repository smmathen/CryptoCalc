<template>
	<div style="display: block">
	<form style="display: block;">
	<div>
	<label for="base">Base:</label>
	<input type="number" v-model="base" name="base"/>
		</div>
	<div>
	<label for="exp">Exp:</label>
	<input type="number" v-model="exp" name="exp"/>
	</div>
	<div>
	<label for="mod">N:</label>
	<input type="number" v-model="mod" name="exp"/>
	</div>
	</form>
	</div>
	<div>{{base !== "" ? base : "base"}}<sup>{{exp !== "" ? exp : "exp"}}</sup> mod {{mod !== "" ? mod : "N"}} = {{ans !== "" ? ans : "?"}}</div>
</template>

<script>
export default {
	name: "FastPower",
  props: {
  },
  data: () => ({
	base: "",
	exp: "",
	mod: "",
	ans: "",
  }),
  watch: {
	base: function () {
		console.log("base: "+this.base);
	},
  },
	

}
</script>

<style>

</style>

