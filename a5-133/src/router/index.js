import { createRouter, createWebHistory } from "vue-router";


import ToDoLis from "@/views/ToDoLis.vue";
import App from "@/App.vue";

const routes = [
  { path: "/todolist", component: ToDoLis },
  { path: "/", component: App }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
