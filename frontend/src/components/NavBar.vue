<template>
  <nav class="flex flex-col sm:flex-row items-center justify-between p-4 bg-white dark:bg-gray-800 shadow-custom dark:shadow-custom-dark transition-colors duration-300">
    <div class="font-bold text-2xl text-sea-buckthorn-600 dark:text-sea-buckthorn-400 mb-4 sm:mb-0">
      AI Tagging Service
    </div>
    <div class="flex flex-col sm:flex-row gap-6 items-center">
      <div class="flex gap-4 sm:gap-6 items-center">
        <router-link
          to="/"
          class="text-gray-700 dark:text-gray-300 p-2 border-transparent border-b-2 hover:border-sea-buckthorn-500 dark:hover:border-sea-buckthorn-400 transition-colors duration-300 font-medium"
        >Home</router-link>
        <router-link
          to="/about"
          class="text-gray-700 dark:text-gray-300 p-2 border-transparent border-b-2 hover:border-sea-buckthorn-500 dark:hover:border-sea-buckthorn-400 transition-colors duration-300 font-medium"
        >About</router-link>
        <div class="flex gap-2 items-center">
          <a
            href="https://github.com/ren-418"
            target="_blank"
            alt="Github profile"
            class="text-gray-500 dark:text-gray-400 items-center flex hover:text-sea-buckthorn-500 dark:hover:text-sea-buckthorn-400 transition-colors duration-300">
            <span class="i-mingcube-github-2-fill text-3xl" aria-hidden="true"></span>
          </a>
          <a
            href="https://x.com/ren-418"
            target="_blank"
            alt="Twitter profile"
            class="text-gray-500 dark:text-gray-400 items-center flex hover:text-sea-buckthorn-500 dark:hover:text-sea-buckthorn-400 transition-colors duration-300">
            <span class="i-mingcube-twitter-fill text-3xl" aria-hidden="true"></span>
          </a>
        </div>
    </div>
      <div class="flex items-center gap-4">
        <LocaleSwitcher/>
        <ThemeToggle :current-theme="currentTheme" @toggle-theme="toggleTheme" />
      </div>
    </div>
  </nav>
</template>
<script setup lang="ts">
import { RouterLink } from 'vue-router';
import LocaleSwitcher from './LocaleSwitcher.vue';
import ThemeToggle from './ThemeToggle.vue';

const props = defineProps({
  currentTheme: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['toggle-theme'])

const toggleTheme = () => {
  emit('toggle-theme')
}
</script>
<style>
nav a.router-link-exact-active {
  @apply text-sea-buckthorn-800 border-b-2 border-sea-buckthorn-500 dark:text-sea-buckthorn-400 dark:border-sea-buckthorn-400;
}
</style>