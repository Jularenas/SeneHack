<template>
  <div id="header">
      <img id="logo" v-bind:src="require('@/assets/Logo.png')" alt="">
      <div v-if="!loggedIn" id="log">
        <BaseInput v-model="user" class="textbox-1" type="text" placeholder="Usuario"></BaseInput>
        <BaseInput v-model="pass" class="textbox-2" type="password" placeholder="Clave"></BaseInput>
        <Boton v-on:click="miMetodo" nombre="Log In"></Boton>
      </div>
  </div>
</template>
<script>

import Boton from '@/components/Base/Boton';
import BaseInput from '@/components/Base/Input';
import {login} from '@/utils.js';

export default {
  props: {
    onLogin: Function,
    loggedIn: Boolean
  },
  data(){
    return{
      user: '',
      pass: ''
    }
  },
  methods: {
    miMetodo() {
      login(this.user,this.pass,(test)=>{
        console.log(test);
        if(test==='True'){
          this.onLogin(this.user);
          this.$router.push({name: "Explore", params: {user: this.user}});
        }
        else if (!test)
          console.log('Failed login') && alert("El usuario o la clave son incorrectos");
      });
      
    }
  },
  components:{
    Boton,
    BaseInput
  }
};
</script>

<style scoped>
.textbox-1{
  margin-top: 15px;
  margin-right: 25px;
}
.textbox-2{
  margin-top: 15px;
  margin-right: 25px;
}
div#header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 90%;
  left: 5%;
  height: 80px;
  background-color: #225584;
  position: fixed;
}
#log{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  font-size: 0.9em;
  padding-top: 20px;
  width: 35%;
}

#logo {
  top:0px;
  height: 80px;
  margin-left: 0px;
}
</style>
