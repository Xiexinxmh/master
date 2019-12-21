#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/10 11:00
# @Version : Python 3.7.1

import requests
import unittest
from common import Log as Log
import json
import aes_com

class Login(unittest.TestCase):
    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.get_url = 'http://61.14.255.62/api/login_login?KEYDATA='
        self.data = '{"phoneNo":"13168320227","password":"670b14728ad9902aecba32e22fa4f6bd","phoneInfo":"HUAWEI MLA-AL10","phoneSn":"4ccc6ab8a9fd2544","longitude":106.56358166666665,"latitude":39.00125,"loginType":2}'
        print(self.data)
        data = json.dumps(self.data)
        data1 = aes_com.encrypt(data)
        self.url1 = (self.get_url + data1).replace('\n', '').replace('\r', '')
        self.headers = {'Charset': 'UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 5.1.1;OPPO R11 Build/FRF91)',
                        'Accept': '*/*', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate',
                        'Host': '61.14.255.62'}

    def testlogin(self):
        url = self.url1
        headers = self.headers
        self.res = requests.get(url=url, headers=headers)
        self.result = self.res.json()
        self.assertEqual(self.result['result'], 101)
        self.assertEqual(self.result['msg'], '登录成功')

    def tearDown(self):
        print(self.res.status_code)
        print(self.res.text)


if __name__ == '__main__':
    unittest.main()
