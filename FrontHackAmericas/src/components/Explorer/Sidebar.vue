<template>
  <div class="sidebar-container">
    <h1>
      Encuentra parceros:
    </h1>

    <label> "Radio de búsqueda (inicio)" </label>

    <div class="slider-container">
      <Slider 
        @input="event => this.onStartRadiusChange(event)"
        v-bind="options"
      />
    </div>

    <label>Radio de búsqueda (final)</label>

    <div class="slider-container">
      <Slider 
        v-model="endRadius"
        v-bind="options"
      />
    </div>

    <div>
      <i class="material-icons">commute</i>
      <i class="material-icons">transfer_within_a_station</i>
    </div>


  </div>
</template>

<script>
import BaseInput from '@/components/Base/Input';
import Slider from "vue-slider-component";

export default {
  components: {
    BaseInput,
    Slider
  },
  props: {
    startRadius: Number,
    endRadius: Number,
    start: Object,
    end: Object,
    onStartRadiusChange: Function,
    onEndRadiusChange: Function
  },
  data() {
    return {
      options: {
        width: "80%", // 组件宽度
        height: 8,
        direction: "horizontal", // 组件方向
        dotSize: 16, // 滑块大小
        eventType: "auto", // 事件类型
        min: 100, // 最小值
        max: 1200, // 最大值
        show: true, // 是否显示组件
        realTime: false, // 是否实时计算组件布局
        tooltip: "always", // 是否显示工具提示
        clickable: true, // 是否可点击的
        tooltipDir: "top", // 工具提示方向
        useKeyboard: false, // 是否使用键盘控制
        reverse: false, // 是否反向组件
        speed: 0.5 // 动画速度
      }
    };
  }
};
</script>

<style scoped>
.sidebar-container {
  display: flex;
  flex: 1.4;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.sidebar-container h1 {
  font-size: 2rem;
}

.slider-container{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  margin-bottom: 8px;
  width: 80%;
}
</style>
