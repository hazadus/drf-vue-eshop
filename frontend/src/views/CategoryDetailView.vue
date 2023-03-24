<template>
  <div class="category-detail-page">
    <div class="column is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">{{ category.name }}</h1>

        <div class="columns is-multiline">
          <div
            v-for="product in category.products"
            :key="product.id"
            class="column is-3"
          >
            <div class="box">
              <figure class="image mb-4">
                <img :src="product.thumbnail_url" />
              </figure>

              <h4 class="is-size-4 mb-3">{{ product.name }}</h4>
              <p class="is-size-6 has-text-grey mb-4">
                &euro;{{ product.price }}
              </p>

              <router-link
                :to="product.get_absolute_url"
                class="button is-link"
              >
                View details
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "CategoryDetailView",
  data() {
    return {
      category: {
        products: [],
      },
    };
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

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
