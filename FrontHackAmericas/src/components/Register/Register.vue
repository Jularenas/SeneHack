<template>
    <div class="registro">
      <div class="recuadro">
        <form class="form-registro" action="index.html" method="post">
          <Input placeholder="Nombre" class="nombre-i"></Input>
          <Input placeholder="Email" class="email-i"></Input>
          <Input placeholder="Password" class="pass-i"></Input>
          <Input placeholder="Celular" class="celular-i"></Input>
          <Boton nombre="Registrarse" class="btn-registrar"></Boton>
        </form>
      </div>
    </div>
</template>

<script>
import Boton from '@/components/Base/Boton'
import Input from '@/components/Base/Input'
export default {
  components:{
    Boton,
    Input
  }
}
</script>

<style scoped>
  .recuadro{
      border-style: solid;
      border-radius: 5px;
      border-width: 2px;
      width: 55%;
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
