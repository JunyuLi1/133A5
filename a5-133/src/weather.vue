<script setup>
    import axios from 'axios';
    import { ref } from 'vue';

    const weather = ref([]);

    // 请求天气数据
    axios.get('http://11.23.3.199:5000/requireWeather')
    .then(result => {
        weather.value = result.data['data'];
    })
    .catch(err => {
        console.error('Failed to request weather data:', err);
    });
</script>

<template>
    <br>
    <p>
        Today's weather is {{ weather }}.
    </p>
</template>

<style scoped>
/* 可根据需要添加样式 */
</style>

