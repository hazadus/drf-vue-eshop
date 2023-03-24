<template>
  <!-- NB: `v-if="product"` below is to exclude `marked` errors when data is not yet loaded from API -->
  <div v-if="product" class="page-product-detail">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img :src="product.thumbnail_url" style="max-width: 300px" />
        </figure>

        <h1 class="title is-size-1">{{ product.name }}</h1>
        <span v-html="markdownToHtml(product.description)"></span>
      </div>

      <div class="column is-3">
        <h2 class="title is-size-2">Purchase Item</h2>
        <p><strong>Price:</strong> &euro;{{ product.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <!-- NB: `type="number"` to auto convert input data -->
            <input v-model="quantity" type="number" class="input" min="1" />
          </div>
          <div class="control">
            <button class="button is-link" @click="addToCart">
              <font-awesome-icon icon="fa-solid fa-cart-shopping" />
              &nbsp;Add to cart
            </button>
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
  name: "ProductDetailView",
  data() {
    return {
      product: null,
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      this.$store.commit("setIsLoading", true);

      const categorySlug = this.$route.params.categorySlug;
      const productSlug = this.$route.params.productSlug;

      await axios
        .get(`/api/v1/products/${categorySlug}/${productSlug}/`)
        .then((response) => {
          this.product = response.data;
          document.title = this.product.name + " | vuEshop";
        })
        .catch((error) => {
          console.log(error);
        });

      // NB: async/await above ensures this will be executed when axios.get() is complete:
      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      /*
      Add product to cart (Vuex Store).
      Display Bulma toast message.
      */
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        product: this.product,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);

      toast({
        message: `"${this.product.name}"x${this.quantity} was added to the cart.`,
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 5000,
        position: "bottom-right",
      });
    },
    markdownToHtml(markedDownContent) {
      /*
       Sanitizes `markedDownContent` and converts markdown to HTML.
       */
      return this.markdown(markedDownContent);
    },
  },
};
</script>
