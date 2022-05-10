module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8080/',
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
            '/topo': {
                target: 'http://localhost:2345/api/',
                //mininet的bottle地址端口，这里的2345端口是自定义的
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/topo': ''
                }
            }
        }
    }
}
//使用代理去解决跨域问题