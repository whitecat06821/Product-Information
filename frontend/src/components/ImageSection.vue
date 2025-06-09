<template>
  <picture class="flex items-center">
    <source :srcset="url" media="(min-width:0px)">
    <img :src="url" alt="uploaded photo for product generation" class="rounded-md self-align sm:w-box image-wrapper"/>
  </picture>
</template>
<script lang="ts" setup>
import { defineProps } from 'vue';

const props = defineProps({
  url: {
    type: String,
    required: true
  },
});
</script>
<style scoped>
.image-wrapper {
  max-width: 100%;
  height: auto;
  object-fit: cover;
}
</style>