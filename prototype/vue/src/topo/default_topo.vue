<template>
<!--  这里只写了几个状态显示的div,通过store传入的数据去改变状态，请求方法写在了App.vue-->
  <div class="container-fluid">
    <div v-if="this.$store.getters.flag_value==0">
      <h3>加载中，请稍等..</h3>
    </div>
    <div v-else-if="this.$store.getters.flag_value==1">
      <h3>默认拓扑导入成功！拓扑参考图：</h3>
      <img src="../assets/mininet.png">
<!--      放个图-->
    </div>
    <div v-else>
      <h3>加载失败！请检查是否已有拓扑！</h3>
    </div>
  </div>
</template>

<script>

export default {
  name: "default_topo",
}
</script>

<style scoped>

</style>