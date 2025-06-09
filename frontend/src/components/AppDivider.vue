<template>
  <div class="relative">
    <div :class="`w-full divider bg-${color} dark:bg-gray-700`" />
    <div class="divider-action absolute px-2 text-gray-500 dark:text-gray-400">
      <slot name="divider-action" class="divider-action absolute px-2">
        {{ label }}
      </slot>
    </div>
  </div>
</template>
<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps({
  label: {
    type: String,
  },
  color: {
    type: String,
    default: 'gray-200'
  }
});
</script>
<style>
.divider {
  height: 1px;
}

.divider-action {
  right: 20px;
  top: -15px;
}
</style>
