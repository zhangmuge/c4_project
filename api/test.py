import bottle
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import *
from subprocess import call
import os
from bottle import route, run, template, get, post, HTTPResponse, request, response, hook

net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8', link=TCLink)
ryu = net.addController(name='ryu', controller=RemoteController, ip='127.0.0.1', protocol='tcp', port=6633)

switchs = []
hosts = []

headers = {'Content-type': 'application/json'}


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@route('/switch/add/<switch>')
def add_switch(switch):
    if switch in switchs:
        return HTTPResponse(status=400)
    try:
        net.addSwitch(name=switch, cls=OVSKernelSwitch)
        switchs.append(switch)
    except Exception as e:
        return HTTPResponse(status=500, headers=headers)
    return HTTPResponse(status=200, headers=headers)


@route('/switch/delete/<switch>')
def delete_switch(switch):
    if switch not in switchs:
        return HTTPResponse(status=400)
    try:
        net.delSwitch(net.get(switch))
        switchs.remove(switch)
    except Exception as e:
        return HTTPResponse(status=500)
    return HTTPResponse(status=200)


@route('/host/add/<hostname>/<ipaddress>')
def add_host(hostname, ipaddress):
    if hostname in hosts:
        return HTTPResponse(status=400)
    try:
        h = net.addHost(hostname, cls=Host, ip=ipaddress)
        hosts.append(hostname)
    except Exception as e:
        return HTTPResponse(status=500)
    return HTTPResponse(status=200)


@route('/host/delete/<hostname>')
def del_host(hostname):
    if hostname not in hosts:
        return HTTPResponse(status=400)
    try:
        net.delHost(net.get(hostname))
        hosts.remove(hostname)
    except Exception as e:
        return HTTPResponse(status=500)
    return HTTPResponse(status=200)


@route('/link/add/', method='POST')
def add_link():
    data = request.forms
    print(data)
    node1 = data['node1']
    node2 = data['node2']
    try:
        bw = int(data['bw'])
    except Exception as e:
        bw = 0
    try:
        delay = data['delay']
    except Exception as e:
        delay = None
    try:
        loss = int(data['loss'])
    except Exception as e:
        loss = 0
    try:
        net.addLink(node1=node1, node2=node2, bw=bw, delay=delay, loss=loss, use_htb=True)
    except Exception as e:
        return HTTPResponse(status=400)
    return HTTPResponse(status=200)


@route('/link/delete/<node1>/<node2>')
def del_link(node1, node2):
    try:
        net.delLinkBetween(node1, node2)
    except Exception as e:
        return HTTPResponse(status=400)
    return HTTPResponse(status=200)


@route('/start')
def start_net():
    ryu.start()
    for i in switchs:
        net.get(i).start([ryu])
    net.build()
    net.pingAll()


@route('/stop')
def stop_net():
    ryu.stop()
    net.stop()
    os.system("sudo mn -c")


@route('/host/setting')
def set_host(hostname):
    return -1


@route('/link/setting/<node1>/<node2>')
def set_link(node1, node2):
    link = net.linksBetween(node1=net.get(node1), node2=net.get(node2))
    link = TCLink(link[0])


@route('/test')
def test():
    add_switch('s1')
    add_host('h1', '10.0.0.1')


if __name__ == '__main__':
    os.system("sudo mn -c")

    run(host='localhost', port=2345)
