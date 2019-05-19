<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-data-table
          :headers="headers"
          :items="matchedCampaigns"
          :search="search"
          hide-actions
  >
    <template v-slot:items="props">
      <td class="text-xs-center">{{ props.item.itemsets }}</td>
      <td class="text-xs-center">{{ props.item.support }}</td>
    </template>
    <template v-slot:no-results>
      <v-alert :value="true" color="error" icon="warning">
        Your search for "{{ search }}" found no results.
      </v-alert>
    </template>
  </v-data-table>
</template>

<script>
  export default {
    name: "AprioriTable",
    props: ['matchedCampaigns'],
    data() {
      return {
        search: '',
        headers: [
          {
            text: 'Matched Campaigns',
            align: 'center',
            sortable: true,
            value: 'itemsets',
          },
          {
            text: 'Support',
            align: 'center',
            sortable: true,
            value: 'support',
          },
        ],
      };
    }
  };
</script>

<style scoped>

</style>