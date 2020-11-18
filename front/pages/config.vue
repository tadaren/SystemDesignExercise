<template lang="pug">
  section.section
    div.columns(to="/config")
      card(title="開放限度")
        b-select(v-model="selectedLevel")
          option(v-for="level in limitLevel", :value=level, :key=level) {{ level }}

    .is-flex.is-justify-content-space-between
      b-button(tag="nuxt-link" to="/") 戻る
      b-button(v-on:click="apply") 適用
</template>

<script>
import Card from '~/components/Card'

export default {
  name: 'Config',

  components: {
    Card,
  },
  methods: {
    apply: function(){
      let level = this.selectedLevel.slice(0, -1);
      if(this.selectedLevel === '締め切り'){
        level = '0'
      }
      this.$axios.post('/api/openlimit', level);
    }
  },
  data(){
    return {
      limitLevel: [
        '締め切り',
        '10%',
        '20%',
        '30%',
        '40%',
        '50%',
        '60%',
        '70%',
        '80%',
        '90%',
        '100%'
      ],
    }
  },
  async asyncData({ $axios }){
    let data = await $axios.$get('/api/openlimit');
    let limitLevel = data+'%'
    if(data === '0'){
      limitLevel = '締め切り'
    }
    return {
      limit: data,
      selectedLevel: limitLevel,
    }
  }
}
</script>
