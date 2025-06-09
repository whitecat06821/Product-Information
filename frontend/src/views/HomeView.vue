<script setup lang="ts">
import UploadImage from '@/components/UploadImage.vue';
import ProductInfo from '@/components/ProductInfo.vue';
import Configuration from '@/components/PromptConfiguration.vue';

import { ref, watch } from 'vue';
import { useCopyToClipboard } from '@/composables/useCopyToClipboard';
import { useConfigurations } from '@/composables/useConfigurations';

const uploadImageRef = ref<InstanceType<typeof UploadImage> | null>(null);
const configurationRef = ref<InstanceType<typeof Configuration> | null>(null);

const currStatus = ref({
  data: null,
  isLoading: false,
  isError: false
});

const { isCopied, copyToJSON } = useCopyToClipboard();
const { configurations } = useConfigurations();

const updateStatus = (status: any) => {
  currStatus.value = status;
}

const copy = () => {
  copyToJSON(currStatus.value.data)
}

const triggerFileInput = () => {
  document.getElementById('file-upload')?.click();
};

const handleFileSelected = (file: File) => {
  if (uploadImageRef.value) {
    configurations.file = file;
  }
};

watch(() => configurationRef.value?.isLoading, (newVal) => {
  currStatus.value.isLoading = newVal ?? false;
});

</script>
<template>
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 bg-gray-50 dark:bg-gray-900 transition-colors duration-300 h-full w-full p-4 lg:p-8">
    <div class="flex flex-col items-center justify-center bg-white dark:bg-gray-800 rounded-lg shadow-xl h-full overflow-y-auto p-4 lg:p-8">
      <div class="flex flex-col w-full h-full">
        <div class="flex flex-col lg:flex-row items-center gap-4 w-full h-full">
          <upload-image ref="uploadImageRef" class="flex-grow" @file_selected="handleFileSelected" />
          <div class="w-full max-w-md">
            <configuration ref="configurationRef" @generate_status="updateStatus" />
          </div>
        </div>
        <div class="flex flex-col lg:flex-row gap-4 mt-6 w-full justify-center pb-4">
          <button
            class="rounded-md px-6 py-3 text-white font-semibold relative flex justify-center gap-2 items-center transition-all duration-300 transform hover:scale-105 w-full lg:w-auto"
            @click="triggerFileInput"
            :disabled="uploadImageRef?.isLoading"
            :class="uploadImageRef?.isLoading ? 'cursor-not-allowed bg-sea-buckthorn-300 dark:bg-sea-buckthorn-700' : 'cursor-pointer bg-sea-buckthorn-600 hover:bg-sea-buckthorn-700 dark:bg-sea-buckthorn-500 dark:hover:bg-sea-buckthorn-600'"
          >
            <span class="i-mingcute-upload-2-line" aria-hidden="true" />
            {{ uploadImageRef?.isLoading ? $t('upload.isUploading') : $t('upload.label') }}
          </button>
          <button
            class="rounded-md px-6 py-3 text-white font-semibold self-center flex justify-center items-center gap-2 transition-all duration-300 transform hover:scale-105 w-full lg:w-auto"
            @click="configurationRef?.generateProductInfo()"
            :disabled="!configurations.file || configurationRef?.isLoading"
            :class="!configurations.file || configurationRef?.isLoading ? 'bg-gray-400 dark:bg-gray-700 cursor-not-allowed' : 'bg-sea-buckthorn-600 hover:bg-sea-buckthorn-700 dark:bg-sea-buckthorn-500 dark:hover:bg-sea-buckthorn-600'"
          >
            <span class="i-mingcute-box-3-line" aria-hidden="true" />
            {{ configurationRef?.isLoading ? $t("isGenerating") : $t("generate") }}
          </button>
        </div>
      </div>
    </div>
    <div class="flex flex-col bg-white dark:bg-gray-800 rounded-lg shadow-xl h-full overflow-y-auto p-4 lg:p-8">
      <product-info
        :product="currStatus.data"
        :isLoading="currStatus.isLoading"
        :isError="currStatus.isError"
        class="flex-grow"
      />
      <button
        class="mt-6 rounded-md px-6 py-3 bg-sea-buckthorn-600 hover:bg-sea-buckthorn-700 text-white font-semibold relative mb-0 lg:w-auto self-center flex justify-center items-center gap-2 transition-all duration-300 transform hover:scale-105"
        v-if="currStatus.data"
        @click="copy"
      >
        <span :class="isCopied ? 'i-mingcute-check-line': 'i-mingcute-copy-line'" aria-hidden="true" />
        {{isCopied ? $t('copied') : $t('copy')}}
      </button>
    </div>
  </div>
</template>