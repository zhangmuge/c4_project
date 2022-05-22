import os

def uipref(h1, h2):
    h2_cmd = os.system("sudo nohup mx " + h2 + " iperf -u -s &")
    h1_cmd = os.popen("sudo mx " + h1 + " iperf -u -c 10.0.0.2 -b 1000M")
    result = h1_cmd.read().split("\n")[10]
    out = round(float(result.split(" ")[7]) * 1.0 / 10, 2)
    plr = result.split(" ")[17]
    print("------------------------------UDP测试----------------------------")
    print("吞吐量:" + str(out) + result.split(" ")[8] + "/sec 带宽:" + result.split(" ")[10] + result.split(" ")[11] + " 时延" + result.split(" ")[14] + result.split(" ")[15] + " 丢包率:" + plr[1:6])
    h1_cmd.close()
