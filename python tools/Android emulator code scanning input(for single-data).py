#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/18 10:04
# @Version : Python 3.7.1

import os
import re


class Infinit:
    def __iter__(self):
        return self

    def __next__(self):
        return None


def connect():
    # 通过任务管理器查看PID，再用cmd查找PID对应的端口
    os.popen('adb connect 127.0.0.1:62001')
    out = os.popen('adb devices').read()
    global devices_list
    devices_list = re.sub('\tdevice', '', out[25:]).strip().split('\n')
    print('设备已连接:%s' % devices_list)


def Input(Num):
    if len(devices_list) > 1:
        os.system("adb -s 127.0.0.1:62001 shell input text \"" + Num + "\"")
        os.system("adb -s 127.0.0.1:62001 shell input keyevent 66")
    else:
        os.system("adb shell input text \"" + Num + "\"")
        os.system("adb shell input keyevent 66")


if __name__ == '__main__':
    connect()
    for i in Infinit():
        Num = input('请输入内容：')
        Input(Num)
