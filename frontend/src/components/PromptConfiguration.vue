<template>
  <div class="mt-2 flex flex-col gap-6">
    <div>
      <label
        for="prompt-textarea"
        class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
        {{$t("configurations.prompt")}}
      </label>
      <textarea
        class="rounded-md p-3 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 w-full focus:ring-blue-500 focus:border-blue-500 transition-colors duration-300"
        type="text"
        id="prompt-textarea"
        :placeholder="$t('configurations.promptPlaceholder')"
        rows="3" maxlength="120"
        v-model="configurations.prompt"
      />
      <span class="text-xs text-gray-500 dark:text-gray-400 mt-1">
        {{$t("configurations.promptHint")}}
      </span>
    </div>
    <div>
      <label
        for="prompt-language"
        class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
        {{$t("configurations.language")}}
      </label>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        <radio-btn
          v-for="lang in languages"
          :key="lang.label"
          :label="lang.label"
          :value="lang.value"
          v-model="configurations.language"
        />
      </div>
    </div>
    <div>
      <label
        for="prompt-language"
        class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                {{$t("configurations.tone")}}
      </label>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        <radio-btn
          v-for="tone in tones"
          :key="tone.value"
          :label="tone.label"
          :value="tone.value"
          v-model="configurations.tone"
        />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { defineEmits, defineExpose } from 'vue';
import RadioBtn from '@/components/RadioBtn.vue';
import { useGenerate } from '@/composables/useGenerate';
import { useConfigurations } from '@/composables/useConfigurations';
import { useI18n } from 'vue-i18n';
import type { Product } from '@/types/Product';

const { generate, isLoading, isError } = useGenerate();
const { configurations } = useConfigurations();
const { t } = useI18n();
const emits = defineEmits(['generate_status']);

const languages = [{
  label: t('languages.en'),
  value: 'English'
}, {
  label: t('languages.es'),
  value: 'Spanish'
  }, {
  label: t('languages.vi'),
  value: 'Vietnamese'
}];
const tones = [{
  label: t("tones.neutral"),
  value: 'neutral'
}, {
  label: t("tones.formal"),
  value: 'formal'
}, {
  label: t("tones.engaging"),
  value: 'engaging'
}]

const generateProductInfo = () => {
  emits('generate_status', {
    data: null,
    isLoading,
    isError
  })

  generate((generatedResponse: { isLoading: boolean; isError: boolean; data: Product | null }) => {
    emits('generate_status', generatedResponse)
  })
}

defineExpose({
  generateProductInfo,
  isLoading
})
</script>