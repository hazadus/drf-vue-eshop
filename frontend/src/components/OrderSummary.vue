<template>
  <div class="box mb-4">
    <h4 class="is-size-4 mb-3">Order #{{ order.id }}</h4>
    <h5 class="is-size-5 mb-2">Delivery details</h5>
    <p class="mb-3">
      To: {{ order.first_name }} {{ order.last_name }}, {{ order.address }},
      {{ order.place }}. Phone: {{ order.phone }}, e-mail: {{ order.email }}
    </p>

    <h5 class="is-size-5 mb-3">Products</h5>

    <table class="table is-fullwidth">
      <thead>
        <tr>
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="item in order.items" :key="item.product.id">
          <td>{{ item.product.name }}</td>
          <td>&euro; {{ item.product.price }}</td>
          <td>{{ item.quantity }}</td>
          <td>&euro; {{ getItemTotal(item).toFixed(2) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "OrderSummary",
  props: {
    order: {
      type: Object,
      default() {
        return {};
      },
      required: true,
    },
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price;
    },
  },
};
</script>
