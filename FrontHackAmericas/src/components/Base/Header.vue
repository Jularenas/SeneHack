<template>
  <div id="header">
      <h1 id="logo">T-MON</h1>
      {{user}} - {{pass}}
      <div id="log">
        <BaseInput v-model="user" class="textbox" type="text" placeholder="Usuario"></BaseInput>
        <BaseInput v-model="pass" class="textbox" type="password" placeholder="Clave"></BaseInput>
        <Boton v-on:click="miMetodo" nombre="Log In"></Boton>
      </div>
  </div>
</template>
<script>

import Boton from '@/components/Base/Boton';
import BaseInput from '@/components/Base/Input';

export default {
  props: {
    onLogin: Function
  },
  data(){
    return{
      user: '',
      pass: ''
    }
  },
  methods: {
    miMetodo() {
      this.$router.push("Explore", this.onLogin);
    }
  },
  components:{
    Boton,
    BaseInput
  }
};
</script>

<style scoped>
div#header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 80px;
  background-color: #225584;
  position: fixed;
}
h1#logo {
  margin-left: 20px;
  margin-top: 20px;
  font-size: 5em;
}
#log{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  font-size: 0.9em;
  padding-top: 20px;
  width: 30%;
}


</style>
