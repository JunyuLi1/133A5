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

## Problem
    1. add delete edit feature with db
    2. new user/add
