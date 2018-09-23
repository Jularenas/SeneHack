<template>
  <div class="explorer-container">
      <Sidebar 
        :startRadius="startRadius"
        :endRadius="endRadius"
        :start="start"
        :end="end"
        :onStartRadiusChange="radius => this.startRadius = radius"
        :onEndRadiusChange="radius => this.endRadius = radius"
      />
      <Map 
        :startRadius="startRadius"
        :endRadius="endRadius"
        :start="start"
        :end="end"
        :onStartDrag="location => this.start = location.latLng"
        :onEndDrag="location => this.end = location.latLng"
      />

<!-- :onStartChange="newStart => this.start = newStart"
        :onEndChange="" -->

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
  data(){
    return{
      start: {lat: 4.620783, lng: -74.077571},
      end: {lat: 4.690783, lng: -74.177571},
      startRadius: 100,
      endRadius: 100,
      searchMode:[
        ''
      ]
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
