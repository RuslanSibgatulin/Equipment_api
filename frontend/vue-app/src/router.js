import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/equipment",
    name: "equipment",
    component: () => import("./components/Equipment")
  },
  {
    path: "/login",
    alias: "/login",
    name: "login",
    component: () => import("./components/Login")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
