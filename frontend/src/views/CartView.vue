<template>
  <div class="page-cart"></div>

  <div class="columns is-multiline">
    <div class="column is-12">
      <h1 class="title is-size-1">Cart</h1>
    </div>

    <div class="column is-23 box">
      <table v-if="cartTotalQuantity" class="table is-fullwidth is-hoverable">
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
          />
        </tbody>
      </table>

      <p v-else>Your cart is empty!</p>

      <div class="column is-4 is-offset-8 box has-text-centered">
        <h2 class="subtitle">Summary</h2>

        <strong>&euro; {{ cartTotalPrice.toFixed(2) }} </strong>,
        {{ cartTotalQuantity }} items

        <hr />

        <router-link to="/cart/checkout" class="button is-success">
          Proceed to checkout
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// import toast from "bulma-toast";

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
};
</script>
