<template>
  <div class = "input">
    <form>
      <input v-if="tipo==='pass'"  :maxlength=cantidad type="password" class="question textarea" required autocomplete="off" v-on="listeners" v-bind="$attrs"/>
      <input v-else-if="tipo==='cel'" :maxlength=cantidad type="number" class="question textarea" required autocomplete="off" v-on="listeners" v-bind="$attrs"/>
      <input v-else :maxlength=cantidad class="question textarea" required autocomplete="off" v-on="listeners" v-bind="$attrs"/>
      <label for="nme"><span>{{placeholder}}</span></label>
    </form>
  </div>
</template>
<script>
  export default {
    inheritAttrs: false,
    name: 'Input',
    props:{
      tipo: String,
      placeholder: String,
      cantidad: Number
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
*{
  font-family: 'Montserrat', sans-serif;
}
  input,
  span,
  label,
  textarea {
    font-family: 'Montserrat', sans-serif;
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
    color: black;
    font-size: 24px;
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
.textarea.question + label {
  display: block;
  position: relative;
  white-space: nowrap;
  padding: 0;
  margin: 0;
  height: 100%;
  width: 45%;
  border-top: 1px solid red;
  -webkit-transition: width 0.4s ease;
  transition: width 0.4s ease;
  height: 0px;
}

input.question:focus + label,
.textarea.question:focus + label {
  width: 90%;
  color: white;
}

input.question:focus,
input.question:valid {
  padding-bottom: 10px;
}

textarea.question:valid,
textarea.question:focus {
  margin-top: 35px;
}

input.question:focus + label > span,
input.question:valid + label > span {
  top: -80px;
  font-size: 20px;
  color: #333;
}

textarea.question:focus + label > span,
textarea.question:valid + label > span {
  top: -80px;
  font-size: 20px;
  color: white;
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
