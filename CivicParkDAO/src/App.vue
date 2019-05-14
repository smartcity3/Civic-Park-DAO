<template>
  <v-app id="inspire">
    <sidebar/>
    <main-tool-bar/>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
  import MainToolBar from './components/layout/MainToolBar.vue';
  import Sidebar from "./components/layout/Sidebar";

export default {
  name: 'App',
  components: {Sidebar, MainToolBar},
  data() {
    return {
      //
    };
  },
};
</script>
