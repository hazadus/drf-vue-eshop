<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">Search results</h1>
        <h2 class="subtitle">
          {{ products.length }} results for term &laquo;{{ query }}&raquo;
        </h2>
      </div>

      <ProductCard
        v-for="product in products"
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
  name: "SearchView",
  components: {
    ProductCard,
  },
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = `Searching... | vuEshop`;

    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");
      this.performSearch();
    }
  },
  methods: {
    async performSearch() {
      this.$store.commit("setIsLoading", true);

      await axios
        .post(`/api/v1/products/search/`, { query: this.query })
        .then((response) => {
          this.products = response.data;
          document.title = `Search results for "${this.query}" | vuEshop`;
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

      // NB: async/await above ensures this will be executed when axios.get() is complete:
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
