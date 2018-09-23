<template>
    <div class="registro">
      <div class="recuadro">
          <BaseInput placeholder="Nombre" v-model="name" pass="False" cantidad=50 class="nombre-i"></BaseInput>
          <BaseInput placeholder="E-Mail" v-model="email" pass="False" cantidad=50 class="email-i"></BaseInput>
          <BaseInput placeholder="Password" v-model="pass" tipo="pass" cantidad=50 class="pass-i"></BaseInput>
          <BaseInput placeholder="Celular" v-model="cell" tipo="cel" cantidad=10 class="celular-i"></BaseInput>
          <Boton nombre="Registrarse" pass="False" class="btn-registrar" v-on:click="miMetodo"></Boton>
      </div>
    </div>
</template>

<script>
import Boton from '@/components/Base/Boton'
import BaseInput from '@/components/Base/Input'
import {register} from '@/utils.js';
export default {
  components:{
    Boton,
    BaseInput
  },
  methods: {
    miMetodo() {
      console.log('Register');
      register(this.name, this.email, this.pass, this.cell,(test)=>{
          this.$router.push({name: 'RegisterSatisfactorio', params:{nombre: this.name}});
      });
      
    }
  }
}
</script>

<style scoped>
  *{
    font-family: 'Montserrat', sans-serif;
  }
  .recuadro{
      border-style: solid;
      border-radius: 5px;
      border-width: 2px;
      width: 55%;
  }
  .registro > input{
    color: black;
  }
  .registro{
    margin-left: auto;
    width: 65%;
    margin-top: 95px;
  }
  .pass-i, .nombre-i, .celular-i, .email-i, .passs-i{
    margin-left: 25px;
    margin-top: 45px;
  }
  .celular-i{
    margin-bottom: 45px;
  }
  .btn-registrar{
    margin-bottom: 15px;
  }

</style>
