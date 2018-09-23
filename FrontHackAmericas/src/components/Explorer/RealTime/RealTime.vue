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
import Map from "../MapRT";
import Sidebar from "@/components/Explorer/SidebarRT";
export default {
  props: {
    email: String
  },
  components: {
    Map,
    Sidebar
  },
  data(){
    return{
      start: {lat: 4.6014463999999995, lng: -74.059776},
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
