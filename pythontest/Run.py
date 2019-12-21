#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/22 15:27
# @Version : Python 3.7.1

import unittest
import os
import HTMLTestRunner
from common.Log import MyLog as Log
import readConfig as readConfig
from common.configEmail import MyEmail

localReadConfig = readConfig.ReadConfig()


class AllTest:
	def __init__(self):
		global log, logger, resultPath, on_off
		log = Log.get_log()
		logger = log.get_logger()
		resultPath = log.get_report_path()
		on_off = localReadConfig.get_email('on_off')
		self.caseListFile = os.path.join(readConfig.proDir, 'caselist.txt')
		self.caseFile = os.path.join(readConfig.proDir, 'testCase')
		self.caseList = []
		self.email = MyEmail.get_email()

	def set_case_list(self):
		fb = open(self.caseListFile)
		for value in fb.readlines():
			data = str(value)
			if data != '' and not data.startswith('#'):
				self.caseList.append(data.replace('\n', ''))
		fb.close()

	def set_case_suite(self):
		self.set_case_list()
		test_suite = unittest.TestSuite()
		suite_module = []

		for case in self.caseList:
			case_name = case.split('/')[-1]
			print(case_name + '.py')
			discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
			suite_module.append(discover)

		if len(suite_module) > 0:

			for suite in suite_module:
				for test_name in suite:
					test_suite.addTest(test_name)
		else:
			return None

		return test_suite

	def run(self):
		try:
			suit = self.set_case_suite()
			if suit is not None:
				logger.info("********测试开始********")
				global fp
				fp = open(resultPath, 'wb')
				runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
				runner.run(suit)
			else:
				logger.info("无用例执行.")
		except Exception as ex:
			logger.error(str(ex))
		finally:
			logger.info("*********测试结束*********")
			fp.close()
			# send test report by email
			if on_off == 'on':
				self.email.send_email()
				logger.info("邮件已发送.")
			elif on_off == 'off':
				logger.info("邮件未发送.")
			else:
				logger.info("未知状态.")


if __name__ == '__main__':
	obj = AllTest()
	obj.run()

# def send_report(testreport):
# 	result_dir = '.\\report'
# 	lists = os.listdir(result_dir)
# 	lists.sort(key=lambda fn: os.path.getmtime(testreport + fn))
# 	file_new = os.path.join(result_dir, lists[-1])
# 	print(file_new)  # 打印出最新的html测试报告名称
#
#
# def creatsuite():
# 	testunit = unittest.TestSuite()
# 	test_dir = '.\\testCase'  # 指定测试用例为当前文件夹下的testCase目录
# 	discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# 	for test_case in discover:
# 		print(test_case)
# 		testunit.addTests(test_case)
# 	return testunit
#
#
# if __name__ == '__main__':
# 	now = time.strftime('%Y-%m-%d %H_%M_%S')  # 获取当前时间
# 	report_dir = '.\\report'  # 指定测试报告输出路径
# 	filename = report_dir + '\\' + now + 'result.html'  # 定义测试报告的名称
# 	fp = open(filename, 'wb')
# 	runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
#
# 	alltestnames = creatsuite()
# 	runner.run(alltestnames)
# 	fp.close()
# send_report(report_dir)
