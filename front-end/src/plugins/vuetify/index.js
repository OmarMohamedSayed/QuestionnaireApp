import Vue from 'vue'
import Vuetify from 'vuetify/lib/framework'
import preset from './default-preset/preset'
import VueApexCharts from 'vue-apexcharts'

Vue.use(Vuetify)
Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)

export default new Vuetify({
  preset,
  icons: {
    iconfont: 'mdiSvg',
  },
  theme: {
    options: {
      customProperties: true,
      variations: false,
    },
  },
})
