<template>
<div class="container-fluid">
  <label for="name">请输入要删除的主机（交换机）名:</label>
  <input type="text" v-model="name1">
  <p></p>
  <label for="name">请输入要与其删除的主机（交换机）名:</label>
  <input type="text" v-model="name2">
  <p></p>
  <button class="btn btn-success" @click="sub">提交</button>
</div>
</template>

<script>
import config from "../config";

export default {
  name: "del_link",
  data(){
    return{
      name1:'',
      name2:''
    }
  },
  methods:{
    sub(){
      this.$http.get(config.Mini_URL+'/dellink/'+this.name1+'/'+this.name2).then(res=>{
        if(res.status===200)
        {
          window.alert('删除成功！')
        }
      }).catch(()=>{
        window.alert('删除失败！请检查输入是否正确')
      })

    }
  }
}
</script>

<style scoped>

</style>