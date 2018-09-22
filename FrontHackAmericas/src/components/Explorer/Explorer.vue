<template>
  <div class="explorer-container">
      <Sidebar />
      <Map />
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
      start: null,
      end: null,
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
}

</style>
