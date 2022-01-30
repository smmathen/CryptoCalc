	<template>
	<div>
	<form>
		<div class="equations">
			<label for="base">Base: </label>
			<input type="number" v-model="base" name="base"/>
		</div>
		<br/>
		<div>
			<label for="exp">Exp: </label>
			<input type="number" v-model="exp" name="exp"/>
		</div>
		<br/>
		<div>
			<label for="mod">N: </label>
			<input type="number" v-model="mod" name="exp"/>
		</div>
		<br/>
		<br/>
		</form>
	</div>
	<div>{{base !== "" ? base : "base"}}<sup>{{exp !== "" ? exp : "exp"}}</sup> mod {{mod !== "" ? mod : "N"}} = {{ans !== "" ? ans : "?"}}<br/> 
	<div>{{solve(base, exp, mod)}}</div>
	</div>
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
	
	methods:{
		solve: function(base, exp, mod){
			return base ** exp % mod;
		}
	}

}
</script>

<style>
	.equations{
		margin-top: 30px;
	}

	#input[type=number]{
		margin-bottom: 30px;
	}
	

</style>

