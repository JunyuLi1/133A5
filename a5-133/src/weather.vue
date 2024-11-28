<script setup>
    import axios from 'axios';
    import { ref } from 'vue';

    const weather = ref([]);

    // request weather data
    axios.get('http://11.23.3.199:5000/requireWeather') // based on backend address
    .then(result => {
        weather.value = result.data['data'];
    })
    .catch(err => {
        console.error('Failed to request weather data:', err);
    });
</script>

<template>
    <br>
    <p class="weather">
        Today's weather is {{ weather }}.
    </p>
</template>

<style scoped>
    .weather {
        font-size: 2em;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-top: 20%;
    }
</style>

