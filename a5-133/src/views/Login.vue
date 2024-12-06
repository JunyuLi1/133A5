<template>
    <Header />
<div id="login">
    <div class="container">
    <h1>{{ isLogin ? "Login" : "Sign up" }}</h1>
    <form @submit.prevent="handleSubmit">
        <div>
        <label for="username">Username</label>
        <input
            type="text"
            id="username"
            v-model="username"
            placeholder="Please enter username"
        />
        </div>
        <div>
        <label for="password">Password</label>
        <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Please enter passward"
        />
        </div>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        <button type="submit">{{ isLogin ? "Login" : "Sign up" }}</button> <!--Submit the form and call handleSubmit function-->
    </form>
    <button @click="toggleMode"> 
        {{ isLogin ? "Cannot login? Sign up here." : "Already have an account? Login here." }}
    </button><!--Change the mode and call toggleMode function-->
    </div>
</div>
</template>

<script>
    import axios from 'axios';
    import Header from '@/components/Header.vue';
    export default {
        components:{Header},
    data() {
        return {
        isLogin: true,
        username: "",
        password: "",
        errorMessage: "",
        };
    },
    methods: {
        toggleMode() {
            this.isLogin = !this.isLogin;
            this.username = "";
            this.password = "";
            this.errorMessage = "";
        },
        handleSubmit() {
        if (!this.username || !this.password) {
            this.errorMessage = "Username and password cannot be blank!";
            return;
        }
        this.errorMessage = "";
        if (this.isLogin) {
            axios
            .post("http://127.0.0.1:5001/login", {
                username: this.username,
                password: this.password
            })
            .then((response) => {
                if (response.data.success) {
                    alert(`Welcome, ${this.username}`);
                    sessionStorage.setItem('username', this.username);
                    this.$store.dispatch('updateUsername', this.username);
                    this.$router.push('/todolis');
                } else {
                this.errorMessage = response.data.message;
                }
            })
            .catch((error) => {
                this.errorMessage = "Server error, please try again later."
                alert(this.errorMessage, error);
            });
        } else {
            axios
            .post("http://127.0.0.1:5001/register", {
                username: this.username,
                password: this.password
            })
            .then((response) => {
                if (response.data.success) {
                    alert(`Success, back to login.`);
                } else {
                this.errorMessage = response.data.message;
                }
            })
            .catch((error) => {
                this.errorMessage = "Server error, please try again later."
                alert(this.errorMessage, error);
            });
            this.isLogin = true;
            this.username = "";
            this.password = "";
            }
            },
        },
    };
</script>

<style>
    .container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    text-align: center;
    font-family: Arial, sans-serif;
    }

    label {
    display: block;
    margin-bottom: 8px;
    }

    input {
    width: 100%;
    padding: 8px;
    margin-bottom: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    }

    button {
    padding: 10px 20px;
    margin: 10px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    }

    button:hover {
    background-color: #0056b3;
    }

    .error {
    color: red;
    margin-bottom: 16px;
    }
</style>
  