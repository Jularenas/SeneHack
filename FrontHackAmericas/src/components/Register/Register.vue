<template>
    <div class="registro">
      <form class="form-registro" action="index.html" method="post">
        <Input placeholder="Nombre" class="nombre-i"></Input>
        <Input placeholder="Password" class="pass-i"></Input>
        <Input placeholder="Celular" class="celular-i"></Input>
      </form>
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
  .registro{
    width: 65%;
    margin-top: 95px;
  }
  .pass-i, .nombre-i, .celular-i{
    margin-top: 45px;
  }
</style>
