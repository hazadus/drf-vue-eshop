<template>
  <div class="page-profile">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">User profile</h1>
        <h2 class="subtitle">Logged in as ...</h2>
        <button class="button is-warning" @click="logout">Log out</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  components: {
    //OrderSummary,
  },
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    document.title = "Profile | vuEshop";
    //this.getMyOrders();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      // Set `token` to "", delete it from Local Storage, `isAuthenticated` to false:
      this.$store.commit("removeToken");
      this.$router.push({ name: "HomeView" });
    },
    // async getMyOrders() {
    //   this.$store.commit("setIsLoading", true);
    //   await axios
    //     .get("/api/v1/orders/")
    //     .then((response) => {
    //       this.orders = response.data;
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    //   this.$store.commit("setIsLoading", false);
    // },
  },
};
</script>
