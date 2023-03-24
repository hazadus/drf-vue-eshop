<!-- Intended to be inside `<div class="columns is-multiline">` -->
<template>
  <div class="column is-3 is-flex">
    <div class="box is-flex is-flex-direction-column">
      <figure class="image mb-4">
        <img :src="product.thumbnail_url" />
      </figure>

      <h4 class="is-size-4 mb-3 is-flex-grow-1">{{ product.name }}</h4>
      <p class="is-size-5 has-text-grey mb-4 has-text-right">
        &euro;{{ product.price }}
      </p>

      <router-link :to="product.get_absolute_url" class="button is-link">
        View details
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductCard",
  props: {
    product: Object,
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}

.image img {
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
}
</style>
