<template>
  <div id="app">
    <Header :onLogin="this.onLogIn"></Header>
    <router-view></router-view>
  </div>
</template>

<script>
import Header from '@/components/Base/Header'
import {login} from './utils.js'
import {register} from './utils.js'
import {adyacentes} from './utils.js'

export default {
  name: "app",
  methods:{
    onLogIn(){
        document.getElementById('log').style.display='none';
        
    }
  },
  components:{
    Header
  },
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  },
  mounted() {
    
    /*
    //register('ja.manrique','ja.manrique.00','3131313131');
    //login('ja.manrique','ja.manrique.00');
    adyacentes('ja.manrique',4.5836411, -74.093567,4.5839411, -74.093667,10,5,);

    var mapboxgl = require("mapbox-gl/dist/mapbox-gl.js");
    mapboxgl.accessToken =
      "pk.eyJ1Ijoic2d1em1hbm0iLCJhIjoiY2pleXB3aW45MDkxZDJxcDZzY3FnaTh2ZCJ9.B7iUjwcIAXVEmjQx6I3iEA";
    var map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/streets-v10"
    });
    // Add zoom and rotation controls to the map.
    map.addControl(new mapboxgl.NavigationControl());
    */

    const esto = this;
    adyacentes('s.guzmanm', 4.5836411, -74.093567, 4.5839411, -74.093667,10,5,);
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