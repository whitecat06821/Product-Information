<template>
  <div class="locale-switcher">
    <div class="relative inline-block text-left">
      <select
        v-model="$i18n.locale"
        class="block appearance-none w-full bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 text-gray-800 dark:text-gray-200 py-2 px-4 pr-8 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-sea-buckthorn-500 focus:border-sea-buckthorn-500 transition-colors duration-300 cursor-pointer"
      >
        <option
          v-for="locale in $i18n.availableLocales"
          :key="`locale-${locale}`"
          :value="locale"
          class="bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200"
        >
          {{ getLocaleLabel(locale).label }}
        </option>
      </select>
      <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 dark:text-gray-300">
        <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
          <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 6.757 7.586 5.343 9z" />
        </svg>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
const localeLabels: { [key: string]: { label: string; icon: string } } = {
    en: {
        label: 'English',
        icon: "united-kingdom"
    },
    es: {
        label: 'Spanish',
        icon: "spain"
    },
    vi: {
        label: 'Tiếng Việt',
        icon: "vietnam"
    },
}

const getLocaleLabel = (locale: string) => {
    return localeLabels[locale] || localeLabels.en;
}
</script>