import { createRouter, createWebHistory } from "vue-router";
import store from "../store";
import HomeView from "../views/HomeView.vue";

const routes = [
  {
    path: "/",
    name: "HomeView",
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
    path: "/log-in/",
    name: "LogInView",
    component: () =>
      import(/* webpackChunkName: "LogInView" */ "../views/LogInView.vue"),
  },
  {
    path: "/profile/",
    name: "ProfileView",
    component: () =>
      import(/* webpackChunkName: "ProfileView" */ "../views/ProfileView.vue"),
    meta: {
      requireLogin: true,
    },
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

router.beforeEach((to, from, next) => {
  /*
  Check if route has `meta: { requireLogin: true, }` then redirect to login page if user
  is not authenticated.
  Reference: https://router.vuejs.org/guide/advanced/meta.html
  */
  if (
    // to.matched.some((parameter) => parameter.meta.requireLogin) &&
    // !store.state.isAuthenticated
    to.meta.requireLogin &&
    !store.state.isAuthenticated
  ) {
    next({ name: "LogInView", query: { to: to.path } });
  } else {
    next();
  }
});

export default router;
