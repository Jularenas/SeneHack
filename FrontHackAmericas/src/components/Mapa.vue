<template>
  <div class="mapa">
    <p>Don Hack: {{obtener}}</p>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  name: 'Mapa',
  props: {
    msg: String
  },
  computed: {
    obtener: function () {
      var cuerpo = {};
      var url = 'http://157.253.224.248:5000/adyacentes';
      var metodo = 'POST';
      fetch(url, {body: cuerpo, method: metodo}).then(function(response){
        return response.text();
      }).then(function(myJson){
        return myJson;
      })
    }
  }
}
</script>
