import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: import("@/views/HomeView.vue"),
    children: [
      {
        path: "",
        name: "LandingContainer",
        component: () => import("@/components/LandingPage.vue"),
      },
      {
        path: "like/:user",
        name: "SelectContainer",
        component: () => import("@/components/SelectLikeAnime.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
