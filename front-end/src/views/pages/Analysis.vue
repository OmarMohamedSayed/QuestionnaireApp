<template>
    <v-row>
    <v-col 
      cols="12"
    >
      <div>
        <apexchart width="600" type="donut" :options="options" :series="series"></apexchart>
      </div>
    </v-col>
    <v-col 
      cols="12"
    >
      <div class="pa-3 text-center">
        <v-btn
          color="primary"
          class="me-3 mt-2"
          @click='reloadPage'
        >
          تسجيل جديد
        </v-btn>
      </div>
    </v-col>
    </v-row>
  </template>
  
  <script>
  
  export default {
    props: ['analysisData'],
    methods: {
      reloadPage(){
        window.location.reload()
      }
    },
    data () {
        return {
            options: {
              chart: {
                type: 'donut',
                dropShadow: {
                  enabled: true,
                  color: '#111',
                  top: -1,
                  left: 3,
                  blur: 3,
                  opacity: 0.2
                }
              },
              stroke: {
                width: 0,
              },
              plotOptions: {
                pie: {
                  donut: {
                    labels: {
                      show: true,
                      total: {
                        showAlways: true,
                        show: true
                      }
                    }
                  }
                }
              },
              labels: Object.keys(this.analysisData),
              dataLabels: {
                dropShadow: {
                  blur: 3,
                  opacity: 0.8
                }
              },
              fill: {
                type: 'gradient',
              },
              states: {
                hover: {
                  filter: 'none'
                }
              },
              theme: {
                palette: 'palette2'
              },
              responsive: [{
                breakpoint: 480,
                options: {
                  chart: {
                    width: 200
                  },
                  legend: {
                    position: 'bottom'
                  }
                }
              }]
            },
            series:Object.values(this.analysisData),
        }

    },
  }
  </script>
  