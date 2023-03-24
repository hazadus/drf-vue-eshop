<template>
  <div class="wrapper">
    <nav class="navbar is-link">
      <div class="container is-widescreen">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
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
            <router-link to="/vinyl-records/" class="navbar-item">
              Vinyl
            </router-link>
            <router-link to="/turntables/" class="navbar-item">
              Turntables
            </router-link>
            <router-link to="/mixers/" class="navbar-item">Mixers</router-link>
            <router-link to="/about/" class="navbar-item">About</router-link>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/log-in" class="button is-light">
                  Log In
                </router-link>
                <router-link to="/cart" class="button is-success">
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

    <section class="section">
      <div class="container is-widescreen">
        <router-view />
      </div>
    </section>

    <footer class="footer">
      <div class="content has-text-centered">
        <p>&copy; hazadus 2023</p>
      </div>
    </footer>
  </div>
</template>

<script>
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
    this.$store.commit("initializeStore");
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
