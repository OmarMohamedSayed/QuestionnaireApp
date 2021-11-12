<template>
  <component :is="resolveLayout">
    <router-view></router-view>
  </component>
</template>

<script>
import { computed } from '@vue/composition-api'
import { useRouter } from '@/utils'
import LayoutContent from '@/layouts/Content.vue'

export default {
  components: {
    LayoutContent,
  },
  setup() {
    const { route } = useRouter()

    const resolveLayout = computed(() => {
      if (route.value.name === null) return null
      return 'layout-content'
    })

    return {
      resolveLayout,
    }
  },
}
</script>
