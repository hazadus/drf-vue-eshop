<template>
  <div class="about">
    <h1 class="title is-size-1">About the project</h1>
    <h2 class="subtitle">What this stuff is all about</h2>

    <p>This is a tutorial project to learn more about Django, DRF and Vue3.</p>

    <p>Write about what I have learned while doing this project.</p>

    <p>
      Source code:
      <font-awesome-icon icon="fa-brands fa-github" />
      <a href="https://www.github.com/hazadus/drf-vue-eshop/">
        hazadus/drf-vue-eshop
      </a>
    </p>
  </div>
</template>

<script>
export default {
  name: "AboutView",
  mounted() {
    document.title = "About the project | vuEshop";
  },
};
</script>
