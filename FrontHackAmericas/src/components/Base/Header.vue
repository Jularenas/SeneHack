<template>
  <div id="header">
      <h1 id="logo">T-MON</h1>
      <div id="log">
        <input class="textbox" type="text" placeholder="Usuario">
        <input class="textbox" type="text" placeholder="Clave">
        <input v-on:click="miMetodo" type="submit" value="Log In">
      </div>
  </div>
</template>
<script>


export default {
  props: {
    onLogin: Function
  },
  methods: {
    miMetodo() {
      this.$router.push("Explore", this.onLogin);
    }
  }
};
</script>

<style scoped>
div#header {
  width: 100%;
  height: 80px;
  background-color: #225584;
  position: fixed;
}
h1#logo {
  margin-left: 20px;
  margin-top: 20px;
  position: fixed;
  font-size: 5em;
}
</style>
