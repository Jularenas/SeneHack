<template>
  <div class="button-container">
      <button class="draw meet" v-bind="$attrs" v-on="listeners">{{nombre}}</button>
  </div>
</template>

<script>
  export default {
    inheritAttrs: false,
    name: 'Boton',
    props:{
      nombre: String
    },
    computed: {
      listeners(){
        return{
          ...this.$listeners,
          input: event => this.$emit("input", event.target.value)
        }
      }
    }
  }
</script>

<style lang="scss" scoped>

.button-container{
  cursor: pointer;
}

$background: #fefefe;
$text: #4b507a;

$cyan: #60daaa;
$yellow: #fbca67;
$orange: #ff8a30;
$red: #f45e61;
$purple: #6477b9;
$blue: #0eb7da;
button {
  background: none;
  border: 0;
  box-sizing: border-box;
  margin: 0.9em;
  padding: 0.8em 1.5em;
  box-shadow: inset 0 0 0 2px $red;
  color: $red;
  font-size: inherit;
  font-weight: 700;
  position: relative;
  vertical-align: middle;
  cursor: pointer;
  &::before,
  &::after {
    box-sizing: inherit;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
  }
}

.draw {
    transition: color 0.25s;

  &::before,
  &::after {
    border: 2px solid transparent;
    width: 0;
    height: 0;
  }
  &::before {
    top: 0;
    left: 0;
  }

  // And this the bottom & left borders (expands left, then up)
  &::after {
    bottom: 0;
    right: 0;
  }

  &:hover {
    color: $cyan;
  }

  // Hover styles
  &:hover::before,
  &:hover::after {
    width: 100%;
    height: 100%;
  }

  &:hover::before {
    border-top-color: $cyan;
    border-right-color: $cyan;
    transition:
      width 0.25s ease-out,
      height 0.25s ease-out 0.25s;
  }

  &:hover::after {
    border-bottom-color: $cyan;
    border-left-color: $cyan;
    transition:
      border-color 0s ease-out 0.5s,
      width 0.25s ease-out 0.5s,
      height 0.25s ease-out 0.75s;
  }
}

.buttons {
  isolation: isolate;
}

</style>
