## Setup
    Open the terminal and Install flask-cors
        - pip install flask-cors
    cd to folder a5-133 and install following
        - npm install 
        - npm install axios
        - npm install vue-router@4
        - npm install vuex@next
## How to use?
    run following commend under folder 133A5
        - python3 app.py
    after start the backend server, get the IP address from the terminal and use this IP address to replace the address
    in ./133A5/a5-133/weather.vue
    run following commend under folder a5-133
        - npm run dev
## Structure
    app.py: communicate with front end.
    tools folder:
        WebAPI.py: define general abstract webapi class
        OpenWeather.py: define and get weather result
    a5-133 folder:
        components: folder that contains different vue component
        App.vue: main app
        
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