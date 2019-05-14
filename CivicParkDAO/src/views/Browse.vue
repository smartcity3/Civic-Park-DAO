<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-container fluid fill-height>
    <v-card flat>
      <v-card-title>
        <span class="black--text font-weight-bold">Campaigns</span>
        <v-text-field mask="#" box
                      v-model="name"
                      :rules="aprioriRules"
                      label="Confidence Level"
                      required
                      class="apriori ml-5"
        >
        </v-text-field>
        <v-btn color="blue" round>Confirm</v-btn>
        <v-spacer></v-spacer>
        <v-text-field
                v-model="search"
                label="Search"
                single-line
                hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
              :headers="headers"
              :items="campaigns"
              :search="search"
              hide-actions
      >
        <template v-slot:items="props">
          <td>{{ props.item.campaignName }}</td>
          <td>{{ props.item.owner }}</td>
          <td class="text-xs-center">{{ props.item.Mobility }}</td>
          <td class="text-xs-center">{{ props.item.Economy }}</td>
          <td class="text-xs-center">{{ props.item.RoadTrans }}</td>
          <td class="text-xs-center">{{ props.item.ArtificialIntelligence }}</td>
          <td class="text-xs-center">{{ props.item.AutonomousVehicles }}</td>
          <td class="text-xs-center">{{ props.item.IoT }}</td>
          <td class="text-xs-center">{{ props.item.Sensors }}</td>
          <td class="text-xs-center">{{ props.item.Safety }}</td>
        </template>
        <template v-slot:no-results>
          <v-alert :value="true" color="error" icon="warning">
            Your search for "{{ search }}" found no results.
          </v-alert>
        </template>
      </v-data-table>
    </v-card>

  </v-container>
</template>

<script>
export default {
  name: 'Browse',
  data() {
    return {
      apiEndpoint: 'http://localhost:8000/api/v1',
      search: '',
      headers: [
        {
          text: 'Campaigns',
          align: 'center',
          sortable: true,
          value: 'campaignName',
        },
        {
          text: 'Owner',
          align: 'center',
          sortable: true,
          value: 'owner',
        },
        {text: 'Mobility', value: 'Mobility', align: 'center', sortable: true,},
        {text: 'Economy', value: 'Economy', align: 'center', sortable: true,},
        {text: 'RoadTrans', value: 'RoadTrans', align: 'center', sortable: true,},
        {text: 'ArtificialIntelligence', value: 'ArtificialIntelligence', align: 'center', sortable: true,},
        {text: 'AutonomousVehicles', value: 'AutonomousVehicles', align: 'center', sortable: true,},
        // { text: 'TGeospatial', value: '' },
        {text: 'IoT', value: 'IoT', align: 'center', sortable: true,},
        {text: 'Sensors', value: 'Sensors', align: 'center', sortable: true,},
        {text: 'Safety', value: 'Safety', align: 'center', sortable: true,},
      ],
      campaigns: [],
      aprioriRules: [
        v => (parseInt(v) >= 0.0 && parseInt(v) <= 0.90) || 'Confidence Level is required',
      ]
    };
  },
  created() {
    const { apiEndpoint } = this;
    this.axios.get(`${apiEndpoint}/campaigns/`).then((response) => {
      this.$set(this, 'campaigns', response.data.campaigns);
      console.log(this.campaigns);
    });
  },
};
</script>

<style scoped>


  .apriori {
    width: 30px;
  }

</style>
