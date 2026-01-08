<script setup>
  import { RouterLink, useRoute } from 'vue-router';

  const isActiveLink = (routePath) => {
    const route = useRoute();
    /** route.path accesses the actual route path */
    /** routePath is passed in to the function for comparison */
    return route.path === routePath; //returns true or false
  }
</script>

<template>
<nav class="bg-blue-950 border-b border-green-700">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between text-white">
        <div class="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
          <!-- Logo -->
          <div class="flex flex-shrink-0 items-center mr-4" to="/">
            <img class="h-10 w-auto" src="./../assets/logo.jpeg" alt="TuneAI Logo" />
            <span class="hidden md:block text-2xl font-bold ml-2">
              TuneAI
            </span>
          </div>
          <div class="md:ml-auto">
            <div class="flex space-x-2">
              
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>