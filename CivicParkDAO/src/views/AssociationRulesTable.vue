<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-data-table
          :headers="headers"
          :items="associationRulesData"
          :search="search"
          hide-actions
  >
    {{ associationRulesData }}
    <template v-slot:items="props">
      <td class="text-xs-center">{{ props.item.antecedents }}</td>
      <td class="text-xs-center">{{ props.item.consequents }}</td>
      <td class="text-xs-center">{{ props.item.antecedent_support }}</td>
      <td class="text-xs-center">{{ props.item.consequent_support }}</td>
      <td class="text-xs-center">{{ props.item.support }}</td>
      <td class="text-xs-center">{{ props.item.confidence }}</td>
      <td class="text-xs-center">{{ props.item.lift }}</td>
      <td class="text-xs-center">{{ props.item.leverage }}</td>
      <td class="text-xs-center">{{ props.item.conviction }}</td>
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
    name: "AssociationRulesTable",
    props: ['associationRulesData'],
    data() {
      return {
        search: '',
        headers: [
          {
            text: 'Antecedents',
            align: 'center',
            sortable: true,
            value: 'antecedents',
          },
          {
            text: 'Consequents',
            align: 'center',
            sortable: true,
            value: 'consequents',
          },
          {
            text: 'Antecedent Support',
            align: 'center',
            sortable: true,
            value: 'antecedent_support',
          },
          {
            text: 'Consequent Support',
            align: 'center',
            sortable: true,
            value: 'consequent_support',
          },
          {
            text: 'Support',
            align: 'center',
            sortable: true,
            value: 'support',
          },
          {
            text: 'Confidence',
            align: 'center',
            sortable: true,
            value: 'confidence',
          },
          {
            text: 'Lift',
            align: 'center',
            sortable: true,
            value: 'lift',
          },
          {
            text: 'Leverage',
            align: 'center',
            sortable: true,
            value: 'leverage',
          },
          {
            text: 'Conviction',
            align: 'center',
            sortable: true,
            value: 'conviction',
          },
        ],
      };
    }
  };
</script>

<style scoped>

</style>