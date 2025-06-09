<template>
  <div class="flex flex-col gap-6 lg:gap-10 h-full bg-white dark:bg-gray-800 rounded-lg shadow-custom dark:shadow-custom-dark transition-colors duration-300">
    <div class="flex flex-col gap-4 p-6 lg:p-10">
      <h1 class="text-2xl sm:text-3xl font-semibold text-gray-900 dark:text-gray-100">{{ $t('about.title') }}</h1>
      <app-divider />
      <div class="flex flex-col gap-3 text-gray-700 dark:text-gray-300">
        <p>{{ $t('about.description') }}</p>
        <p>{{ $t('about.subDescription') }}</p>
        <p class="text-gray-500 dark:text-gray-400 text-sm italic">{{ $t('about.disclaimer') }}</p>
      </div>
    </div>
    <div class="flex flex-col sm:flex-row gap-6 sm:gap-10 p-6 lg:p-10">
      <div class="flex flex-col gap-3 w-full">
        <h2 class="text-xl sm:text-2xl font-semibold text-gray-900 dark:text-gray-100">{{ $t('about.technologies') }}</h2>
        <app-divider />
        <div class="flex flex-col sm:flex-row gap-6 sm:gap-12 text-gray-700 dark:text-gray-300">
          <div class="flex flex-col gap-2">
            <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200">{{ $t('about.frontend') }}</h3>
            <ul class="list-disc pl-5">
              <li v-for="tech in $t('about.frontendList').split(',')" :key="tech">{{ tech }}</li>
            </ul>
          </div>
          <div class="flex flex-col gap-2">
            <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200">{{ $t('about.backend') }}</h3>
            <ul class="list-disc pl-5">
              <li v-for="tech in $t('about.backendList').split(',')" :key="tech">{{ tech }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import AppDivider from '@/components/AppDivider.vue';
</script>
