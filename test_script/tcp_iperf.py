import os

def tipref(h1, h2):
    h2_cmd = os.system("sudo nohup mx " + h2 + " iperf -s &")
    h1_cmd = os.popen("sudo mx " + h1 + " iperf -c 10.0.0.2")
    result = h1_cmd.read().split("\n")[6]
    throughput = round(float(result.split(" ")[7]) * 1.0 / 10, 2)
    print("---------------TCP测试---------------")
    print("吞吐量:" + str(throughput) + result.split(" ")[8] + " 带宽:" + result.split(" ")[10] + result.split(" ")[11])
    h1_cmd.close()
