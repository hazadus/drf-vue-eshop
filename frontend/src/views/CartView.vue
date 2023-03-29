<template>
  <div class="page-cart"></div>

  <h1 class="title is-size-1">Cart</h1>

  <div v-if="cartTotalQuantity" class="columns is-multiline">
    <div class="column is-23 box">
      <table class="table is-fullwidth is-hoverable">
        <thead>
          <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
            <th><!-- Column for buttons --></th>
          </tr>
        </thead>
        <tbody>
          <CartItem
            v-for="item in cart.items"
            :key="item.id"
            :initial-item="item"
            @remove-from-cart="removeFromCart(item)"
          />
        </tbody>

        <div class="columns is-fullwidth"></div>
      </table>
    </div>
    <div class="column is-4 is-offset-8 box has-text-centered">
      <h2 class="subtitle">Summary</h2>

      <strong>&euro; {{ cartTotalPrice.toFixed(2) }} </strong>,
      {{ cartTotalQuantity }} items

      <hr />

      <button class="button is-warning mr-2" @click="clearCart">
        Clear cart
      </button>
      <router-link :to="{ name: 'CheckoutView' }" class="button is-success">
        Proceed to checkout
      </router-link>
    </div>
  </div>
  <p v-else>Your cart is empty!</p>
</template>

<script>
import CartItem from "@/components/CartItem.vue";

export default {
  name: "CartView",
  components: {
    CartItem,
  },
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  computed: {
    cartTotalQuantity() {
      return this.cart.items.reduce((accumulated, currentItem) => {
        return (accumulated += currentItem.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((accumulated, currentItem) => {
        return (accumulated +=
          currentItem.product.price * currentItem.quantity);
      }, 0);
    },
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  methods: {
    clearCart() {
      this.$store.commit("clearCart");
      this.cart = { items: [] };
      this.$router.push({ name: "HomeView" });
    },
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (currentItem) => currentItem.product.id !== item.product.id
      );
    },
  },
};
</script>
