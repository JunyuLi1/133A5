<template>
    <div class="todo-container">
        <br>
        <h1>My To-Do List</h1>
        <table class="todo-table">
        <thead>
            <tr>
            <th>#</th>
            <th>Task</th>
            <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in todos" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.task }}</td>
            <td>{{ item.status }}</td>
            </tr>
        </tbody>
        </table>
    </div>
</template>
  
<script setup>
    import { ref } from 'vue';

    const todos = ref([
        { task: "Buy groceries", status: "Incomplete" },
        { task: "Finish Vue.js tutorial", status: "Incomplete" },
        { task: "Walk the dog", status: "Complete" },
    ]);
</script>
  
<style scoped>
    .todo-container {
        max-width: 600px;
        margin: 20px auto;
        font-family: Arial, sans-serif;
    }
    
    .todo-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }
    
    .todo-table th,
    .todo-table td {
        border: 1px solid #ccc;
        text-align: left;
        padding: 10px;
    }
    
    .todo-table th {
        background-color: #f4f4f4;
    }
    
    .todo-table td {
        background-color: #fff;
    }
</style>
  