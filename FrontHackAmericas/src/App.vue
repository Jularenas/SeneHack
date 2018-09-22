<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  },
  mounted() {
    var mapboxgl = require("mapbox-gl/dist/mapbox-gl.js");

    mapboxgl.accessToken =
      "pk.eyJ1Ijoic2d1em1hbm0iLCJhIjoiY2pleXB3aW45MDkxZDJxcDZzY3FnaTh2ZCJ9.B7iUjwcIAXVEmjQx6I3iEA";
    var map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/streets-v10"
    });

    // Add zoom and rotation controls to the map.
    map.addControl(new mapboxgl.NavigationControl());

    const esto = this;

    fetch('http://157.253.224.248:5000/adyacentes',{
      method: 'POST',
      body: JSON.stringify({
        origen:{
          latitud: 4.661257,
          longitud: -74.114722
        },
        destino: {
          latitud: 4.603030,
          longitud: -74.065253
        },
        radioSalida: 20,
        radioLlegada: 20
      })
    }).then(res => res.text()).then(text =>{
        const parsed = text.replace(/'/g, '"');
        const json = JSON.parse(parsed);
        esto.msg = json;
        console.log(json)
      }
    ).catch(error => console.log(error));
  }
};
</script>

<style>
html, body{
  height: 100vh;
  width: 100vw;
  
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex: 1;
  flex-direction: column;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

#map {
  height: 300px;
  width: 300px;
}
</style>
