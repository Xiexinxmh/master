#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/6 10:48
# @Version : Python 3.7.1


# # 导入模块 openpyxl
# import openpyxl
# from openpyxl.styles import PatternFill
# from openpyxl.styles import colors
# from openpyxl.styles import Font, Color
#
# # 读取excel文件
# # 括号中的字符串为你要比较的两个excel的路径，注意用“/”
# wb_a = openpyxl.load_workbook('E:/KENO表.xlsx')
# wb_b = openpyxl.load_workbook('E:/KENO表 - 副本.xlsx')
#
#
# # 定义一个方法来获取表格中某一列的内容，返回一个列表
# # 在这里，我的表格中：IP是具有唯一性的，所以我用它来区分数据的差异，而IP这一列在我的表格中是第“C”列
# def getIP(wb):
# 	sheet = wb.active
# 	ip = []
# 	for cellobj in sheet['C']:
# 		ip.append(cellobj.value)
#
# 	return ip
#
#
# # 获得ip列表
# ip_a = getIP(wb_a)
# ip_b = getIP(wb_b)
# # 将两个列表转换成集合
# aa = set(ip_a)
# bb = set(ip_b)
# # 找出两个列表的不同行，并转换成列表
# difference = list(aa ^ bb)
# # 打印出列表中的元素
# # 到这一步，两个表格中不同的数据已经被找出来了
# for i in difference:
# 	print(i)
#
# # 将不同行高亮显示
# print("开始第一张表" + "----" * 10)
# a = wb_a.active['C']
# for cellobj in a:
# 	if cellobj.value in difference:
# 		print(cellobj.value)
# 		cellobj.font = Font(color=colors.BLACK, italic=True, bold=True)
# 		cellobj.fill = PatternFill("solid", fgColor="DDDDDD")
# print("开始第二张表" + "----" * 10)
# b = wb_b.active['C']
# for cellobj in b:
# 	if cellobj.value in difference:
# 		print(cellobj.value)
# 		cellobj.font = Font(color=colors.BLACK, italic=True, bold=True)
# 		cellobj.fill = PatternFill("solid", fgColor="FF0000")
#
# # wb_a.save('E:/a.xlsx')
# wb_b.save('E:/b.xlsx')

# 比对两个Excel文件内容的差异
# ---------------------假设条件----------------
# 1、源表和目标表格式一致
# 2、不存在合并单元格
# 3、第2行开始比对
# ---------------------------------------------

import xlrd
import xlwt
import os
import time  # 引入time模块


# 往日志文件中追加内容函数
def writeappend_logfile(filename, content):
	file = open(filename, 'a')  # 以追加方式打开日志文件
	time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 系统时间格式化
	file.writelines(time_now + ':' + content + '\n')  # 写入内容
	file.close()  # 关闭文件


def read_excel(ori_path, tar_path, sub_name):  #
	same = 0  # 匹配一致数量
	different = 0  # 匹配不一致数量
	before_xls = {}  # 存储源xls文件
	after_xls = {}  # 比对的xls文件
	wb_bef = xlrd.open_workbook(ori_path)  # 打开原始文件
	wb_aft = xlrd.open_workbook(tar_path)  # 打开目标文件
	sheet_num = len(wb_bef.sheets())  # 源表子表数量
	##    for sheet_i in range(sheet_num):  #excel中子页面数量
	##        sheet_ori=wb_ori.sheet_by_index(sheet_i) #通过索引值获取源表名
	##        sheet_tar=wb_tar.sheet_by_index(sheet_i) #通过索引值获取源表名

	startime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 获取系统当前时间并格式化为格式
	print(startime, ' 开始比对...')
	logname = 'log_' + startime[0:10] + '.log'  # 截取日期年月日构成日志文件名

	logfile = open(logname, 'w')  # 创建日志文件,如果文件存在则清空内容，不存在则创建，如果需要同时批量比对多张表，可以考虑将日志文件名作为参数传入
	logfile.writelines(startime + '：开始比对...' + '\n')  # 写入开始时间
	logfile.close()  # 关闭日志文件

	try:
		sheet_bef = wb_bef.sheet_by_name(sub_name)
		sheet_aft = wb_aft.sheet_by_name(sub_name)
		if sheet_bef.name == sheet_aft.name:
			# sheet表名
			if sheet_bef.name == sub_name:
				# 先将数存入dictionary中dictionary(rows:list)
				# 第一行存储表头
				# 源表取一行数据与目标表全表进行比对如果表中存在主键可以用主键进行索引
				# 数据从excel第3行开始
				global bef_num
				for rows in range(1, sheet_bef.nrows):
					before_list = sheet_bef.row_values(rows)  # 源表i行数据
					after_list = sheet_aft.row_values(rows)  # 目标表i行数据
					before_xls[rows] = before_list  # 源表写入字典
					after_xls[rows] = after_list  # 目标表写入字典

				if before_xls[1] == after_xls[1]:
					print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 表头一致')
				for bef_num in before_xls:
					flag = 'false'  # 判断是否一致标志
					for aft_num in after_xls:
						if before_xls[bef_num] == after_xls[aft_num]:
							flag = 'true'
							break  # 如果匹配到结果退出循环
					if flag == 'true':  # 匹配上结果输出后台日志
						print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' row:%d is ok' % bef_num)
						same += 1
					else:  # 匹配不上将源表中行记录写入txt
						print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' row:%d is different' % bef_num)
						different += 1
						data = before_xls[bef_num]
						logstr = '  不一致：row< ' + str(bef_num) + ' >：' + str(data)
						writeappend_logfile(logname, logstr)
				# logstr='【比对完成】总记录数:'+str(bef_num)+'条,一致:'+str(success)+'条,不一致:'+str(fail)+'条'
				logstr = '  比对完成总记录数：{:d} 条，一致：{:d} 条，不一致：{:d} 条'.format(bef_num, same, different)
				print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' %s 比对结束' % sheet_bef.name)
				print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ' 总记录数：%d 条,一致：%d 条,不一致：%d 条' % (
					bef_num, same, different))
				writeappend_logfile(logname, logstr)

		else:
			errmsg = ' ' + sub_name + '子表名不一致'
			writeappend_logfile(logname, errmsg)
	except Exception as err:
		writeappend_logfile(logname, str(err))  # 输出异常


def main():
	pass


if __name__ == '__main__':
	read_excel(r'now.xlsx', 'before.xlsx', 'Sheet1')
