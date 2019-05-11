<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-card flat>
    <v-card-title>
      Nutrition
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
        <td>{{ props.item.Name_Of_Community }}</td>
        <td class="text-xs-right">{{ props.item.FAMobility }}</td>
        <td class="text-xs-right">{{ props.item.SAEconomic }}</td>
<!--        <td class="text-xs-right">{{ props.item.carbs }}</td>-->
<!--        <td class="text-xs-right">{{ props.item.protein }}</td>-->
<!--        <td class="text-xs-right">{{ props.item.iron }}</td>-->
      </template>
      <template v-slot:no-results>
        <v-alert :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </template>
    </v-data-table>
  </v-card>
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
          value: 'name',
        },
        { text: 'FAMobility', value: 'FAMobility' },
        { text: 'SAEconomic', value: 'SAEconomic' },
        // { text: 'SARoadsTrans', value: '' },
        // { text: 'TArtificialIntelligence', value: '' },
        // { text: 'TAutonomousVehicles', value: '' },
        // { text: 'TGeospatial', value: '' },
        // { text: 'TIoT', value: '' },
        // { text: 'TSensors', value: '' },
        // { text: 'Calories', value: 'calories' },
        // { text: 'Fat (g)', value: 'fat' },
      ],
      desserts: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: '1%',
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: '1%',
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: '7%',
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: '8%',
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: '16%',
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: '0%',
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: '2%',
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: '45%',
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: '22%',
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: '6%',
        },
      ],
      campaigns: [],
    };
  },
  created() {
    const { apiEndpoint } = this;
    this.axios.get(`${apiEndpoint}/campaigns/`).then((response) => {
      this.$set(this, 'campaigns', response.data.campaigns);
      console.log(response.data.campaigns);
    });
  },
};
</script>

<style scoped>

</style>
