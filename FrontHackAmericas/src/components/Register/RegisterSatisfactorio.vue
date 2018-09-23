<template>
    <div class="registro">
      <div class="recuadro">
          <p class="regis">Tu registro fue satisfactorio, {{nombre}}!</p>
          <p>Ahora podras hacer Log in con el correo que registraste.</p>
      </div>
    </div>
</template>
    
<script>
export default {
  name: 'Satisfactorio',
  props: {
    nombre: String
  },
  mounted(){
      setTimeout(function () { this.$router.push({name: 'LandingPage'}); }.bind(this), 2000)
  }
}
</script>

<style scoped>
*{
  font-family: 'Montserrat', sans-serif;
}
.regis{
    font-size: 28px;
}
.registro{
    margin-left: auto;
    width: 100%;
    margin-top: 125px;
  }
</style>