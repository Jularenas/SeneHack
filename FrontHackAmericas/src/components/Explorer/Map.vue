<template>
  <div class="map-container">
    <div id="map"></div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.map-container{
  display: flex;
  flex: 5;
  flex-direction: column;
}

#map{
  position: relative;
  width: 100%;
  height: 100%;
}

canvas.mapboxgl-canvas{
  position: absolute;
  left: 0;
}

</style>
