# -*- coding:UTF-8 -*-
# Time          : 2019-12-19 15:53
# Author        : xiexin
# File          : test_login_login.py
# Description   : 

import requests
import unittest
import readConfig
import paramunittest
from common import Log as Log
from common import common
from common import configHttp as ConfigHttp
import json
import aes_com

login_xls = common.get_xls("userCase.xlsx", "login")
localReadConfig = readConfig.ReadConfig()
configHttp = ConfigHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):
    def setParameters(self, case_name, method, url, header, phone, password, result, msg):
        self.case_name = str(case_name)
        self.url = str(url)
        self.header = str(header)
        self.phone = str(phone)
        self.password = str(password)
        self.resultCode = str(result)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.get_url = self.url + '?KEYDATA='
        self.data = {"phoneNo": self.phone, "password": self.password, "phoneInfo": "HUAWEI MLA-AL10",
                     "phoneSn": "4ccc6ab8a9fd2544", "longitude": 106.56358166666665, "latitude": 39.00125,
                     "loginType": 2}
        data = aes_com.encrypt(json.dumps(str(self.data)))
        self.url1 = (self.get_url + data).replace('\n', '').replace('\r', '')
        self.headers = eval(self.header)  # eval将从Excel中读取到的header数据转换成字典类型

    def testlogin(self):
        url = self.url1
        headers = self.headers
        self.res = requests.get(url=url, headers=headers)
        self.result = self.res.json()
        self.assertEqual(self.result['result'], int(self.resultCode))  # 判断返回的状态码是否正确
        self.assertEqual(self.result['msg'], self.msg)  # 判断返回的msg是否和用例一致

    def tearDown(self):
        # print(self.res.status_code)
        print(self.res.text)


if __name__ == '__main__':
    unittest.main()

# @paramunittest.parametrized(*login_xls)
# class Login(unittest.TestCase):
# 	def setParameters(self, case_name, method, phone, password, result, code, msg):
# 		"""
# 		set params
# 		:param case_name:
# 		:param method:
# 		:param token:
# 		:param phone:
# 		:param password:
# 		:param result:
# 		:param code:
# 		:param msg:
# 		:return:
# 		"""
# 		self.case_name = str(case_name)
# 		self.method = str(method)
# 		self.token = str(token)
# 		self.phone = str(phone)
# 		self.password = str(password)
# 		self.result = str(result)
# 		self.code = str(code)
# 		self.msg = str(msg)
# 		self.return_json = None
# 		self.info = None
#
# 	def description(self):
# 		"""
# 		test report description
# 		:return:
# 		"""
#
# 	# self.case_name
#
# 	def setUp(self):
# 		"""
#
# 		:return:
# 		"""
# 		self.log = Log.MyLog.get_log()
# 		self.logger = self.log.get_logger()
# 		print(self.case_name + "测试开始前准备")
#
# 	def testLogin(self):
# 		"""
# 		test body
# 		:return:
# 		"""
# 		# set url
# 		self.url = common.get_url_from_xml('login')
# 		configHttp.set_url(self.url)
# 		print("第一步：设置url  " + self.url)
#
# 		# get visitor token
# 		if self.token == '0':
# 			global token
# 			token = localReadConfig.get_headers("token_v")
# 		elif self.token == '1':
# 			token = None
#
# 		# set headers
# 		# header = {"token": str(token)}
# 		header = {'Charset': 'UTF-8',
#                'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 5.1.1;OPPO R11 Build/FRF91)',
#                'Accept': '*/*', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate',
#                'Host': '61.14.255.62'}
# 		configHttp.set_headers(header)
# 		print(header)
# 		print("第二步：设置header(token等)")
#
# 		# set params
# 		# data = {"phone": self.phone, "password": self.password}
# 		# configHttp.set_data(data)
# 		# print("第三步：设置发送请求的参数")
# 		data = {"phoneNo":self.phone,"password":self.password,"phoneInfo":"google Pixel 2","phoneSn":"14ccc6ab8a9fd431","longitude":101.56358166666665,"latitude":25.001249999999995,"loginType":2}
# 		data = aes_com.encrypt(data)
# 		configHttp.set_data(data)
# 		print(data)
# 		print("第三步：设置发送请求的参数")
#
# 		# test interface
# 		self.return_json = configHttp.get()
# 		method = str(self.return_json.request)[int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
# 		print("第四步：发送请求\n\t\t请求方法：" + method)
#
# 		# check result
# 		self.checkResult()
# 		print("第五步：检查结果")
#
# 	# def tearDown(self):
# 	# 	"""
# 	#
# 	# 	:return:
# 	# 	"""
# 	# 	info = self.info
# 	# 	if info['code'] == 0:
# 	# 		# get uer token
# 	# 		token_u = common.get_value_from_return_json(info, 'member', 'token')
# 	# 		# set user token to config file
# 	# 		localReadConfig.set_headers("TOKEN_U", token_u)
# 	# 	else:
# 	# 		pass
# 	# 	self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])
# 	# 	print("测试结束，输出log完结\n\n")
#
# 	def checkResult(self):
# 		"""
# 		check test result
# 		:return:
# 		"""
# 		self.info = self.return_json.json()
# 		# show return message
# 		common.show_return_msg(self.return_json)
#
# 		if self.result == '0':
# 			phone = common.get_value_from_return_json(self.info, 'member', 'email')
# 			self.assertEqual(self.info['code'], self.code)
# 			self.assertEqual(self.info['msg'], self.msg)
# 			self.assertEqual(phone, self.phone)
#
# 		if self.result == '1':
# 			self.assertEqual(self.info['code'], self.code)
# 			self.assertEqual(self.info['msg'], self.msg)
