<template>
  <div class="page-product-detail">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img :src="product.thumbnail_url" style="max-width: 300px" />
        </figure>

        <h1 class="title is-size-1">{{ product.name }}</h1>
        <p>{{ product.description }}</p>
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
            <a class="button is-link">
              <font-awesome-icon icon="fa-solid fa-cart-shopping" />
              &nbsp;Add to cart
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductDetailView",
  data() {
    return {
      product: Object,
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    getProduct() {
      const categorySlug = this.$route.params.categorySlug;
      const productSlug = this.$route.params.productSlug;

      axios
        .get(`/api/v1/products/${categorySlug}/${productSlug}/`)
        .then((response) => {
          this.product = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
