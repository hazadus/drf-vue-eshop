<template>
  <div class="home">
    <!-- Hero section -->
    <section class="hero is-medium is-info mb-6">
      <div class="hero-body has-text-centered">
        <p class="title is-size-1 mb-6">
          Welcome to <font-awesome-icon icon="fa-brands fa-vuejs" />uEshop!
        </p>
        <p class="subtitle">The best online record shop on the block!</p>
        <p>
          See <router-link to="/about">About</router-link> page to find out what
          this is all about.
        </p>
      </div>
    </section>

    <!-- Latest products list -->
    <div
      v-if="latestProducts.length"
      class="latest-products columns is-multiline"
    >
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductCard
        v-for="product in latestProducts"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import toast from "bulma-toast";

import ProductCard from "@/components/ProductCard.vue";

export default {
  name: "HomeView",
  components: {
    ProductCard,
  },
  data() {
    return {
      latestProducts: [],
    };
  },
  mounted() {
    document.title = "Welcome! | vuEshop";
    this.getLatestProducts();
  },
  methods: {
    async getLatestProducts() {
      /*
      NB: base URL for axios is set in `main.js`.
      */
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
          toast({
            message: `Something went wrong, please try again.`,
            type: "is-danger",
            dismissible: true,
            pauseOnHover: true,
            duration: 5000,
            position: "bottom-right",
          });
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
