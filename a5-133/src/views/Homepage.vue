<template>
    <Header/>
    <div class="main">
    <div class="clock">{{ currentTime }}</div>
  </div>
    <br>
    <p class="weather">
        Today's weather is {{ weather }}.
    </p>
</template>
  
<script setup>
    import axios from 'axios';
    import { ref, onMounted } from 'vue';
    import Header from '@/components/Header.vue';
    const weather = ref([]);

    // request weather data
    axios.get('http://127.0.0.1:5001/requireWeather') // based on backend address
    .then(result => {
        weather.value = result.data['data'];
    })
    .catch(err => {
        console.error('Failed to request weather data:', err);
    });
    
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
  
<style scoped>
.weather {
        font-size: 2em;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-top: 20px;
}
.main{
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
  