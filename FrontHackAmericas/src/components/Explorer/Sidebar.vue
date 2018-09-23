<template>
  <div class="sidebar-container">
    <h1>
      Encuentra pares y fuentes:
    </h1>

    <label>Radio de búsqueda (inicio)</label>

    <div class="slider-container">
      <Slider 
        @input="event => this.onStartRadiusChange(event)"
        v-bind="options"
      />
    </div>

    <label>Radio de búsqueda (final)</label>

    <div class="slider-container">
      <Slider 
        @input="event => this.onEndRadiusChange(event)"
        v-bind="options"
      />
    </div>

    <div class='icons-container'>

      <div class="icon-container">
        <label>Buscar fuentes</label>
        <i
          @click="() => selectMode('fuentes')" 
          :class="['material-icons', searchMode.indexOf('fuentes') !== -1 ? 'selected-icon' : {} ]">
          commute
        </i>
      </div>

      <div class="icon-container">
        <label>Buscar peers</label>
        <i
          @click="() => selectMode('peers')" 
          :class="['material-icons', searchMode.indexOf('peers') !== -1 ? 'selected-icon' : {} ]">
          transfer_within_a_station
        </i>
      </div>
    </div>
    <Boton
      @click="queryAdjacencies"
      nombre="Buscar"
    />

    <div class="results-container">
      <Result v-for="result in results"
        :key="result.fecha_calculo"
        :result='result'
      />
    </div>

  </div>
</template>

<script>
import BaseInput from "@/components/Base/Input";
import Boton from "@/components/Base/Boton";
import Slider from "vue-slider-component";
import Result from "./Result";
import { adyacentes } from "@/utils";

export default {
  components: {
    BaseInput,
    Slider,
    Boton,
    Result
  },
  props: {
    startRadius: Number,
    endRadius: Number,
    start: Object,
    end: Object,
    onStartRadiusChange: Function,
    onEndRadiusChange: Function,
    searchMode: Array,
    onAdjacencyQuery: Function,
    results: Array
  },
  data() {
    return {
      options: {
        width: "100%", // 组件宽度
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
  },
  methods: {
    selectMode(mode) {
      const index = this.searchMode.indexOf(mode);
      if (index !== -1) {
        //The item is on the list
        this.searchMode.splice(index, 1);
      } else {
        this.searchMode.push(mode);
      }
    },
    queryAdjacencies() {
      var este = this;
      fetch("http://157.253.222.183:5000/adyacentes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          user: "julian",
          origen: {
            latitud: this.start.lat,
            longitud: this.start.lng
          },
          destino: {
            latitud: this.end.lat,
            longitud: this.end.lng
          },
          radioSalida: this.startRadius,
          radioLlegada: this.endRadius
        })
      })
        .then(res => res.text())
        .then(json => {
          const parsed = json.replace(/'/g, '"');
          console.log("parsed: ", parsed);
          este.onAdjacencyQuery(parsed);
        });
    }
  }
};
</script>

<style scoped>
.sidebar-container {
  display: flex;
  flex: 1.5;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.sidebar-container h1 {
  font-size: 1.92rem;
}

label {
  font-size: 1.32rem;
}

.slider-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
  margin-bottom: 8px;
  width: 80%;
}

.icons-container {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  width: 100%;
}

.icon-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.icon-container label {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  width: 60%;
}

.icon-container i {
  border: 3px #2c3e50 solid;
  padding: 3px;
  font-size: 2.6rem;
  cursor: pointer;
  margin-top: 4px;
  transition: all 0.2s ease-in-out;
}

.icon-container i:hover {
  background-color: rgb(232, 255, 255);
}

.icons-container .icon-container .selected-icon {
  background-color: rgb(118, 180, 180);
}

.icons-container .icon-container .selected-icon:hover {
  background-color: rgb(79, 153, 153);
}
</style>
