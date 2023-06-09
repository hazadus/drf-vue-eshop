import { createStore } from "vuex";

export default createStore({
  state: {
    cart: {
      items: [],
    },
    user: {},
    isAuthenticated: false,
    token: "",
    isLoading: false,
  },
  getters: {
    /*
    Used to "watch" cart updates using `mapGetters`.
    */
    getCart: (state) => state.cart,
    getUser: (state) => state.user,
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("cart")) {
        state.cart = JSON.parse(localStorage.getItem("cart"));
      } else {
        localStorage.setItem("cart", JSON.stringify(state.cart));
      }

      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    addToCart(state, item) {
      /*
      Add `item` to cart, or increase it's quantity if it's already in the cart.
      */
      const exists = state.cart.items.filter(
        (i) => i.product.id === item.product.id
      );

      if (exists.length) {
        exists[0].quantity = parseInt(
          exists[0].quantity + parseInt(item.quantity)
        );
      } else {
        state.cart.items.push(item);
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    clearCart(state) {
      /*
      Reset cart to empty state.
      */
      state.cart = { items: [] };
      localStorage.setItem("cart", JSON.stringify(state.cart));
    },
    setIsLoading(state, status) {
      /* 
      Global `loading` state of the app - set to `true` while fetching data from backend to display
      "loading" indicator on the page.
      */
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
      localStorage.setItem("token", token);
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      localStorage.removeItem("token");
      state.isAuthenticated = false;
    },
    setUser(state, user) {
      /*
      Save detailed user info we get from our "user/details/" endpoint to use throughout the app.
      */
      state.user = user;
    },
    removeUser(state) {
      /*
      Clear user info on logout.
      */
      state.user = {};
    },
  },
  actions: {},
  modules: {},
});
