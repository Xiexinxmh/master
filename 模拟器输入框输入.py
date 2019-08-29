#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/30 11:10
# @Version : Python 3.7.1

import sys
import os
import time

os.system("adb connect 127.0.0.1:62001")
result = []
with open('accounts.txt', 'r') as f:
	for line in f:
		# result.append(list(line.strip('\n').split(',')))
		result.append(line.strip('\n').split(',')[0])
		# print(line.strip('\n').split(',')[0])
# # print(len(result))
for i in range(150):
	print(result[i])
	idd = result[i]
	# idd = "A00021800200031311000000152129"
	cod = "adb -s 127.0.0.1:62001 shell input text \"" + idd + "\""
	os.system(cod)
	time.sleep(1)
	os.system("adb -s 127.0.0.1:62001 shell input keyevent 66")

