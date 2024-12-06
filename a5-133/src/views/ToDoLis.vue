<template>
    <div class="page-container">
      <h1>Todo List</h1>
      <div class="todo-container">
        <div class="left-panel">
          <form @submit.prevent="handleSubmit" class="todo-form">
            <label>
              Time:
              <input v-model="form.time" type="datetime-local" required />
            </label>
            <label>
              Task:
              <input v-model="form.description" type="text" placeholder="Input Task" required />
            </label>
            <label>
              Category:
              <input v-model="form.category" type="text" placeholder="Input Category" required />
            </label>
            <button type="submit">{{ isEditing ? "Save Change" : "Create Task" }}</button>
          </form>
        </div>
        
        <div class="right-panel">
          <div class="task-list-container">
            <ul class="todo-list">
              <li v-for="task in tasks" :key="task.id" class="todo-item">
                <div class="task-info">
                  <strong>{{ task.time }}</strong> | {{ task.description }} ({{ task.category }})
                </div>
                <div class="task-actions">
                  <button @click="editTask(task)">Edit</button>
                  <button @click="deleteTask(task.id)">Delete</button>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  let currentId = 1
  
  const tasks = ref([
    { id: currentId++, time: '2024-12-05T09:00', description: '学习 Vue 3', category: '学习' },
    { id: currentId++, time: '2024-12-05T14:00', description: '买菜', category: '生活' }
  ])
  
  const form = ref({
    time: '',
    description: '',
    category: ''
  })
  
  const isEditing = ref(false)
  const editingTaskId = ref(null)
  
  const handleSubmit = () => {
    if (!form.value.time || !form.value.description || !form.value.category) return
    if (isEditing.value && editingTaskId.value !== null) {
      const index = tasks.value.findIndex(task => task.id === editingTaskId.value)
      if (index !== -1) {
        tasks.value[index] = {
          ...tasks.value[index],
          time: form.value.time,
          description: form.value.description,
          category: form.value.category
        }
      }
      resetForm()
    } else {
      tasks.value.push({
        id: currentId++,
        time: form.value.time,
        description: form.value.description,
        category: form.value.category
      })
      resetForm()
    }
  }
  
  const editTask = (task) => {
    isEditing.value = true
    editingTaskId.value = task.id
    form.value = {
      time: task.time,
      description: task.description,
      category: task.category
    }
  }
  
  const deleteTask = (id) => {
    tasks.value = tasks.value.filter(task => task.id !== id)
  }
  
  const resetForm = () => {
    form.value = {
      time: '',
      description: '',
      category: ''
    }
    isEditing.value = false
    editingTaskId.value = null
  }
  </script>
  
  <style scoped>
  * {
    box-sizing: border-box;
  }
  
  .page-container {
    max-width: 800px;
    margin: 0 auto;
    font-family: Arial, sans-serif;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .todo-container {
    display: flex;
    gap: 20px;
  }
  

  .left-panel {
    flex: 1; 
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
  }
  

  .right-panel {
    flex: 2;
    min-width: 0;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 10px;
    display: flex;
    flex-direction: column;
  }
  
  /* 表单样式 */
  .todo-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .todo-form label {
    display: flex;
    flex-direction: column;
    font-weight: bold;
  }
  
  .todo-form input {
    padding: 4px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .todo-form button {
    padding: 8px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
  }
  
  .todo-form button:hover {
    background-color: #0056b3;
  }
  
  /* fix height */
  .task-list-container {
    min-width: 300px;
    height: 300px;
    overflow-y: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 5px;
    margin-top: 10px;
  }
  
  .todo-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .todo-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid #ddd;
  }
  
  .task-info {
    max-width: 60%;
    word-wrap: break-word;
  }
  .task-actions {
    display: flex;
    gap: 5px;
    white-space: nowrap; 
    align-items: start;
    }
  .task-actions button {
    margin-left: 5px;
    padding: 4px 8px;
    background: #007bff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .task-actions button:hover {
    background: #0056b3;
  }

  @media (max-width: 600px) {
    .todo-container {
        flex-direction: column;
    }

    .left-panel, .right-panel {
        flex: none;
        width: 100%;
    }

    .task-info {
        max-width: 100%;
        margin-right: 0;
    }

    .task-actions {
        margin-top: 5px;
    }

    .todo-item {
        flex-direction: column;
        align-items: flex-start;
    }

    .task-actions {
        justify-content: flex-start;
    }
    }
  </style>