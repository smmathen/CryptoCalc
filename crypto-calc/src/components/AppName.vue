
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
  <div>
<form>
<label for="base">Base:</label>
<input type="number" v-model="base" name="base"/>
<label for="exp">Exp:</label>
<input type="number" v-model="exp" name="exp"/>
<label for="mod">N:</label>
<input type="number" v-model="mod" name="exp"/>
</form>
  </div>
  <div>{{base !== "" ? base : "base"}}<sup>{{exp !== "" ? exp : "exp"}}</sup> mod {{mod !== "" ? mod : "N"}} = {{ans !== "" ? ans : "?"}}</div>
</template>

<script>
export default {
  name: 'AppName',
  props: {
    msg: String
  },
  data: () => ({
    base: "",
    exp: "",
    mod: "",
    ans: ""
  }),
  watch: {
    base: function () {
      console.log(this.base);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
