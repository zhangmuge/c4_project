<template>
  <div class="container">
    <!--      bootstrap将container类作为容器，即在container内才能起作用-->
    <sdntitle></sdntitle><!--标题组件-->
    <div class="panel panel-warning" v-if="flag">
<!--      使用面板，清晰明了，warning为黄色面板,这里用了v-if控制面板显示-->
      <div class="panel-heading">
<!--        面板头-->
        <h3 class="panel-title">
<!--          面板标题-->
          Mininet控制面板
        </h3>
      </div>
      <div class="panel-body">
<!--        面板主体-->
        <div class="row clearfix">
<!--          行块 清除浮动-->
          <div class="col-md-4 column">
<!--            占用四格的列块-->
            <router-link :to="{name:'default_topo'}" class="btn btn-primary" @click.native="watch_topo">导入默认拓扑</router-link>
<!--            导入默认拓扑的路由，绑定了一个watch_topo方法去发送请求，@click.native可以直接监听vue组件的根元素的原生事件，如果直接用@click不会生效-->
          </div>
          <div class="col-md-4 column">
<!--            以下都是类似结构，不多赘述-->
            <router-link :to="{name:'add_host'}" class="btn btn-primary">增加主机</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'add_switch'}" class="btn btn-primary">添加交换机</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'add_link'}" class="btn btn-primary">添加链路</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'del_link'}" class="btn btn-primary">删除链路</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'del_host'}" class="btn btn-primary">删除主机</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'del_switch'}" class="btn btn-primary">删除交换机</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'update_topo'}" class="btn btn-primary">导入拓扑文件生成拓扑图</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'start_net'}" class="btn btn-success" @click.native="change_flag">建立拓扑</router-link>
<!--            这里绑定一个方法切换面板-->
          </div>
        </div>
      </div>
    </div>
    <div class="panel panel-info" v-else>
<!--      v-else监听flag编辑决定显示什么面板，这里是Ryu面板，先在Mininet面板操作完拓扑才能进来-->
      <div class="panel-heading">
        <h3 class="panel-title">
          Ryu控制面板
        </h3>
      </div>
      <div class="panel-body">
        <div class="row clearfix">
          <div class="col-md-4 column">
            <router-link :to="{name:'watchtopo'}" class="btn btn-primary">查看当前拓扑图</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'watchrouter'}" class="btn btn-primary">查看拓扑中的交换机与流表</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'add_flow'}" class="btn btn-primary">添加流表项</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'add_flow_by_file'}" class="btn btn-primary">以文件形式提交流表项</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'delete_flow_by_id'}" class="btn btn-primary">删除指定交换机的所有流表</router-link>
          </div>
          <div class="col-md-4 column">
            <router-link :to="{name:'default_route'}" class="btn btn-success" @click.native="change_flag">返回
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div class="panel panel-primary">
<!--      路由显示面板-->
      <div class="panel-heading">
        <h3 class="panel-title">操作面板</h3>
      </div>
      <div class="panel-body">
        <router-view></router-view>
<!--        路由显示-->
      </div>
    </div>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'//引入bootstrap3 css框架，本次项目用的样式都来自于此，如果不会用请参考菜鸟教程
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.js'
import sdntitle from "@/components/sdntitle";
import config from "@/config";
//将要用的ryu和mininet请求封装在了config文件里
export default {
  name: 'App',
  components: {
    sdntitle
  },
  data() {
    return {
      flag: true,
      //控制ryu和mininet切换的面板的标记
    }
  },
  methods: {
    change_flag() {
      //控制显示Mininet还是Ryu面板
      if (this.flag == true) {
        this.$http.get(config.Mini_URL + '/first_start').catch(() => {
          window.alert('创建失败！请重启拓扑Python文件')
          //如果创建失败就返回上一级路由
          this.$router.go(-1)
          this.flag=true
        })
      }
      this.flag = !this.flag
    },
    watch_topo() {
      //由于组件会跟着组件一起加载，所以请求方法直接写在首页里面。这样点击按钮的时候就可以同时调用请求方法
      this.$http.get(config.Mini_URL + '/defaulttopo').then(res => {
        if (res.status == 200) {
          this.$store.commit('change_flag', 1)
        //  这里使用store传参给目标路由default_topo决定显示什么页面，成功的时候flag为1，页面显示成功
        }
      }).catch(() => {
        this.$store.commit('change_flag', 2)
        //失败了flag为2，页面显示失败
      })
    },
  }
}
</script>

<style>
.column {
  margin: 0 0 5px 0;
/*  给所有按钮一个间距，看起来比较美观
    否则会挤在一起*/
}
</style>
