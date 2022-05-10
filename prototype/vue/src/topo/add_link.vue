<template>
<div class="container-fluid">
  <label for="name">请输入要连接的主机（交换机）名:</label>
  <input type="text" v-model="name1">
  <p></p>
  <label for="name">请输入要与其连接的主机（交换机）名:</label>
  <input type="text" v-model="name2">
  <p></p>
  <button class="btn btn-success" @click="sub">提交</button>
</div>
</template>

<script>
import config from "@/config";

export default {
  name: "add_link",
  data(){
    return{
      name1:'',
      name2:''
    }
  },
  methods:{
    sub(){
      this.$http.get(config.Mini_URL+'/addlink/'+this.name1+'/'+this.name2).then(res=>{
        if(res.status===200)
        {
          window.alert('添加成功！')
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