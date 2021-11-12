<template>
  <v-card id="account-setting-card">
    <v-progress-linear value="100"></v-progress-linear>
    <!-- stepper -->
    <v-stepper v-model="e1">
      <v-stepper-header>
        <v-stepper-step
          :complete="e1 > 1"
          step="1"
        >
          البيانات
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
          :complete="e1 > 2"
          step="2"
        >
          الأسئلة
        </v-stepper-step>

        <v-divider></v-divider> -->

        <v-stepper-step step="3">
          النتائج
        </v-stepper-step>
      </v-stepper-header>


    <!-- tabs item -->
    <v-stepper-items>
      <v-stepper-content step="1">
        <account-settings-account @clicked="StepperChange"></account-settings-account>
      </v-stepper-content>

      <v-stepper-content step="2">
        <random-questions @clicked="StepperChange" @analysis="getCounter"></random-questions>
      </v-stepper-content>
      <v-stepper-content step="3">
        <analysis @clicked="StepperChange" v-if="loaded" :analysisData="analysisData"></analysis>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
  </v-card> 
</template>

<script>
import { mdiAccountOutline, mdiLockOpenOutline, mdiInformationOutline } from '@mdi/js'
import { ref } from '@vue/composition-api'

// demos
import AccountSettingsAccount from './AccountSettingsAccount.vue'
import RandomQuestions from './RandomQuestions.vue'
import Analysis from './Analysis.vue'
export default {
  components: {
    AccountSettingsAccount,
    RandomQuestions,
    Analysis,
  },
  data () {
      return {
        e1: 1,
        analysisData:[],
        loaded:false,
      }
    },
  methods: {
      StepperChange (event) {
        this.e1 = event
      },
      async getCounter (event) {
        this.analysisData = await this.$store.dispatch("answerscounter",event)
        if(this.analysisData !=[])
        {
          this.loaded=true
        }
        else{
          this.loaded=false
        }
      }
    },
  setup() {
    
    return {
      icons: {
        mdiAccountOutline,
        mdiLockOpenOutline,
        mdiInformationOutline,
      },
    }
  },
}
</script>
