import Vue from "vue";
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        //store的数据，这里放一个改变default_topo显示状态的flag
        topo_flag: 0
    },
    mutations: {
        //提交更改的方法，用this.$store.commit调用
        change_flag(state, n) {
            state.topo_flag = n
        }
    },
    //获取里面的数据，用this.$store.getters调用
    getters:{
        flag_value(state){
            //直接返回flag的值
            return state.topo_flag
        }
    }
})