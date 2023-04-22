import { createWebHistory, createRouter } from "vue-router";

const routes =  [
  {
    path: "/",
    alias: "/equipment",
    name: "equipment",
    component: () => import("./components/Equipment")
  },
  {
    path: "/test",
    alias: "/test",
    name: "test",
    component: () => import("./components/TestEquipment")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
