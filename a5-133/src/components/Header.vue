<template>
    <header class="header">
      <div class="logo">
        <h1><a href="/">Anteater ToDoList</a></h1>
      </div>
      <nav class="nav">
        <ul>
          <li><a href="/login">Login</a></li>
          <li><a href="/todolis">ToDoList</a></li>
          <li><a href="mailto:yuxid5@uci.edu">Contact</a></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  .header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #66BB6A;
    color: #fff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}
  
  .logo h1 {
    font-family: 'Unica One', sans-serif;
    font-size: 1.5em;
    margin: 0;
  }
  
  .nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: 15px;
  }
  h1 a{
    color: #fff;
  }
  .nav li {
    display: inline;
  }
  
  .nav a {
    color: #fff;
    text-decoration: none;
    font-size: 1.2em;
  }
  
  .nav a:hover {
    text-decoration: underline;
  }
  </style>
  