<template>
  <div id="header">
      <h1 id="logo">T-MON</h1>
  </div>
</template>

<script>
export default {
  props: {
    login: Boolean
  }
};
</script>

<style scoped>
  div#header{
    width: 100%;
    height: 80px;
    background-color: #225584;
    position: fixed;
  }
  h1#logo{
    margin-left: 20px;
    margin-top: 20px;
    position: fixed;
    font-size: 5em;
  }
</style>
