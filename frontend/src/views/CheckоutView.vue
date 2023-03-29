<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">Checkout</h1>
        <h2 class="subtitle mb-3">Make payment and place the order</h2>
      </div>
    </div>
  </div>

  <div class="column is-12 box">
    <table class="table is-fullwidth is-hoverable">
      <thead>
        <tr>
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="item in cart.items" :key="item.product.id">
          <td>{{ item.product.name }}</td>
          <td>${{ item.product.price }}</td>
          <td>{{ item.quantity }}</td>
          <td>${{ getItemTotalPrice(item).toFixed(2) }}</td>
        </tr>
      </tbody>

      <tfoot>
        <tr>
          <td colspan="2">Total</td>
          <td>{{ cartTotalQuantity }}</td>
          <td>&euro; {{ cartTotalPrice.toFixed(2) }}</td>
        </tr>
      </tfoot>
    </table>
  </div>

  <div class="column is-12 box">
    <h2 class="title is-size-2">Shipping details</h2>
    <h3 class="subtitle mb-3">All fields are required</h3>

    <div class="columns is-multiline">
      <div class="column is-6">
        <div class="field">
          <label>First name*</label>
          <div class="control">
            <input v-model="firstName" type="text" class="input" />
          </div>
        </div>

        <div class="field">
          <label>Last name*</label>
          <div class="control">
            <input v-model="lastName" type="text" class="input" />
          </div>
        </div>

        <div class="field">
          <label>E-mail*</label>
          <div class="control">
            <input v-model="email" type="email" class="input" />
          </div>
        </div>

        <div class="field">
          <label>Phone*</label>
          <div class="control">
            <input v-model="phone" type="text" class="input" />
          </div>
        </div>
      </div>

      <div class="column is-6">
        <div class="field">
          <label>Address*</label>
          <div class="control">
            <input v-model="address" type="text" class="input" />
          </div>
        </div>

        <div class="field">
          <label>Place*</label>
          <div class="control">
            <input v-model="place" type="text" class="input" />
          </div>
        </div>
      </div>
    </div>

    <div v-if="errors.length" class="notification is-danger mt-4">
      <p v-for="error in errors" :key="error">{{ error }}</p>
    </div>

    <hr />

    <div id="card-element" class="mb-5"></div>

    <template v-if="cartTotalQuantity">
      <hr />

      <div class="column is-12 has-text-right">
        <button class="button is-success" @click="submitForm">
          Pay (demo, no real payment!)
        </button>
      </div>
    </template>
  </div>
</template>

<script>
//import axios from "axios";

export default {
  name: "CheckOutView",
  components: {},
  data() {
    return {
      cart: {
        items: [],
      },
      card: {},
      firstName: "",
      lastName: "",
      email: "",
      phone: "",
      address: "",
      place: "",
      errors: [],
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
    document.title = "Check Out | vuEshop";
    this.cart = this.$store.state.cart;
  },
  methods: {
    getItemTotalPrice(item) {
      return item.quantity * item.product.price;
    },
    submitForm() {
      this.errors = [];

      if (this.firstName === "") {
        this.errors.push("The first name is missing!");
      }
      if (this.lastName === "") {
        this.errors.push("The last name is missing!");
      }
      if (this.email === "") {
        this.errors.push("The email is missing!");
      }
      if (this.phone === "") {
        this.errors.push("The phone is missing!");
      }
      if (this.address === "") {
        this.errors.push("The address is missing!");
      }
      if (this.place === "") {
        this.errors.push("The place is missing!");
      }

      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true);

        // Proceed with real payment stuff here!

        this.$store.commit("setIsLoading", false);

        this.$store.commit("clearCart");
        this.$router.push("/cart/success/");
      }
    },
  },
};
</script>
