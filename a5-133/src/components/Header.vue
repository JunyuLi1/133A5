<template>
    <header class="header">
      <div class="logo">
        <h1>Anteater Weather Checklist</h1>
      </div>
      <nav class="nav">
        <ul>
          <li><a href="#new">New Schedule</a></li>
          <li><a href="#load">Load</a></li>
          <li><a href="#log">Log</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <script setup>
  </script>
  
  <style scoped>
  /* Header 样式 */
  .header {
    position: fixed; /* 固定在页面顶部 */
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
    z-index: 1000; /* 确保 header 在最上层 */
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
  