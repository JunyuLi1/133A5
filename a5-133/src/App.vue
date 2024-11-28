<script setup>
import { ref, onMounted } from 'vue';
import Header from './components/Header.vue';
import weather from './weather.vue'
import todolis from './ToDoLis.vue'
const currentTime = ref('');
function updateClock() {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');
  currentTime.value = `${hours}:${minutes}:${seconds}`;
}
onMounted(() => {
  updateClock();
  setInterval(updateClock, 1000);
});
</script>

<template>
  <Header />
  <div id="main">
    <div class="clock">{{ currentTime }}</div>
  </div>
    <weather/>
    <todolis/>
</template>

<style>

body {
  background-color: #E8F5E9;
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

#app {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#main{
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.clock {
  text-align: center;
  font-size: 2em;
  font-family: 'Share Tech Mono', monospace;
  font-weight: bold;
  color: #333;
}

</style>
