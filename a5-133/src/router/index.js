import { createRouter, createWebHistory } from "vue-router";

import Login from '@/views/Login.vue'
import Homepage from '@/views/Homepage.vue'
import ToDoLis from "@/views/ToDoLis.vue";

const routes = [
  { path: "/todolis", component: ToDoLis },
  { path: "/login", component: Login },
  { path: "/", name: 'Home', component: Homepage }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
