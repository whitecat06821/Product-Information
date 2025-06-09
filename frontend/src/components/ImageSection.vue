<template>
  <picture class="flex items-center">
    <source :srcset="url" media="(min-width:0px)">
    <img :src="url" alt="uploaded photo for product generation" class="rounded-md self-align w-full h-full object-cover"/>
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
/* Removed .image-wrapper styles as they are now applied directly to the img tag */
</style>