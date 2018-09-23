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
    email: String
  },
  components: {
    Map,
    Sidebar
  },
  mounted(){
    window.onbeforeunload = closingCode;
    function closingCode(){
      const url = 'http://157.253.222.183:5000/closed'+this.email;
      const Http=new XMLHttpRequest();
      Http.open('DELETE', url, false);
      Http.send();
      return null;
}
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
  }
};
</script>

<style scoped>

.explorer-container{
  display: flex;
  flex-direction: row;
  height: calc(100vh - 80px);
  margin-top: 80px;
}

</style>
