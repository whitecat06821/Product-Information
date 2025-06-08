<script setup lang="ts">
import UploadImage from '@/components/UploadImage.vue';
import ProductInfo from '@/components/ProductInfo.vue';
import Configuration from '@/components/PromptConfiguration.vue';
import Divider from '@/components/Divider.vue';
import { ref } from 'vue';
import { useCopyToClipboard } from '@/composables/useCopyToClipboard';

const currStatus = ref({
  data: null,
  isLoading: false,
  isError: false
});

const { isCopied, copyToJSON } = useCopyToClipboard();

const updateStatus = (status: any) => {
  currStatus.value = status;
}

const copy = () => {
  copyToJSON(currStatus.value.data)
}
</script>
<template>
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 p-6 lg:p-10 min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-300">
    <div class="flex flex-col items-center justify-center py-4 bg-white dark:bg-gray-800 rounded-lg shadow-xl">
      <upload-image />
      <div class="mt-8 px-4 w-full max-w-md">
        <divider :label="$t('configurations.header')" class="mb-6"/>
        <configuration @generate_status="updateStatus" />
      </div>
    </div>
    <div class="flex flex-col py-4 bg-white dark:bg-gray-800 rounded-lg shadow-xl">
      <product-info
        :product="currStatus.data"
        :isLoading="currStatus.isLoading"
        :isError="currStatus.isError"
        class="flex-grow p-4"
      />
      <button
        class="mt-6 rounded-md px-6 py-3 bg-sea-buckthorn-600 hover:bg-sea-buckthorn-700 text-white font-semibold relative mb-3 lg:w-auto self-center flex justify-center items-center gap-2 transition-all duration-300 transform hover:scale-105"
        v-if="currStatus.data"
        @click="copy"
      >
        <span :class="isCopied ? 'i-mingcute-check-line': 'i-mingcute-copy-line'" aria-hidden="true" />
        {{isCopied ? $t('copied') : $t('copy')}}
      </button>
    </div>
  </div>
</template>