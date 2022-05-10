import Vue from 'vue'
import App from './App.vue'
import axios from "./axios.js";
import router from "./router.js";
import ElementUI from 'element-ui'
import store from './store'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)

Vue.use(axios)
Vue.config.productionTip = false
//使用axios完成rest API需要的http请求
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
