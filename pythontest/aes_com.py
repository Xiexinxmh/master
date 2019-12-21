# -*- coding:utf-8 -*-
# Time          : 2019-11-20 17:55
# Author        : xiexin
# File          : aes_com.py
# Description   : 加解密调用的入口

import subprocess
import chardet


key = "893261785611546766@**xmenWYAX&hu"

def encrypt(data):
    command = "java -jar F:/python/AWL/testFile/encrytor.jar"
    arg0 = data
    arg1 = key
    # cmd = [command, arg0]
    cmd = [command, arg0, arg1]  # 如需加key，需要传入arg1
    new_cmd = " ".join(cmd)
    stdout, stderr = subprocess.Popen(new_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    encoding = chardet.detect(stdout)["encoding"]
    en_result = stdout.decode(encoding)
    return en_result

def decrypt(data):
    command = "java -jar F:/python/AWL/testFile/decryptor.jar"
    arg0 = data
    arg1 = key
    # cmd = [command, arg0]
    cmd = [command, arg0, arg1]  # 如需加key，需要传入arg1
    new_cmd = " ".join(cmd)
    stdout, stderr = subprocess.Popen(new_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    encoding = chardet.detect(stdout)["encoding"]
    de_result = stdout.decode(encoding)
    return de_result


