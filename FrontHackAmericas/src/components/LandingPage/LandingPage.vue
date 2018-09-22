<template>
  <div>
    <Header></Header>
    <img id="foto_ciudad" v-bind:src="require('@/assets/Centro_internacional.png')" alt="Fondo">
    <div id="fondo"></div>
    <img id="foto" v-bind:src="require('@/assets/captura.png')" >
    <h2 id="slogan">La forma mas amigable de transportarse</h2>
    <h3>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eleifend justo a pulvinar laoreet. Mauris varius sed enim ac accumsan. Nulla id tellus pharetra, vestibulum ante in, tempor mi. Donec at velit sed eros auctor tincidunt. Curabitur sed tincidunt sem. Mauris tempus ligula neque. Vivamus vel vestibulum quam.</h3>
   <button id="registro">Registrarse</button>
    <div id="redes">
      <i class="fab fa-facebook-square"></i>
      <i class="fab fa-twitter-square"></i>
      <i class="fab fa-instagram"></i>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Base/Header'
export default {
  components:{
    Header
  }
}
</script>

<style scoped>
  #foto_ciudad{
    position: fixed;
    width: 100%;
    height: 100%;
    top:80px;
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
        right: 200px;
        width: 400px;
        top: 250px;
  }

  #slogan{
    font-size: 3em;
    color: #D9CCC1;
    position: relative;
    width: 40%;
    top: 140px;
    left: 140px;
    line-height: 50px;
    text-align: justify;
  }
  h3{
    font-size: 1em;
    color: #D9CCC1;
    position: relative;
    width: 40%;
    margin-top: 160px;
    left: 140px;
    text-align: justify;
  }
  i{
    position: relative;
    font-size: 3em;
    display: inline-block;
    margin-right: 5%;
    margin-top: 35%;
    color: #6B91B6;
  }
  #redes{
    position: absolute;
    top:60%;
    left: 11%;
    width: 40%;
  }
  #registro{
    position: relative;
  }
</style>
