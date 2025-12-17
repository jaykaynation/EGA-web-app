<script setup>
  import Card from '@/components/Card.vue';
  // import { ref } from 'vue';
  import { reactive } from 'vue';
  import axios from 'axios';

  const selectedGenre = reactive({
    name: '',
    loading: false,
  });

  const returnedPlaylist = reactive({
    content: [],
    state: false,
  });

  const handleCreatePlaylist = async () => {
    selectedGenre.loading = true

    try{
      if (!selectedGenre.name){
        alert("Please Select A Genre")
        return;
      }

      console.log(selectedGenre.name) 
      
      //post request to backend here
      const res = await axios.post('http://localhost:3000/api/playlist_api', { genre: selectedGenre.name });
      const newPlaylist = JSON.parse(res.data.playlist.content);

      returnedPlaylist.content = newPlaylist.songs;
      returnedPlaylist.state = true;

      console.log("something", newPlaylist)
      console.log("Playlist Generated:", returnedPlaylist.content);

    } catch (err) {
      console.error("Error Generating Playlist:", err)
    } finally {
      selectedGenre.loading = false;
    }
  }
</script>

<template>
  <section class="py-4">
    <div class="container-xl lg:container m-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 rounded-lg">
        <Card>
          <h2 class="text-2xl font-bold">Select Your Genre Below</h2>
          <p class="mt-2 mb-4">
            Your AI agent will generate your playlist ASAP!
          </p>
          <select v-model="selectedGenre.name" class="mt-4 block w-full rounded-lg border border-gray-300 bg-white px-4 py-2 text-gray-800 shadow-sm focus:border-blue-100 focus:ring-1 focus:ring-blue-300 focus:outline-none">
            <option disabled selected value="">
              Select a genre
            </option>
            <option value="pop">Pop</option>
            <option value="jazz">Jazz</option>
            <option value="rock">Rock</option>
            <option value="hip-hop">Hip Hop</option>
            <option value="classical">Classical</option>
          </select>
          <div class="flex justify-end">
            <button @click="handleCreatePlaylist"
            :disabled="selectedGenre.loading"
            class="inline-block bg-black text-white rounded-lg px-4 py-2 mt-3 hover:bg-gray-700">
              {{ selectedGenre.loading ? "Loading..." : "Create Playlist" }}
            </button>
          </div>
        </Card>

        <!-- playlist card is here -->
        <Card v-if="selectedGenre.name != ''">
          <h2 class="text-2xl font-bold capitalize">{{ selectedGenre.name }} Playlist</h2>
  
          <!-- Loading State -->
          <div v-if="selectedGenre.loading" class="mt-8">
            <div class="inline-block animate-spin rounded-full h-9 w-9 border-b-2 border-gray-900">
            </div>
              <p class="mt-2 text-gray-600">Generating your playlist...</p>
          </div>
  
          <!-- Playlist Content -->
          <div v-else-if="returnedPlaylist.state && returnedPlaylist.content.length > 0" class="mt-4">
            <ul class="space-y-3">
              <li 
              v-for="(song, index) in returnedPlaylist.content" 
              :key="index"
              class="p-3 bg-gray-50 rounded-lg border border-gray-200 hover:bg-gray-100 transition-colors">
                <div class="flex items-start">
                  <span class="font-bold text-gray-700 mr-3">{{ index + 1 }}.</span>
                  <span class="text-gray-800">
                    <span class="text-red-700"> {{ song.title }} </span>
                    by 
                    <span class="text-blue-700"> {{ song.artist }} </span>
                  </span>
                </div>
              </li>
            </ul>
          </div>
  
          <!-- Empty State -->
          <div v-else class="mt-4 text-gray-500">
            <p>Click "Create Playlist" to generate songs</p>
          </div>

        </Card>

      </div>
    </div>
  </section>
</template>