import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CartView from "../views/CartView.vue";
import SearchView from "../views/SearchView.vue";
import ProductDetailView from "../views/ProductDetailView.vue";
import CategoryDetailView from "../views/CategoryDetailView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/search/",
    name: "SearchView",
    component: SearchView,
  },
  {
    path: "/cart/",
    name: "CartView",
    component: CartView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/:categorySlug/:productSlug/",
    name: "ProductDetailView",
    component: ProductDetailView,
  },
  {
    path: "/:categorySlug/",
    name: "CategoryDetailView",
    component: CategoryDetailView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
