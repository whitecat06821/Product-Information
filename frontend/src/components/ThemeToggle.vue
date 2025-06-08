<script setup lang="ts">
import { SunIcon, MoonIcon } from '@heroicons/vue/24/solid'

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

<template>
  <button
    @click="toggleTheme"
    class="p-2 rounded-full text-gray-500 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 dark:focus:ring-offset-gray-800 focus:ring-blue-500 transition-colors duration-300"
    aria-label="Toggle theme"
  >
    <MoonIcon v-if="currentTheme === 'light'" class="h-6 w-6" />
    <SunIcon v-else class="h-6 w-6" />
  </button>
</template>