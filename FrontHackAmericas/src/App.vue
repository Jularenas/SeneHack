<template>
  <div id="app">
    <Header :loggedIn="loggedIn" :onLogin="onLogIn"></Header>
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
    onLogIn(event){
      this.user = event;
      this.loggedIn = true;
    }
  },
  components:{
    Header
  },
  data() {
    return {
      loggedIn: false,
      user: ''
    };
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
