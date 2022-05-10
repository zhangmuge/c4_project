import axios from "axios";
export default {
    install:function (vue)
    {
        var obj=axios.create({
        })
        vue.prototype.$http=obj
    }
}
//创建axios对象并且注册到prototype中使全局都可以访问调用$http来使用axios