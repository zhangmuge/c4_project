<template>
  <div class="container-fluid tab">
    <div class="panel panel-info">
      <div class="panel-heading">
        <div class="panel-title">
          <h4>请上传JSON文件</h4>
        </div>
      </div>
      <div class="panel-body">
      <el-upload action="/" accept=".json" :on-change="submitflow"></el-upload>
    </div>
    <div class="panel-footer">
      <button @click="sub" class="btn btn-success ">提交</button>
    </div>
    </div>

  </div>
</template>
<script>
import config from "@/config";
export default {
  name:'add_flow_by_file',
  data(){
    return{
      flowInfo:"",
    }
  },
  methods:{
    submitflow(file){
      let reader=new FileReader()
      reader.readAsText(file.raw,"UTF-8")
      if(typeof FileReader==="undefined")
      {
        alert("浏览器不支持上传文件")
        return
      }
      reader.onload=e=>{
        this.flowInfo=e.target.result
      }
    },
    sub(){
      this.$http.post(config.Ryu_URL+'/stats/flowentry/add', this.flowInfo).then(res=>{
        if(res.status===200)
        {
          window.alert("流表添加成功！")
        }
      }).catch(()=>{
        window.alert("添加失败！请检查交换机id，格式等是否正确！")
      })
      // window.console.log(this.flowInfo)
    }
  }
}
</script>

<style>

</style>