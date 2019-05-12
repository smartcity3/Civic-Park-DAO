<template>
    <v-container>
        <v-layout
                text-xs-center
                wrap
        >
            <v-card dark raised>
                <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                >
                    <v-layout row>
                        <v-text-field class="mx-3"
                                      v-model="name"
                                      :counter="10"
                                      :rules="nameRules"
                                      label="Name"
                                      required

                        ></v-text-field>

                        <v-text-field class="mx-3"
                                      v-model="owner"
                                      :rules="ownerRules"
                                      label="Owner"
                                      required
                        ></v-text-field>
                    </v-layout>

                    <v-layout row>
                        <v-text-field class="mx-3"
                                      v-model="safety"
                                      :rules="safetyRules"
                                      label="Safety"
                                      required
                        ></v-text-field>

                        <v-text-field class="mx-3"
                                      v-model="mobility"
                                      :rules="mobilityRules"
                                      label="Mobility"
                                      required
                        ></v-text-field>
                    </v-layout>

                    <v-layout row>
                        <v-text-field class="mx-3"
                                      v-model="economy"
                                      :rules="economyRules"
                                      label="Economy"
                                      required
                        ></v-text-field>

                        <v-text-field class="mx-3"
                                      v-model="roadtrans"
                                      :rules="roadTransRules"
                                      label="Road Trans"
                                      required
                        ></v-text-field>
                    </v-layout>

                    <v-layout row>
                        <v-text-field class="mx-3"
                                      v-model="artificialintelligence"
                                      :rules="artificialIntelligenceRules"
                                      label="Artificial Intelligence"
                                      required
                        ></v-text-field>

                        <v-text-field class="mx-3"
                                      v-model="autonomousvehicles"
                                      :rules="autonomousVehiclesRules"
                                      label="Autonomous Vehicles"
                                      required
                        ></v-text-field>
                    </v-layout>

                    <v-layout row>
                        <v-text-field class="mx-3"
                                      v-model="iot"
                                      :rules="iotRules"
                                      label="IoT"
                                      required
                        ></v-text-field>

                        <v-text-field class="mx-3"
                                      v-model="sensors"
                                      :rules="sensorsRules"
                                      label="Sensors"
                                      required
                        ></v-text-field>
                    </v-layout>


                    <v-btn
                            round
                            class="text-none"
                            :disabled="!valid"
                            color="success"
                            @click="validate"
                    >
                        Validate
                    </v-btn>

                    <v-btn
                            round
                            class="text-none"
                            color="error"
                            @click="reset"
                    >
                        Reset Form
                    </v-btn>

                    <v-btn
                            round
                            color="blue"
                            class="text-none"
                            @click="createCampaign"
                    >
                        Confirm
                    </v-btn>
                </v-form>
            </v-card>

        </v-layout>
    </v-container>
</template>

<script>
    export default {
        name: "CreateCampaign",
        data: () => ({
            valid: true,
            name: '',
            nameRules: [
                v => !!v || 'Name is required',
            ],
            owner: '',
            ownerRules: [
                v => !!v || 'Owner is required',
            ],
            mobility: '',
            mobilityRules: [
                v => !!v || 'Mobility is required',
            ],
            economy: '',
            economyRules: [
                v => !!v || 'Economy is required',
            ],
            roadtrans: '',
            roadTransRules: [
                v => !!v || 'Road Trans is required',
            ],
            artificialintelligence: '',
            artificialIntelligenceRules: [
                v => !!v || 'Artificial Intelligence is required',
            ],
            autonomousvehicles: '',
            autonomousVehiclesRules: [
                v => !!v || 'Autonomous Vehicles is required',
            ],
            iot: '',
            iotRules: [
                v => !!v || 'IoT is required',
            ],
            sensors: '',
            sensorsRules: [
                v => !!v || 'Sensors is required',
            ],
            safety: '',
            safetyRules: [
                v => !!v || 'Safety is required',
            ],
        }),

        methods: {
            validate() {
                if (this.$refs.form.validate()) {
                    this.snackbar = true;
                }
            },
            reset() {
                this.$refs.form.reset();
            },
            resetValidation() {
                this.$refs.form.resetValidation();
            },
            createCampaign() {
                let postData = {
                    "campaignId": Math.floor(Math.random() * Math.floor(100)),
                    "campaignName": this.name,
                    "Mobility": parseInt(this.mobility),
                    "Safety": parseInt(this.safety),
                    "Economy": parseInt(this.economy),
                    "RoadTrans": parseInt(this.roadtrans),
                    "ArtificialIntelligence": parseInt(this.artificialintelligence),
                    "AutonomousVehicles": parseInt(this.autonomousvehicles),
                    "IoT": parseInt(this.iot),
                    "Sensors": this.sensors,
                    "owner": this.owner
                };
                this.axios.post('http://localhost:3000/api/Campaign', postData)
                    .then(function (response) {
                        alert('Campaign created!');
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
        }
    };
</script>

<style scoped>

</style>