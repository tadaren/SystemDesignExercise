<template lang="pug">
  section.section
    div.columns
      card(title="現在の湿度")
        span.has-text-weight-bold(v-bind:class="{ 'has-text-danger': isDanger }") {{ humid }}%

      card(title="現在の開放限度")
        span.has-text-weight-bold {{ openLimitText }}

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
    let res = await Promise.all([$axios.$get('/api/humid'), $axios.$get('/api/isopen'), $axios.$get('/api/openlimit'), $axios.$get('/api/mode')]);
    let humid = Number.parseFloat(res[0]);
    let isOpen = res[1] == 'True';
    let openLimit = Number.parseInt(res[2]);
    let mode = res[3];

    return {
      humid,
      isOpen,
      openLimit,
      mode,
    }
  },
  watch:{
    mode: function(newValue, oldValue){
      this.$axios.post('/api/mode', newValue);
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
    },
    openLimitText: function(){
      if(this.openLimit == 0){
        return '締め切り';
      }else{
        return this.openLimit + '%';
      }
    }
  },
  mounted: function(){
    setInterval(() => {
      this.$axios.get('/api/humid').then(res => {
        console.log(res);
        this.humid = Number.parseFloat(res.data);
      });
      this.$axios.get('/api/isopen').then(res => {
        console.log(res);
        this.isOpen = res.data == 'True';
      })
    }, 1000);
    setInterval(() => {
      this.$axios.get('/api/openlimit').then(res => {
        console.log(res);
        this.openLimit = Number.parseInt(res.data);
      })
    }, 10000);
  }
}
</script>
