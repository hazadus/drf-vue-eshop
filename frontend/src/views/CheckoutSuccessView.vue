<template>
  <div class="page-checkout-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title is-size-1">Thank you for your order!</h1>

        <p>Your order will be processed within 48 hours.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CheckoutSuccessView",
  mounted() {
    document.title = "Thank you for your order! | vuEshop";
  },
};
</script>
