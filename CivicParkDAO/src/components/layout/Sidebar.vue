<template>
  <v-navigation-drawer v-model="drawer" permanent app width="220" class="nav">
    <v-toolbar flat class="transparent">
      <v-list class="pa-0">
        <v-list-tile avatar>
          <v-list-tile-avatar size="30">
            <img src="https://randomuser.me/api/portraits/men/85.jpg" alt="Avatar">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title class="text--darken-3 grey--text">xB54G4L4...</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-list class="pt-0" dense>
      <v-divider></v-divider>
      <p class="grey--text caption mt-3 ml-4">APPS</p>
      <v-list-tile
              v-for="item in items"
              :key="item.title"
              :to="item.link"

      >

        <v-list-tile-action class="ml-2">
          <v-icon size="20" :color="item.color">{{ item.icon }}</v-icon>
        </v-list-tile-action>

        <v-list-tile-content>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>

  </v-navigation-drawer>
</template>

<script>
  export default {
    name: 'Sidebar',
    data() {
      return {
        drawer: true,
        items: [
          {title: 'Home', icon: 'fas fa-home', color: 'blue lighten-3', link: '/'},
          {title: 'Campaigns', icon: 'fas fa-pager', color: 'deep-purple lighten-3', link: '/browse'},
          {title: 'AI & Analytics', icon: 'fas fa-chart-bar', color: 'orange lighten-3', link: '/ai'},
          {title: 'Voting', icon: 'fas fa-vote-yea', color: 'green lighten-3', link: 'voting'}

        ],
        right: null
      };
    }
  };

</script>

<style scoped>

  .nav {
    box-shadow: rgba(0, 0, 0, 0.1) 1px 0 15px;
  }

</style>
