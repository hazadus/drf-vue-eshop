<template>
  <div class="page-sign-up">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <div class="box">
          <h1 class="title is-size-2">Sign up</h1>
          <h2 class="subtitle">Create new user account</h2>
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

            <div class="field">
              <label>Repeat password:</label>
              <div class="control">
                <input v-model="password2" type="password" class="input" />
              </div>
            </div>

            <div v-if="errors.length" class="notification is-danger">
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>

            <div class="field">
              <div class="control has-text-right">
                <button class="button is-success">Sign up</button>
              </div>
            </div>

            <hr />

            <p>
              <router-link to="/log-in/" class="is-link">Log In</router-link>
              if you already have an account.
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "SignUpView",
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Sign up | vuEshop";
  },
  methods: {
    submitForm() {
      this.errors = [];

      /* Do simple form validation before sending it to backend */
      if (this.username.trim() === "") {
        this.errors.push("The username is missing.");
      }

      if (this.password.trim() === "") {
        this.errors.push("The password is too short.");
      } else {
        if (this.password !== this.password2) {
          this.errors.push("Passwords must match.");
        }
      }

      /* If all seems fine, send form to backend */
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            console.log(response);

            toast({
              message: `Account for user "${this.username}" successfully created. Please log in!`,
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 5000,
              position: "bottom-right",
            });

            this.$router.push("/log-in/");
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
                console.log(JSON.stringify(error.response.data));
              }
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again.");
              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>
