#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import optparse
from threading import Thread

#执行成功则输出密码
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode('ascii'))
        print("[+] Found password '" + password + "'")
    except:
        pass


#分别设置zip文件与字典的参数输入
def main():
    parser = optparse.OptionParser("usage %prog "+\
      "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',\
      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

	#多线程处理
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()
