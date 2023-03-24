<template>
  <div class="category-detail-page">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">
          All products in &laquo;{{ category.name }}&raquo;
        </h1>
      </div>

      <ProductCard
        v-for="product in category.products"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

import ProductCard from "@/components/ProductCard.vue";

export default {
  name: "CategoryDetailView",
  components: {
    ProductCard,
  },
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  watch: {
    // eslint-disable-next-line
    $route(to, from) {
      if (to.name === "CategoryDetailView") {
        this.getCategoryDetails();
      }
    },
  },
  mounted() {
    this.getCategoryDetails();
  },
  methods: {
    async getCategoryDetails() {
      this.$store.commit("setIsLoading", true);

      const categorySlug = this.$route.params.categorySlug;

      await axios
        .get(`/api/v1/products/${categorySlug}/`)
        .then((response) => {
          this.category = response.data;
          document.title = this.category.name + " | vuEshop";
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
