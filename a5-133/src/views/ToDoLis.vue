<template>
    <div class="todo-container">
    <br>
    <h1>My To-Do List</h1>
    <h1>Welcome, {{ username }}</h1>
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
          <td>{{ item[0] }}</td>
          <td>{{ item[1]}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
  
<script setup>
    import { ref, computed, onMounted } from 'vue';
    import axios from 'axios';
    import { useStore } from 'vuex';

    const todos = ref([]);

    const store = useStore();
    const username = computed(() => store.state.username);

    // 获取用户的 notes（从后端加载）
    const fetchNotes = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5001/loadTask', {
                            params: {
                                username: username.value
                            }
                        });
        if (response.data.success) {
        todos.value = response.data.note;
        } else {
        console.error(response.data.message);
        }
    } catch (error) {
        console.error("Failed to load notes:", error);
    }
    };

    // 在组件挂载时加载 notes
    onMounted(() => {
    fetchNotes();
    });
</script>
  
<style scoped>
    .todo-container {
        max-width: 600px;
        margin: 20px auto;
        font-family: Arial, sans-serif;
    }
    .todo-container h1{
        text-align: center;
        font-weight: bold;
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
  