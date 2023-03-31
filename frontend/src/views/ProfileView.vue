<template>
  <div class="page-profile">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">User profile</h1>
        <h2 class="subtitle">Logged in as &laquo;{{ user.username }}&raquo;</h2>
        <div class="box">
          <table class="table">
            <tbody>
              <tr>
                <td>First name:</td>
                <td>{{ user.first_name }}</td>
              </tr>
              <tr>
                <td>Last name:</td>
                <td>{{ user.last_name }}</td>
              </tr>
              <tr>
                <td>E-mail:</td>
                <td>{{ user.email }}</td>
              </tr>
              <tr>
                <td>Last login:</td>
                <td>{{ user.last_login }}</td>
              </tr>
              <tr>
                <td>Date joined:</td>
                <td>{{ user.date_joined }}</td>
              </tr>
            </tbody>
          </table>

          <button class="button is-warning" @click="logout">Log out</button>
        </div>
      </div>

      <div v-if="orders.length" class="column is-12">
        <h2 class="title is-size-2">Your orders</h2>
        <OrderSummary v-for="order in orders" :key="order.id" :order="order" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
import OrderSummary from "../components/OrderSummary.vue";

export default {
  name: "ProfileView",
  components: {
    OrderSummary,
  },
  data() {
    return {
      orders: [],
    };
  },
  computed: {
    ...mapGetters({
      /*
      This maps `user` state from Vuex store to computed property.
      */
      user: "getUser",
    }),
  },
  mounted() {
    document.title = "Profile | vuEshop";
    this.getUserOrders();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      // Set `token` to "", delete it from Local Storage, `isAuthenticated` to false:
      this.$store.commit("removeToken");
      this.$store.commit("removeUser");
      this.$router.push({ name: "HomeView" });
    },
    async getUserOrders() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/orders/")
        .then((response) => {
          this.orders = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
