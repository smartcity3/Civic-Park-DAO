<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12 v-for="link in links" :key="link.name">
        <v-btn color="blue" :to="link.route">
          <v-icon class="mr-3" size="20" color="white">{{ link.icon }}</v-icon>
          <span class="text-none white--text">{{ link.name }}</span>
        </v-btn>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    links: [
      {
        icon: 'fas fa-table', name: 'Browse Campaigns', route: 'browse',
      },
      {
        icon: 'fas fa-plus', name: 'Create Campaign',
      },
      {
        icon: 'fas fa-chart-bar', name: 'AI & Analytics',
      },
      {
        icon: '', name: 'Other',
      },
    ],
  }),
};
</script>

<style>

</style>
