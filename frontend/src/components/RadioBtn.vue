<template>
  <label class="inline-flex items-center cursor-pointer p-3 rounded-md border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-800 transition-all duration-300 w-full sm:w-auto hover:border-sea-buckthorn-500 dark:hover:border-sea-buckthorn-400"
    :class="{
      'bg-sea-buckthorn-100 dark:bg-sea-buckthorn-800 border-sea-buckthorn-500 dark:border-sea-buckthorn-400': selected === value,
      'shadow-custom dark:shadow-custom-dark': selected === value
    }">
      <input
        type="radio"
        class="form-radio h-5 w-5 text-sea-buckthorn-600 dark:text-sea-buckthorn-400 focus:ring-sea-buckthorn-500 dark:focus:ring-sea-buckthorn-400 border-gray-300 dark:border-gray-600 transition-colors duration-300"
        :value="value"
        v-model="selected">
        <span class="ml-2 text-gray-700 dark:text-gray-300 font-medium text-sm"
      >{{label}}</span>
  </label>
</template>
<script setup lang="ts">
import { defineProps, defineModel } from 'vue';

const props = defineProps({
  label: {
    type: String,
    required: true
  },
  value: {
    type: String,
    required: true
  }
});

const selected = defineModel();
</script>