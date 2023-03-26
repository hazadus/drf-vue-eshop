import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/search/",
    name: "SearchView",
    component: () =>
      import(/* webpackChunkName: "SearchView" */ "../views/SearchView.vue"),
  },
  {
    path: "/cart/",
    name: "CartView",
    component: () =>
      import(/* webpackChunkName: "CartView" */ "../views/CartView.vue"),
  },
  {
    path: "/sign-up/",
    name: "SignUpView",
    component: () =>
      import(/* webpackChunkName: "SignUpView" */ "../views/SignUpView.vue"),
  },
  {
    path: "/about/",
    name: "AboutView",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "AboutView" */ "../views/AboutView.vue"),
  },
  {
    path: "/:categorySlug/:productSlug/",
    name: "ProductDetailView",
    component: () =>
      import(
        /* webpackChunkName: "ProductDetailView" */ "../views/ProductDetailView.vue"
      ),
  },
  {
    path: "/:categorySlug/",
    name: "CategoryDetailView",
    component: () =>
      import(
        /* webpackChunkName: "CategoryDetailView" */ "../views/CategoryDetailView.vue"
      ),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
