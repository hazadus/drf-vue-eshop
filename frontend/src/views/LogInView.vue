<template>
  <div class="page-log-in">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <div class="box">
          <h1 class="title is-size-2">Log in</h1>
          <h2 class="subtitle">Log into the site with your account.</h2>
          <form @submit.prevent="submitForm">
            <div class="field">
              <label>Username:</label>
              <div class="control">
                <input v-model="username" type="text" class="input" />
              </div>
            </div>

            <div class="field">
              <label>Password:</label>
              <div class="control">
                <input v-model="password" type="password" class="input" />
              </div>
            </div>

            <div v-if="errors.length" class="notification is-danger">
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>

            <div class="field">
              <div class="control has-text-right">
                <button class="button is-success">Log in</button>
              </div>
            </div>

            <hr />

            <p>
              <router-link :to="{ name: 'SignUpView' }" class="is-link">
                Sign up
              </router-link>
              if you don't have an account yet.
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogInView",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Log in | vuEshop";
  },
  methods: {
    async submitForm() {
      // Reset authorization data, if any
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("/api/v1/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          // Save token in Vuex store, Local storage, and set `isAuthenticated` global state to `true`:
          this.$store.commit("setToken", token);

          axios.defaults.headers.common["Authorization"] = "Token " + token;
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");

            console.log(JSON.stringify(error));
          }
        });

      /*
      Get detailed user info to use throughout the app.
      */
      await axios
        .get("/api/v1/user/details/")
        .then((response) => {
          const user = response.data;
          // Save user info to Vuex store for global use.
          this.$store.commit("setUser", user);
        })
        .catch((error) => {
          console.log(error);
        });

      // Redirect to profile page
      const toPath = this.$route.query.to || { name: "ProfileView" };
      this.$router.push(toPath);
    },
  },
};
</script>
