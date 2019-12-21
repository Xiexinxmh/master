#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/26 17:04
# @Version : Python 3.7.1

import requests
import unittest


class GetSessionIdKeno(unittest.TestCase):
	def setUp(self):
		self.url = 'http://61.14.255.35:8080/LYMS/api/platform/getSessionId'
		self.headers = {'Host': '61.14.255.35:8080', 'Proxy-Connection': 'keep-alive', 'Content-Length': '118',
		                'Accept': 'application/json, text/plain, */*', 'Origin': 'file://',
		                'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36',
		                'Content-Type': 'application/json;charset=UTF-8', 'Accept-Encoding': 'gzip, deflate',
		                'Accept-Language': 'zh-CN,en-US;q=0.8', 'X-Requested-With': 'com.xmen.asianlottery.v1'}
		# 当前为13168320227这个账号的userid数据。sessionid是变化的，所以暂时跑不通，需要从登陆成功响应中提取token作为sessionid。
		self.payload = {
			"data": {"userid": "5cbfc897ef2043c3b4e9e3fe7cbf31d0", "sessionid": "08142fde-2a54-4931-a6fb-fa96831d88d0"},
			"keydata": ""}

	def testgetsessionidkeno(self):
		url = self.url
		headers = self.headers
		payload = self.payload
		self.res = requests.post(url, json=payload, headers=headers)
		result = self.res.json()
		self.assertEqual(result['result'], 101)
		self.assertEqual(result['msg'], '操作成功')

	def tearDown(self):
		print(self.res.status_code)
		print(self.res.text)


if __name__ == '__main__':
	unittest.main()
