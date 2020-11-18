<template lang="pug">
  section.section
    div.columns
      card(title="現在の湿度")
        span.has-text-weight-bold(v-bind:class="{ 'has-text-danger': isDanger }") {{ humid }}%

      card(title="現在の開放限度")
        span.has-text-weight-bold {{ openLimit }}%

      card(title="現在の状態")
        span.has-text-weight-bold {{ open }}
    
    b-field(position="is-centered")
      b-radio-button(v-model="mode", native-value="open", type="is-success")
        span 開放
      b-radio-button(v-model="mode", native-value="auto")
        span 自動
      b-radio-button(v-model="mode", native-value="close", type="is-danger")
        span 閉鎖

    b-button(tag="nuxt-link" to="/config") 設定
</template>

<script>
import Card from '~/components/Card'

export default {
  name: 'Home',

  components: {
    Card,
  },
  async asyncData({ $axios }){
    let res = await Promise.all([$axios.$get('/api/humid'), $axios.$get('/api/isopen'), $axios.$get('/api/openlimit')]);
    let humid = Number.parseFloat(res[0]);
    let isOpen = res[1] == 'True';
    let openLimit = Number.parseInt(res[2]);

    return {
      humid,
      isOpen,
      openLimit,
    }
  },
  watch:{
    mode: function(oldValue, newValue){
      // TODO 
    }
  },
  computed: {
    open: function(){
      if(this.isOpen){
        return 'OPEN';
      }else{
        return 'CLOSE';
      }
    },
    isDanger: function(){
      return this.humid <= 30.0
    }
  },
  data(){
    return {
      mode: 'auto'
    }
  }
}
</script>
