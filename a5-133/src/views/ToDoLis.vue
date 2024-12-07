<template>
    <Header />
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
                <div class="task-info" :class="{'text-red': isPast(task.time)}">
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
  import Header from '@/components/Header.vue';
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';
  import { useStore } from 'vuex';
  
//   let currentId = 1
  
  const tasks = ref([])
  
  const form = ref({
    time: '',
    description: '',
    category: ''
  })
  
  const isEditing = ref(false)
  const editingTaskId = ref(null)
    // username from session
  const store = useStore();
  const username = computed(() => store.state.username);

  
  const isPast = (time) => {
    const currentTime = new Date();
    const taskTime = new Date(time);
    return taskTime < currentTime;
};
  
  const handleSubmit = async () => {
    if (!form.value.time || !form.value.description || !form.value.category) return
    if (isEditing.value && editingTaskId.value !== null) {
      const index = tasks.value.findIndex(task => task.id === editingTaskId.value)
      console.log(index)
      if (index !== -1) {
        // const updatedTask = {
        //   ...tasks.value[index],
        //   time: form.value.time,
        //   description: form.value.description,
        //   category: form.value.category
        // };
        try {
          const response = await axios.post('http://127.0.0.1:5001/editTask', {
          id: editingTaskId.value,
          username: username.value,
          time: form.value.time,
          description: form.value.description,
          category: form.value.category
        });
        if (response.data.success) {
          alert("Success!");
          fetchNotes()
          resetForm()
        }
        } catch (error) {
            alert(error.message, error);
        }
      }
    } else {
      try {
          const response = await axios.post('http://127.0.0.1:5001/insertTask', {
          username: username.value,
          time: form.value.time,
          description: form.value.description,
          category: form.value.category
        });
        if (response.data.success) {
          alert("Success!");
          fetchNotes();
          resetForm()
        }
      } catch (error) {
          alert(error.message, error);
      }
    }
  }
  
  const editTask = (task) => {
    console.log(task.id)
    isEditing.value = true
    editingTaskId.value = task.id
    form.value = {
      time: task.time,
      description: task.description,
      category: task.category
    }
  }
  
  const deleteTask = async (task_id) => {
    try {
          const response = await axios.post('http://127.0.0.1:5001/deleteTask', {
          id: task_id
        });
        if (response.data.success) {
          alert("Success!");
        }
      } catch (error) {
          alert(error.message, error);
      }
    tasks.value = tasks.value.filter(task => task.id !== task_id)
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

  // request notes from backend
  const fetchNotes = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:5001/loadTask', {
                            params: {
                                username: username.value
                            }
                        });
        if (response.data.success) {
            tasks.value = response.data.note;
        } else {
        console.error(response.data.message);
        }
    } catch (error) {
        console.error("Failed to load notes:", error);
    }
    };

    // load notes
    onMounted(() => {
    fetchNotes();
    });

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
  .text-red {
    max-width: 60%;
    word-wrap: break-word;
    color: red;
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