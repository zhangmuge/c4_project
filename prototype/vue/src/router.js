import Vue from "vue";
import VueRouter from "vue-router";
import watchtopo from "@/ryu/watchtopo";
import watchrouter from "@/ryu/watchrouter";
import watchflow from "@/ryu/watchflow";
import add_flow from "@/ryu/add_flow";
import add_flow_by_file from "@/ryu/add_flow_by_file";
import delete_all_flow_entries from "@/ryu/delete_all_flow_entries";
import add_host from "@/topo/add_host";
import add_link from "@/topo/add_link";
import add_switch from "@/topo/add_switch";
import del_host from "@/topo/del_host";
import del_switch from "@/topo/del_switch";
import start_net from "@/topo/start_net";
import update_topo from "@/topo/update_topo";
import default_topo from '@/topo/default_topo'
import default_route from "@/components/default_route";
import del_link from "./topo/del_link";
Vue.use(VueRouter)
//注册路由
var router = new VueRouter({
    routes: [
        {
            path: '/ryu/watchtopo',
            component: watchtopo,
            name: 'watchtopo',
        },
        {
            path: '/ryu/watchrouter',
            component: watchrouter,
            name: 'watchrouter',
        },
        {
            path: '/ryu/watchrouter/flow/:id',
            component: watchflow,
            props: true,
            name: 'watchflow'
        },
        {
            path: '/ryu/add_flow',
            component: add_flow,
            name: 'add_flow'
        },
        {
            path: '/ryu/add_flow_by_file',
            component: add_flow_by_file,
            name: 'add_flow_by_file'
        },
        {
            path: '/ryu/delete_flow_by_id',
            component: delete_all_flow_entries,
            name: 'delete_flow_by_id'
        },
        {
            path: '/mininet/add_host',
            component: add_host,
            name: 'add_host'
        },
        {
            path: '/mininet/add_link',
            component: add_link,
            name: 'add_link'
        },
        {
            path: '/mininet/add_switch',
            component: add_switch,
            name: 'add_switch'
        },
        {
            path: '/mininet/del_host',
            component: del_host,
            name:'del_host'
        },
        {
            path:'/mininet/del_switch',
            component:del_switch,
            name:'del_switch'
        },
        {
            path:'/mininet/start_net',
            component:start_net,
            name:'start_net'
        },
        {
            path:'/mininet/update_topo',
            component:update_topo,
            name:'update_topo'
        },
        {
            path:'/mininet/default_topo',
            component:default_topo,
            name:'default_topo'
        },
        {
            path:'/',
            component:default_route,
            name:'default_route'
        },
        {
            path:'/mininet/del_link',
            component:del_link,
            name:'del_link'
        }
    ],
    linkActiveClass: 'active'
//    用了bootstrap的激活样式，不用特地写css
})
export default router