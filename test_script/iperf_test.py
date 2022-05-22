from mininet.net import Mininet
import topo

class iperftest(object):
    hosts = []
    def __init__(self, h1, h2):
        self.hosts.append(h1)
        self.hosts.append(h2)
    def tcpiperf(self):
        topo.net.iperf(self.hosts,'TCP',None,None,5,5001)
    def udpiperf(self):
        topo.net.iperf(self.hosts,'UDP','1000M',None,5,5001)
