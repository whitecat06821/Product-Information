<template>
  <footer class="text-sm text-center text-gray-600 dark:text-gray-400 py-5 border-t border-gray-200 dark:border-gray-700 transition-colors duration-300 bg-gray-50 dark:bg-gray-900">
    {{ $t('footer.madeby') }}
    <a href="https://ren-418.com" rel="noopener noreferrer" target="_blank" class="underline text-sea-buckthorn-600 hover:text-sea-buckthorn-700 dark:text-sea-buckthorn-400 dark:hover:text-sea-buckthorn-500 transition-colors duration-300">Ren</a>
    {{ $t('footer.withlove') }} - © {{ new Date().getFullYear() }}
  </footer>
</template>