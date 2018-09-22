<template>
  <div class="sidebar-container">
    <h1>
      Encuentra parceros:
    </h1>

    <input />

    <label>Radio de búsqueda (inicio)</label>
    <Slider />

    <input />

    <label>Radio de búsqueda (final)</label>
    <Slider />

    <div>
      <i class="material-icons">commute</i>
      <i class="material-icons">transfer_within_a_station</i>
    </div>


  </div>
</template>

<script>
//import Input from '@/components/Base/Input';
import Slider from 'vue-slider-component';

export default {
  components:{
    //¿Input,
    Slider
  }
}
</script>

<style scoped>

.sidebar-container{
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

</style>
