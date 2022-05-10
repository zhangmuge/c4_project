<template>
<div class="container-fluid">
  <div class="form-group">
    <label for="name">添加流表项</label>
    <textarea class="form-control" placeholder="请以JSON格式输入流表" rows="10" v-model="flow"></textarea>
    <button class="btn btn-default" @click="submit_flow">提交</button>
  </div>
</div>
</template>

<script>
import config from "@/config";
export default {
  name: "add_flow",
  data(){
    return{
      flow:''
    }
  },
  methods:{
    submit_flow(){
      this.$http.post(config.Ryu_URL+'/stats/flowentry/add',this.flow).then(res=>{
        if(res.status===200)
        {
          window.alert("流表添加成功！")
        }
      }).catch(()=>{
        window.alert("添加失败！请检查交换机id，格式等是否正确！")
      })
    }
  }
}
</script>

<style scoped>

</style>