<template>
  <div class='flex flex-col items-center gap-2 w-full max-w-xs'>
    <div :class="`h-2 w-full rounded-full bg-${color}-100 dark:bg-${color}-900 overflow-hidden`">
      <div :class="`progress h-full bg-${color}-500 dark:bg-${color}-400 left-right rounded-full`"/>
    </div>
    <span v-if="label" :class="`text-${labelColor} dark:text-gray-300 text-sm font-medium`">{{ label }}</span>
  </div>
</template>
<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps({
  label: {
    type: String,
  },
  color: {
    type: String,
    default: 'sea-buckthorn'
  },
  labelColor: {
    type: String,
    default: 'gray-500'
  }
});
</script>
<style>
.progress {
  animation: progress 1s infinite linear;
}

.left-right {
    transform-origin: 0% 50%;
}
    @keyframes progress {
    0% {
        transform:  translateX(0) scaleX(0);
    }
    40% {
        transform:  translateX(0) scaleX(0.4);
    }
    100% {
        transform:  translateX(100%) scaleX(0.5);
    }
}
</style>