<template>
  <div class="flex flex-col items-center gap-4 self-center w-full px-4">
    <image-section :url="selectedImage" v-if="selectedImage" />
    <div
      class="image-placeholder border-2 border-dashed rounded-lg flex flex-col items-center justify-center p-6 text-gray-400 dark:border-gray-600 dark:text-gray-500 bg-gray-50 dark:bg-gray-700 transition-colors duration-300 w-full h-full aspect-square overflow-hidden"
      :class="{'border-sea-buckthorn-500': selectedImage}"
      v-else
    >
      <span class="i-mingcute-pic-line text-5xl mb-2" aria-hidden="true" />
      <p class="text-center text-sm">{{ $t('upload.imagePlaceholder') }}</p>
    </div>
    <input
      type="file"
      tabindex="-1"
      accept=".jpeg,.jpg,.png,image/jpeg,image/png"
      class="hidden"
      id="file-upload"
      aria-label="upload image button"
      @change="selectFile"
      :disabled="isLoading"
    />
  </div>
</template>
<script setup lang="ts">
import { defineEmits, ref, defineExpose } from 'vue';
import ImageSection from '@/components/ImageSection.vue';
import { useConfigurations } from '@/composables/useConfigurations';

const emits = defineEmits(['upload_status', 'file_selected'])

const selectedImage = ref<string | null>(null);
const isLoading = ref(false);
const { setFile } = useConfigurations();

const selectFile = async (e: Event) => {
  const file = (e.target as HTMLInputElement)?.files?.[0];
  let isError = false;

  if (!file) return;
  isLoading.value = true;

  emits('upload_status', {
    isLoading: isLoading.value,
  });

  const readData = () => new Promise<string>(resolve => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result as string)
    reader.readAsDataURL(file);
  })

  try {
    selectedImage.value = await readData();
    setFile(file);
    emits('file_selected', file);
  } catch(e) {
    isError = true;
  } finally {
    isLoading.value = false;

    emits('upload_status', {
      isError,
      isLoading: isLoading.value
    });
  }
}

defineExpose({
  isLoading,
  selectedImage
})
</script>
<style>
.image-placeholder {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>