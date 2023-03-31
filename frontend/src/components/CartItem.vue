<template>
  <tr>
    <td>
      <router-link :to="item.product.get_absolute_url">
        {{ item.product.name }}
      </router-link>
    </td>
    <td>&euro; {{ item.product.price }}</td>
    <td>
      <div class="columns">
        <div class="column is-6">
          {{ item.quantity }}
        </div>
        <div class="buttons has-addons">
          <button
            class="button is-small is-outlined is-rounded p-3 is-danger"
            @click="decrementQuantity(item)"
          >
            -
          </button>
          <button
            class="button is-small is-outlined is-rounded p-3 is-success"
            @click="incrementQuantity(item)"
          >
            +
          </button>
        </div>
      </div>
    </td>
    <td>&euro; {{ getItemTotal(item).toFixed(2) }}</td>
    <td>
      <button class="delete" @click="removeFromCart(item)"></button>
    </td>
  </tr>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: {
      type: Object,
      default() {
        return {};
      },
      required: true,
    },
  },
  emits: ["removeFromCart"],
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;
      if (item.quantity === 0) {
        this.removeFromCart(item);
      }
      this.updateCart();
    },
    incrementQuantity(item) {
      item.quantity += 1;
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },
  },
};
</script>
