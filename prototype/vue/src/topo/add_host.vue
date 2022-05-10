<template>
<div class="container-fluid">
  <label for="name">请输入主机名: </label>
  <input type="text" v-model="hostname">
  <!--  用v-model双向绑定数据-->
  <p></p>
  <label for="name">请输入ip: </label>
  <input type="text" v-model="ip">
  <p></p>
  <label for="name">请输入默认连接的交换机: </label>
  <input type="text" v-model="switch_name">
  <p></p>
  <button class="btn btn-success" @click="sub">提交</button></div>
<!--  这里不用form的submit而是调用自己写的方法去发送请求-->
</template>

<script>
import config from "@/config";
export default {
  name: "add_host",
  data(){
    return{
      hostname:'',
      ip:'',
      switch_name:''
    }
  },
  methods:{
    sub(){
      this.$http.get(config.Mini_URL+'/addhost/'+this.hostname+'/'+this.ip+'/'+this.switch_name).then(res=>{
        //拼接出请求地址
        if(res.status===200)
        {
          window.alert('添加主机'+this.hostname+'成功！')
        }
      }).catch(()=>{
        window.alert('添加失败！请检查输入是否正确')
      })

    }
  }
}
</script>

<style scoped>

</style>