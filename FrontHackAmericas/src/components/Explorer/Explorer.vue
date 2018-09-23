<template>
  <div class="explorer-container">
      <Sidebar 
        :startRadius="startRadius"
        :endRadius="endRadius"
        :start="start"
        :end="end"
        :onStartRadiusChange="radius => this.startRadius = radius"
        :onEndRadiusChange="radius => this.endRadius = radius"
        :searchMode="searchMode"
        :onAdjacencyQuery="(queryRes) => {
          this.results = queryRes; 
        }"
        :results='this.results'
      />
      <Map 
        :startRadius="startRadius"
        :endRadius="endRadius"
        :start="start"
        :end="end"
        :onStartDrag="location => this.start = location.latLng"
        :onEndDrag="location => this.end = location.latLng"
      />
  </div>
</template>

<script>
import Map from "./Map";
import Sidebar from "./Sidebar";

export default {
  props: {
    user: String
  },
  components: {
    Map,
    Sidebar
  },
  methods:{
  },
  created: function () {
    var borrar = this.user;
    console.log(borrar);
    window.addEventListener('beforeunload', function (event) {
      const url = 'https://p2poolserver.herokuapp.com/closed/'+borrar;
      const Http=new XMLHttpRequest();
      Http.open('DELETE', url, false);
      Http.send();
      console.log("Acabó 1");
      return null;
    }, false)
  },
  data(){
    return{
      start: {lat: 4.620783, lng: -74.077571},
      end: {lat: 4.650783, lng: -74.098771},
      startRadius: 100,
      endRadius: 100,
      searchMode:[],
      results: []
    }
  },
  mounted(){
    console.log(this.$route.params);
  }
};
</script>

<style scoped>

.explorer-container{
  display: flex;
  flex-direction: row;
  height: calc(100vh - 80px);
  margin: 0 5vw;
  margin-top: 80px;
}

</style>
