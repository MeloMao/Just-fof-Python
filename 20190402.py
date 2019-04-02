# -*- coding: UTF-8 -*-

import socket
import time


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('%d端口开放' % tgtPort)
        connSkt.close()
    except:
        print('%d端口关闭' % tgtPort)


def portScan(tgtHost, tgtPorts, speed):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("无法解析的主机名" % tgtHost)
        return
    print('\n扫描的主机IP是: ' + tgtIP)
    socket.setdefaulttimeout(speed)
    for tgtPort in tgtPorts:
        print('正在扫描的端口：' + str(tgtPort))
        time.sleep(speed)
        connScan(tgtHost, int(tgtPort))


def main():
    name = input("请输入要扫描的目标主机:")
    chose1 = int(input("是否扫描默认端口?是请输入1，需要自定义端口请输入2，自定义扫描某范围内所有端口请输入3:"))
    chose2 = int(input("是否需要自定义扫描速率（默认为0.5秒/次）？不需要请输入1，需要输入2："))
    if (chose2 == 2):
        speed = float(input("请输入扫描速率（秒/次）："))
    else:
        speed = 0.5
    if (chose1 == 2):
        c = input("请输入需要扫描的端口（用英文逗号隔开）：")
        d = eval(c)
        print("正在扫描自定义端口...")
        portScan(name, d, speed)
    elif (chose1 == 3):
        d = int(input("请输入范围扫描起始端口："))
        e = int(input("请输入范围扫描结束端口："))
        f = []
        for i in range(d, e + 1):
            f.append(i)
        portScan(name, f, speed)
    else:
        print("正在扫描默认端口...")
        portScan(name, [80, 443, 3389, 1433, 23, 445], speed)

main()