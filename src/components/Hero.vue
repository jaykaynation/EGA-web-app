<script setup>
  import { defineProps } from 'vue';

  defineProps ({
    title: {
      type: String,
      default: 'Your Playlist Generator'
    },
    subTitle: {
      type: String,
      default: 'Get Your AI Generated Playlist Now!'
    }
  });
</script>

<template>
  <section class="bg-blue-950 to-blue-950 py-20 mb-4 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col items-center">
      <div class="text-center">
        <h1 class="text-4xl font-extrabold sm:text-5xl md:text-6xl">
          {{ title }}
        </h1>
        <p class="my-4 text-xl">
          {{ subTitle }}
        </p>
      </div>
    </div>
  </section>
</template>