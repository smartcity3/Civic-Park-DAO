<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <v-card flat v-if="!(aprioriShow || associationShow)">
      <v-card-title>
        <span class="black--text font-weight-bold">Campaigns</span>
        <v-text-field mask="#.#" box
                      v-model="support"
                      label="Confidence Level"
                      required
                      class="apriori ml-5"
        >
        </v-text-field>
        <v-btn color="blue" round @click="postApriori" class="text-none">Apriori</v-btn>
        <v-btn color="green" round @click="postAssociationRules" class="text-none">Association Rules</v-btn>

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
    <v-card flat v-if="aprioriShow">
      <apriori-table :matched-campaigns="this.arrays"/>
    </v-card>
    <v-card flat v-if="associationShow">
      <association-rules-table :association-rules-data="this.arrays"/>
    </v-card>
  </div>
</template>

<script>
  import AprioriTable from "./AprioriTable";
  import AssociationRulesTable from "./AssociationRulesTable";

  export default {
    name: 'Browse',
    components: {AssociationRulesTable, AprioriTable},
    data() {
      return {
        apiEndpoint: 'http://localhost:8000/api/v1',
        search: '',
        shown: true,
        aprioriShow: false,
        associationShow: false,
        support: 0,
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
      };
    },
    created() {
      const {apiEndpoint} = this;
      this.axios.get(`${apiEndpoint}/campaigns/`)
          .then((response) => {
            this.$set(this, 'campaigns', response.data.campaigns);
          });
    },
    methods: {
      postApriori: function () {
        this.axios.post(`${this.apiEndpoint}/apriori/`, {"support": this.support.slice(0, 1) + '.' + this.support.slice(1)}).then((resp) => {
          this.arrays = JSON.parse(resp.data.apriori);
          this.aprioriShow = true;
        });
      },
      postAssociationRules: function () {
        this.axios.post(`${this.apiEndpoint}/associationrules/`, {"support": this.support.slice(0, 1) + '.' + this.support.slice(1)}).then((resp) => {
          this.arrays = JSON.parse(resp.data.association_rules);
          console.log(this.arrays);
          this.associationShow = true;
        });
      }
    }
  };
</script>

<style scoped>


  .apriori {
    width: 30px;
  }

</style>
