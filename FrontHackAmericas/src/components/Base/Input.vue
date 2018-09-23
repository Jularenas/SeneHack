<template>
  <div class = "input">
    <form>
      <input type="text" name="name" class="question" id="nme" required autocomplete="off" v-on="listeners" v-bind="$attrs"/>
      <label for="nme"><span>{{placeholder}}</span></label>
    </form>
  </div>
</template>
<script>
  export default {
    inheritAttrs: false,
    name: 'Input',
    props:{
      placeholder: String
    },
    data() {
      return{
        placeholder: ''
      }
    },
    created(){
      this.placeholder = '';
    },
    computed:{
      listeners(){
        return {
          ...this.$listeners,
          input: event => this.$emit("input", event.target.value)
        }
      }
    }
  }
</script>
<style scoped>
  input,
  span,
  label,
  textarea {
    font-family: 'Ubuntu', sans-serif;
    display: block;
    margin: 10px;
    padding: 5px;
    border: none;
    font-size: 22px;
  }
  textarea:focus,
  input:focus {
    outline: 0;
  }
  input.question,
  textarea.question {
    font-size: 32px;
    font-weight: 300;
    border-radius: 2px;
    margin: 0;
    border: none;
    width: 80%;
    background: rgba(0, 0, 0, 0);
    transition: padding-top 0.2s ease, margin-top 0.2s ease;
    overflow-x: hidden;
  }
  input.question + label,
textarea.question + label {
  display: block;
  position: relative;
  white-space: nowrap;
  padding: 0;
  margin: 0;
  height: 100%;
  width: 35%;
  border-top: 1px solid red;
  -webkit-transition: width 0.4s ease;
  transition: width 0.4s ease;
  height: 0px;
}

input.question:focus + label,
textarea.question:focus + label {
  width: 80%;
}

input.question:focus,
input.question:valid {
  padding-bottom: 20px;
}

textarea.question:valid,
textarea.question:focus {
  margin-top: 35px;
}

input.question:focus + label > span,
input.question:valid + label > span {
  top: -80px;
  font-size: 22px;
  color: #333;
}

textarea.question:focus + label > span,
textarea.question:valid + label > span {
  top: -80px;
  font-size: 22px;
  color: #333;
}

input.question:valid + label,
textarea.question:valid + label {
  border-color: green;
}

input.question:invalid,
textarea.question:invalid {
  box-shadow: none;
}

input.question + label > span,
textarea.question + label > span {
  font-weight: 300;
  margin: 0;
  position: absolute;
  color: #8F8F8F;
  font-size: 22px;
  top: -40px;
  left: 0px;
  z-index: -1;
  -webkit-transition: top 0.4s ease, font-size 0.4s ease, color 0.4s ease;
  transition: top 0.4s ease, font-size 0.4s ease, color 0.4s ease;
}

@-webkit-keyframes appear {
  100% {
    opacity: 1;
  }
}

@keyframes appear {
  100% {
    opacity: 1;
  }
}
</style>
