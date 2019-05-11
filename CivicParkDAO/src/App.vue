<template>
  <v-app id="inspire">
    <main-tool-bar/>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import MainToolBar from '@/components/MainToolBar.vue';

export default {
  name: 'App',
  components: { MainToolBar },
  data() {
    return {
      //
    };
  },
};
</script>
