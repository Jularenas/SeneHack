<template>
  <div class="map-container">
    <GmapMap
      :center="start"
      :zoom="13"
      map-type-id="terrain"
      style="width: 100%; height: 100%"
    >
    <GmapCircle
      :center="start"
      :radius="startRadius"
    />

    <GmapMarker
      clickable
      draggable
      @drag="location => onStartDrag(location)"
      label="Start"
      title="Start"
      :position="start"
    />

    </GmapMap>
  </div>
</template>

<script>
export default {
  props:{
    startRadius: Number,
    endRadius: Number,
    start: Object,
    end: Object,
    onStartDrag: Function,
    onEndDrag: Function
  },
  mounted() {

  },
  methods: {}
};
</script>

<style>
.map-container {
  display: flex;
  flex: 5;
  flex-direction: column;
}

#map {
  position: relative;
  width: 100%;
  height: 100%;
}

canvas.mapboxgl-canvas {
  position: absolute;
  left: 0;
  top: 0;
}
</style>
