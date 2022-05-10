#!/usr/bin/env python
# 这里的代码是将MiniEdit导出的Python文件基础上做修改
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from bottle import route, run, template, get, post

# 引入bottle,可以简单的提供回应http的api
net = Mininet(topo=None,
              build=False,
              ipBase='10.0.0.0/8')

info('*** Adding controller\n')
c0 = net.addController(name='c0',
                       controller=RemoteController,
                       ip='127.0.0.1',
                       protocol='tcp',
                       port=6633)

# 添加交换机和网络对象
sw = []


# @route可以创建一个默认为get的http接口，在下面定义一个函数即为在得到请求后调用的函数
@route('/api/defaulttopo')
def start_topo():
    # 把默认的各种交换机和拓扑加入并连接
    global c0
    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    sw.append('s1')
    sw.append('s2')
    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    info('*** Add links\n')
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s1, s2)


# 删除主机的接口，用<变量名>即可传参
# 比如/api/deletehost/h1即为删h1
@route('/api/deletehost/<hostname>')
def delete_host(hostname):
    #     net.get可以根据字符串也就是名字获取主机对象
    #     这里做了一个嵌套
    #     下同
    net.delHost(net.get(hostname))


@route('/api/deleteswitch/<switchname>')
# 删除交换机的接口
def delete_switch(switchname):
    net.delSwitch(net.get(switchname))
    sw.remove(switchname)


@route('/api/addlink/<name1>/<name2>')
# 增加链路的接口,增加两个参数并将他们连接
def add_link(name1, name2):
    net.addLink(net.get(name1), net.get(name2))


@route('/api/addhost/<hostname>/<ip>/<dst>')
# 添加主机的接口，并且设置他的ip和默认要连接的交换机（dst）
def add_host(hostname, ip, dst):
    net.addHost(hostname, ip=ip, cls=Host, defaultRoute=None)
    #     添加后做一个连接
    net.addLink(net.get(dst), net.get(hostname))


@route('/api/addswitch/<switchname>')
# 添加交换机的接口,传入交换机名
def add_switch(switchname):
    global c0
    #     把最开始定义的控制器对象，即为c0引进来用
    net.addSwitch(switchname, cls=OVSKernelSwitch)
    sw.append(switchname)


#     把新增的控制器连上c0

@route('/api/dellink/<node1>/<node2>')
def del_link(node1, node2):
    net.delLinkBetween(net.get(node1), net.get(node2))


@route('/api/pingall')
# 这个接口出来的数据似乎只能在终端显示，故不使用
def ping_all():
    net.pingAll()


@route('/api/first_start')
# 第一次启动拓扑的接口
def start_first_net():
    global c0
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()
    # 开控制器
    for i in sw:
        net.get(i).start([c0])
    info('*** Starting network\n')
    net.build()
    #     拓扑建立
    net.pingAll()


#     做一个连接，让交换机下发流表


@route('/api/start')
# 没啥用
def start_net():
    net.start()
    net.pingAll()


@route('/api/stop')
# 废弃
def stop_net():
    for controller in net.controllers:
        controller.stop()
    net.stop()


# run是bottle的运行函数。这里是指定了端口号和运行地址，这里写了个2345，前端也是写了2345
run(host='localhost', port=2345)
