<template>
  <div class="content-container">
    <img id="foto_ciudad" v-bind:src="require('@/assets/Centro_internacional.png')" alt="Fondo">
    <div id="fondo"></div>
    <div>
      <img id="foto" v-bind:src="require('@/assets/demo.png')" >
      <h2 id="slogan">La forma mas amigable de transportarse</h2>
      <h3>Consigue transporte a cualquier hora y lugar en tiempo real o planea tus viajes de una forma eficiente, comoda y barata en el medio de transporte de tu elección</h3>
    </div>
    <div class="button-container">
   <Boton nombre="Registrate" v-on:click="registrar"></Boton>
    </div>
    <div id="redes">
      <i class="fab fa-facebook-square"></i>
      <i class="fab fa-twitter-square"></i>
      <i class="fab fa-instagram"></i>
    </div>
  </div>
</template>

<script>
import Boton from '@/components/Base/Boton';
export default {
  components:{
    Boton
  },
  methods:{
    registrar: function(event){
      console.log('lp')
      this.$router.push('Registrar');
    }
  }
}
</script>

<style scoped>

.content-container{
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  margin-top: 120px;
  margin-left: 120px;
  height: 60vh;
}

  #foto_ciudad{
    position: fixed;
    width: 100%;
    height: 120%;
    left:0px;
    z-index:-1;
  }
  div#fondo{
    background-color: black;
    opacity: 0.7;
    position: absolute;
    z-index: -1;
    height: 100%;
    width: 90%;
    top: 0px;
    left: 5%;
  }
  #foto{
    opacity: 1;
    position: absolute;
    right: 8%;
    top: 25%;
    width: 40vw;
    height: 50vh;
  }

  #slogan{
    font-size: 3em;
    color: #D9CCC1;
    width: 45%;
    line-height: 50px;
    text-align: left;
  }
  h3{
    font-size: 1em;
    color: #D9CCC1;
    position: relative;
    width: 40%;
    margin-top: 30px;
    text-align: justify;
  }
  i{
    position: relative;
    font-size: 3em;
    display: inline-block;
    margin-right: 5%;
    margin-top: 35%;
    color: #6B91B6 ;
    cursor: pointer;
    transition: all 0.4s ease-in-out;
  }

  i:hover{
    color: #f45e61;
    font-size: 4em;
  }

  #redes{
    position: absolute;
    top:60%;
    left: 11%;
    width: 40%;
  }

  .button-container{
    margin-left: -0.35rem;
  }
</style>
