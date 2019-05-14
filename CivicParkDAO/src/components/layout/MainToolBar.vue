<template>
  <v-toolbar color="white" dense fixed app height="64" flat class="toolbar">
    <v-flex class="justify-center">
      <v-btn to="/" flat color="transparent">
        <h2 class="font-weight-light title blue--text">Civic Park DAO</h2>
      </v-btn>
    </v-flex>
  </v-toolbar>
</template>

<script>
export default {
  name: 'MainToolBar',
};
</script>

<style scoped>

  .toolbar {
    border-bottom: 1px solid #e6e6e6 !important;
  }
</style>
