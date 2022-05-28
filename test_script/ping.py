import os

def pings(host1, host2):#host1 host2的类型为Host
    host1_lines = host1.cmd("ifconfig|grep 'inet'").split("\r\n")
    host1_line = host1_lines[0].split("inet")
    h1 = host1_line[1].split(" ")[1]
    #h1 = host1.cmd("ifconfig|grep 'inet'")[13:21]
    host2_lines = host2.cmd("ifconfig|grep 'inet'").split("\r\n")
    host2_line = host2_lines[0].split("inet")
    h2 = host2_line[1].split(" ")[1]
    #h2 = host2.cmd("ifconfig|grep 'inet'")[13:21]
    cmd = os.popen("ping -c 5 -a "+ h1 + " " +  h2 + "| grep 'time='")
    lines = cmd.read().split("\x07\n")
    lines.remove('')
    sum = 0
    for line in lines:
        print(line)
        time_ms = line.split("time=")
        time_s = time_ms[1].split(" ")
        time = float(time_s[0])
        sum += time
    print("ave time:" + str(sum/5) + "ms")
