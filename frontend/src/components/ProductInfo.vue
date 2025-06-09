<template>
  <div v-if="!product || isLoading || isError" 
    class="flex flex-col items-center justify-center border-2 border-dashed rounded-lg p-6 text-gray-400 dark:border-gray-600 dark:text-gray-500 bg-gray-50 dark:bg-gray-700 transition-colors duration-300 h-full"
  >
    <progress-bar v-if="isLoading" :label="$t('isGenerating')" />
    <p v-else-if="isError" class="text-center">{{$t("productInfo.error")}}</p>
    <p v-else class="text-center">{{ $t('productInfo.placeholder')}}</p>
  </div>
  <div 
    class="flex flex-col border border-gray-200 dark:border-gray-700 rounded-lg p-6 gap-6 h-full bg-white dark:bg-gray-800 transition-colors duration-300 overflow-auto"
    v-else
  >
    <div class="flex flex-col gap-2 w-full">
      <h2 class="font-semibold text-gray-700 dark:text-gray-300">{{$t('productInfo.title')}}</h2>
      <p class="bg-gray-50 dark:bg-gray-900 p-3 rounded-md border border-gray-100 dark:border-gray-700 text-gray-800 dark:text-gray-200">{{ product.title }}</p>
    </div>
    <div class="flex flex-col gap-2 w-full flex-grow">
      <h2 class="font-semibold text-gray-700 dark:text-gray-300">{{$t('productInfo.description')}}</h2>
      <p class="bg-gray-50 dark:bg-gray-900 p-3 rounded-md border border-gray-100 dark:border-gray-700 text-gray-800 dark:text-gray-200 flex-grow">{{ product.description }}</p>
    </div>
    <div class="flex flex-col gap-2 w-full">
      <h2 class="font-semibold text-gray-700 dark:text-gray-300">{{$t('productInfo.tags')}}</h2>
      <p class="bg-gray-50 dark:bg-gray-900 p-3 rounded-md border border-gray-100 dark:border-gray-700 text-gray-800 dark:text-gray-200">{{ product.tags?.join(', ') }}</p>
    </div>
    <div class="flex flex-col gap-2 w-full" v-if="product.colors && product.colors.length > 0">
      <h2 class="font-semibold text-gray-700 dark:text-gray-300">{{$t('productInfo.colors')}}</h2>
      <div class="flex flex-wrap gap-2">
        <span v-for="color in product.colors" :key="color" class="px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800 dark:bg-blue-800 dark:text-blue-100">
          {{ color }}
        </span>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { defineProps, type PropType } from 'vue';
import ProgressBar from '@/components/ProgressBar.vue';
import type { Product } from '@/types/Product';

const props = defineProps({
  product: {
    type: Object as PropType<Product | null>,
  },
  isLoading: {
    type: Boolean,
    default: false
  },
  isError: {
    type: Boolean,
    default: false
  }
});

const placeholder = "Generated product information will appear here";
</script>
<style>
.product-placeholder {
  min-height: 200px;
  /* Ensure this takes available height when in column layout */
  flex-grow: 1;
}
</style>