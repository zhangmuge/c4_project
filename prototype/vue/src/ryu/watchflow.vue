<template>
  <div class="container-fluid">
    <h4>dpid:{{id}}中有{{flowtable.length}}条流表</h4>
    <div v-for="(item,index) in flowtable" :key="index">
<!--      v-for需要一个key，由于流表项没有具体的id,偷懒用index，即索引值-->
      <table class="table table-striped table-bordered table-hover">
        <!--        bootstrap中的table样式，还分为<thead>定义表头，<tbody>定义表的内容
table-striped添加斑马条纹样式，table-bordered添加边框,table-hover在鼠标放上去时高亮-->
        <thead>
        <tr>
          <th>
            第{{index}}条流表
          </th>
        </tr>
        </thead>
        <tbody>
          {{item}}
<!--        这里本来是想做一个表格细化分类，而不是直接将json打印出来，但是具体实现还需要构思，比较麻烦，先放在这里做一个TODO
            设想是可以点击按钮切换表格或者JSON格式-->
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import config from "@/config";
export default {
  name: "watchflow",
  props:['id'],//props用于接受传入的id参数
  data(){
    return{
      flowtable:[]
    }
  },
  created() {
    this.getflow()
  },
  methods:{
    getflow(){////使用axios注册的$http来发送get请求，并用变量res接收，获取传入的交换机id的所有流表
      //这里调用的是ryu的获取特定交换机的流表的api，完整地址为http://localhost:8080/stats/flow/id
      this.$http.get(config.Ryu_URL+'/stats/flow/'+this.id).then(res=>{//利用了字符串拼接把id拼进url
        this.flowtable=res.data[Object.keys(res.data)[0]]//拿取JSON里面data对象的第一个元素
      })
    }

  }
}
</script>

<style scoped>

</style>