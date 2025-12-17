<script setup>
  import Navbar from '@/components/Navbar.vue';
  import { RouterView } from 'vue-router';
</script>

<template>
  <div class=" items-center justify-center bg-gray-100">
    <Navbar />
    <RouterView />
  </div>
</template>