<template>
<div class="container">
  <div class="row clearfix">
    <div class="col-md-12 column">
<!--      行数为12行，即为占用一整行-->
      <h3 class="text-center">
        欢迎使用SDN拓扑管理系统
        <small>基于Mininet和Ryu控制器</small>
      </h3>
    </div>
</div>
</div>
</template>

<script>
export default {
  name: "sdntitle"
}
</script>

<style scoped>
.container{
  margin-bottom: 25px;
  /*让标题离下面远一点*/
}
</style>