<template>
  <div class="result-container">
    <div class="result-top">
      <h3>{{genName()}}</h3>
      <span> <div class="rating-text">{{genRating()}}</div>⭐</span>
    </div>
    <span>{{genPhone()}}</span>
  </div>
</template>

<script>
export default {
  methods: {
    genName() {
      const names = [ "Andres", "Kevin", "Sergio", "Julián", "Rafael",
        "Alberto", "Carlos", "Ricardo", "Ray", "Juan", "John", "Jenny", "Juana",
        "Melisa", "Verónica", "Daniel", "Alejandra", "Evelyn"];
      
      const index = Math.random()*names.length;
      return names[Math.floor(index)];
    },
    genRating(){
      const num = '' + Math.random()*5;
      return num.substring(0,3);
    },
    genPhone(){
      let phone = '+57 3';

      for(let i = 0; i<9; i++){
        phone += '' + Math.floor(Math.random()*10)
      }

      return phone;
    }
  }
};
</script>

<style scoped>
.result-container{
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.result-top{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.result-top h3{
  font-size: 1.4rem;
  margin: 2px;
}

.result-top .rating-text{
  font-size: 1.2rem;
}

</style>
