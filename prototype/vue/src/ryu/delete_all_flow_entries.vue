<template>
  <div class="container-fluid">
    <div>
      <table class="table table-striped table-bordered table-hover">
        <!--        bootstrap中的table样式，还分为<thead>定义表头，<tbody>定义表的内容
        table-striped添加斑马条纹样式，table-bordered添加边框,table-hover在鼠标放上去时高亮-->
        <thead>
        <tr>
          <th>
            dpid(点击交换机即可删除)
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="id in dpid" :key="id">
          <!--          用了一个v-for循环去遍历函数获取的dpid并显示在表格内-->
          <a class="link" @click="deleteflow(id)">
            <th>{{ id }}</th>
          </a>
        </tr>
        <tr>
          <th>当前拓扑共有：{{ dpid.length }}台交换机</th>
        </tr>
        </tbody>
      </table>
    </div>
    <button @click="getdpid" >刷新</button>
  </div>

</template>

<script>
import config from "@/config";
export default {
  name: "delete_all_flow_entries",
  data() {
    return {
      dpid: [],
    }
  },
  created() {
    this.getdpid()//created()用于在调用组件时候初始化，这里初始化下面methods里面定义的getdpid函数，作用是在调用时获取所有交换机id
  },
  methods: {
    getdpid() {//使用axios注册的$http来发送get请求，并用变量res接收，赋给数组dpid以便在h5代码里面调用
      //这里调用的是ryu的获取交换机api，完整地址为http://localhost:8080/stats/switches
      this.$http.get(config.Ryu_URL+'/stats/switches').then(res => {
        this.dpid = res.data
      })
    },
    deleteflow(id){
      this.$http.delete(config.Ryu_URL+'/stats/flowentry/clear/'+id).then(res=>
      {
        if(res.status===200)
        {
          window.alert("删除成功！当前交换机流表已清空")
        }
      }).catch(()=>{
        window.alert("删除失败！请检查交换机是否正确！")
      })
    }
  }

}
</script>

<style scoped>
.link{
  /*route-link是渲染为默认a标签，会破坏原来的美观，需要修改*/
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
  cursor: pointer;
}
</style>