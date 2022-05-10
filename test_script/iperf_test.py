from mininet.net import Mininet

class iperf_test():
    def tcpiperf(self, h1, h2):
        hosts[0] = h1;
        hosts[1] = h2;
        net.iperf(hosts,'TCP',None,None,5,5001)
    def udpiperf(self, h1, h2):
        hosts[0] = h1;
        hosts[1] = h2;
        net.iperf(hosts,'UDP',None,None,5,5001)
