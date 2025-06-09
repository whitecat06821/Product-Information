<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import AppFooter from './components/AppFooter.vue'
import { ref, onMounted, watch } from 'vue'

const theme = ref(localStorage.getItem('theme') || 'light')

const toggleTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}

watch(theme, (newTheme) => {
  document.documentElement.classList.toggle('dark', newTheme === 'dark')
  localStorage.setItem('theme', newTheme)
})

onMounted(() => {
  document.documentElement.classList.toggle('dark', theme.value === 'dark')
})
</script>

<template>
  <nav-bar @toggle-theme="toggleTheme" :current-theme="theme" />
  <main class="flex-grow flex flex-col overflow-y-auto">
    <RouterView class="w-full h-full" />
  </main>
  <app-footer />
</template>

<style>
/* Global styles for theme transitions */
html.dark {
  /* Add global dark mode styles here if needed */
  background-color: #1a202c; /* Example dark background */
  color: #e2e8f0; /* Example dark text color */
}

/* Base styles to ensure smooth transitions */
html {
  transition: background-color 0.3s ease, color 0.3s ease;
}
</style>
