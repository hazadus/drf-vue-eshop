<template>
  <div class="wrapper">
    <nav class="navbar is-link">
      <div class="container is-widescreen">
        <div class="navbar-brand">
          <router-link :to="{ name: 'HomeView' }" class="navbar-item">
            <h2 class="title is-2 has-text-light">
              <font-awesome-icon icon="fa-brands fa-vuejs" />
              <strong>uEshop</strong>
            </h2>
          </router-link>

          <a
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbar-menu"
            @click="showMobileMenu = !showMobileMenu"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div
          id="navbar-menu"
          class="navbar-menu"
          :class="{ 'is-active': showMobileMenu }"
        >
          <div class="navbar-start is-size-5">
            <router-link
              :to="{
                name: 'CategoryDetailView',
                params: { categorySlug: 'vinyl-records' },
              }"
              class="navbar-item"
              :class="{
                'is-active': $route.params.categorySlug === 'vinyl-records',
              }"
            >
              Vinyl
            </router-link>
            <router-link
              :to="{
                name: 'CategoryDetailView',
                params: { categorySlug: 'turntables' },
              }"
              class="navbar-item"
              :class="{
                'is-active': $route.params.categorySlug === 'turntables',
              }"
            >
              Turntables
            </router-link>
            <router-link
              :to="{
                name: 'CategoryDetailView',
                params: { categorySlug: 'mixers' },
              }"
              class="navbar-item"
              :class="{
                'is-active': $route.params.categorySlug === 'mixers',
              }"
            >
              Mixers
            </router-link>
            <router-link
              :to="{ name: 'AboutView' }"
              class="navbar-item"
              :class="{
                'is-active': $route.name === 'about',
              }"
            >
              About
            </router-link>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <form method="get" action="/search/">
                <div class="field has-addons">
                  <div class="control">
                    <input
                      type="text"
                      class="input"
                      placeholder="Find product..."
                      name="query"
                    />
                  </div>
                  <div class="control">
                    <button class="button is-info">
                      <span class="icon">
                        <font-awesome-icon icon="fa-solid fa-search" />
                      </span>
                    </button>
                  </div>
                </div>
              </form>
            </div>
            <div class="navbar-item">
              <div class="buttons">
                <router-link
                  v-if="!$store.state.isAuthenticated"
                  :to="{ name: 'LogInView' }"
                  class="button is-light"
                >
                  Log In
                </router-link>
                <router-link
                  v-else
                  :to="{ name: 'ProfileView' }"
                  class="button is-light"
                >
                  <font-awesome-icon icon="fa-solid fa-user" />
                  &nbsp;Profile
                </router-link>
                <router-link
                  :to="{ name: 'CartView' }"
                  class="button is-success"
                >
                  <font-awesome-icon icon="fa-solid fa-cart-shopping" />
                  &nbsp;Cart ({{ cartTotalQuantity }})
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div
      class="is-loading-bar has-text-centered"
      :class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section page-content">
      <div class="container is-widescreen">
        <router-view />
      </div>
    </section>

    <footer class="footer">
      <div class="columns">
        <div class="column is-2 content has-text-centered">
          <p>
            &copy;
            <a href="https://www.github.com/hazadus/" class="is-link">
              hazadus
            </a>
            2023
          </p>
        </div>
        <div class="column is-10 has-text-centered">
          <template v-if="!$store.state.isAuthenticated">
            <router-link :to="{ name: 'SignUpView' }" class="is-link">
              Sign Up
            </router-link>
            &middot;
            <router-link :to="{ name: 'LogInView' }" class="is-link">
              Log In
            </router-link>
          </template>
          <template v-else>
            <router-link :to="{ name: 'ProfileView' }" class="is-link">
              Profile
            </router-link>
          </template>
          &middot;
          <router-link :to="{ name: 'AboutView' }" class="is-link">
            About
          </router-link>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  computed: {
    cartTotalQuantity() {
      let totalQuantity = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalQuantity += this.cart.items[i].quantity;
      }

      return totalQuantity;
    },
  },
  beforeCreate() {
    // Load initial data from local storage
    this.$store.commit("initializeStore");

    // Configure axios headers
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Nunito:400,700");
$family-sans-serif: "Nunito", sans-serif;

@import "../node_modules/bulma";

.wrapper {
  min-height: 100vh;
}

/* 100vh - footer height - header height. Quick and dirty! */
.page-content {
  min-height: calc(100vh - 192px - 61px);
}

/* Loading indicator-related stuff */
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
