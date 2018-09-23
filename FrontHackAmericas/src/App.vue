<template>
  <div id="app">
    <Header :onLogin="this.onLogIn"></Header>
    <router-view></router-view>
  </div>
</template>

<script>
import Header from '@/components/Base/Header'

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
