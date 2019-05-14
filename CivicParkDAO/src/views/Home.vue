<template>
  <v-container fluid class="mt-5">
    <v-layout justify-center align-center>
      <p>Welcome to RealTwin // </p>
      <p>beta-0.1</p>
    </v-layout>
    <v-layout justify-center align-center>
      <v-flex lg3 v-for="link in links.slice(0,2)" :key="link.name">
        <v-card height="180" width="200" elevation="3" hover>
          <v-img :src="link.image" height="100" width="100" class="ml-5"></v-img>
          <p class="text-none black--text text-lg-center mt-3">{{ link.name }}</p>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout justify-center align-center class="mt-3">
      <v-flex lg3 v-for="link in links.slice(2)" :key="link.name">
        <v-card height="180" width="200" elevation="3" hover>
          <v-img :src="link.image" height="100" width="100" class="ml-5"></v-img>
          <span class="text-none black--text text-lg-center mt-3">{{ link.name }}</span>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    name: 'Home',
    data: () => ({
      links: [
        {name: 'Home', image: require('../assets/house.png')},
        {name: 'Campaigns', image: require('../assets/digital-campaign.png')},
        {name: 'AI & Analytics', image: require('../assets/brain.png')},
        {name: 'Voting', image: require('../assets/business.png')}
        ,
      ],
    }),
    methods: {
      createCampaign: function () {
        this.axios.post('http://localhost:8000/api/v1/Campaign', {
          firstName: 'Fred',
          lastName: 'Flintstone'
        })
                .then(function (response) {
                  console.log(response);
                })
                .catch(function (error) {
                  console.log(error);
                });
      },
    }
  };
</script>

<style>

</style>
