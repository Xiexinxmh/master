# -*- coding:utf-8 -*-
# Time          : 2019-11-20 17:55
# Author        : xiexin
# File          :
# Description   :

# from __future__ import division
# from ctypes import *
# import win32con, win32clipboard
# import wx.grid
# import warnings
# import base64
# import urllib.parse
# from math import trunc
# from pdf417gen import encode, render_image
# from PIL import Image, ImageDraw, ImageFont
#
# warnings.filterwarnings('ignore')
#
#
# class testFrame(wx.Frame):
#     def __init__(self):
#         self.maxwidth = 600  # 设置总界面的宽
#         self.maxhigh = 450  # 设置总界面的高
#         wx.Frame.__init__(self, None, -1, u'pdf417二维码生成器', size=(self.maxwidth, self.maxhigh))  # 设置底层框架
#         self.panel0 = wx.Panel(self, 1, pos=(0, 0), size=(
#             self.maxwidth, self.maxhigh))  # 新建panel于Frame之后。self:表示panel的归属是谁。pos:坐标(横坐标，纵坐标).size:大小(（)宽，高).
#         # 输入票号ID
#         self.inputText = wx.StaticText(self.panel0, -1, u'输入票号ID:', pos=(20, 25))
#         # self.text1.SetBackgroundColour('green')
#         # self.text1.SetForegroundColour('yellow')
#         self.codeID = wx.TextCtrl(self.panel0, -1, u"", pos=(120, 25), size=(450, 25))
#         # 单选框
#         self.typeText = wx.StaticText(self.panel0, -1, u'选择类型:', pos=(20, 60))
#         self.typeTextWarning = wx.StaticText(self.panel0, -1, u'(请先输入票号ID!!!)', pos=(100, 60))
#         self.typeTextWarning.SetForegroundColour('red')
#         self.choose5D = wx.RadioButton(self.panel0, -1, "5D", pos=(20, 90), size=wx.DefaultSize, style=wx.RB_GROUP)
#         self.choose6D = wx.RadioButton(self.panel0, -1, "6D", pos=(200, 90), size=wx.DefaultSize)
#         self.choosejikai = wx.RadioButton(self.panel0, -1, "即开二维码", pos=(380, 90), size=wx.DefaultSize)
#         self.choose5D.SetValue(False)
#         self.choose5D.Bind(wx.EVT_RADIOBUTTON, self.chooseType)
#         self.choose6D.Bind(wx.EVT_RADIOBUTTON, self.chooseType)
#         self.choosejikai.Bind(wx.EVT_RADIOBUTTON, self.chooseType)
#         self.Centre()
#         self.codeText = wx.StaticText(self.panel0, -1, u'生成的二维码：', pos=(20, 120))
#         # 保存二维码图片到剪贴板
#         self.copyButton = wx.Button(self.panel0, -1, u"复制二维码", pos=(22, 350), size=(550, 60))
#         self.copyButton.Bind(wx.EVT_BUTTON, self.copyImage)
#         self.Fit()
#
#     # 选择彩种类型
#     def chooseType(self, event):
#         global code
#         code = self.codeID.GetValue()
#         choosed = event.GetEventObject().GetLabel()
#         if code != "":
#             if choosed == '5D':
#                 finalCode = '5D-' + urllib.parse.quote(str(base64.b64encode(code.encode('utf-8')), 'utf-8'))
#                 print(finalCode)
#                 printCode(finalCode)
#                 self.displayImage()
#                 return finalCode
#             elif choosed == '6D':
#                 finalCode = '6D-' + urllib.parse.quote(str(base64.b64encode(code.encode('utf-8')), 'utf-8'))
#                 print(finalCode)
#                 printCode(finalCode)
#                 self.displayImage()
#                 return finalCode
#             elif choosed == '即开二维码':
#                 finalCode = code
#                 print(finalCode)
#                 printCode(finalCode)
#                 self.displayImage()
#                 return finalCode
#             else:
#                 print("输入错误!")
#         else:
#             self.choose5D.SetValue(False)
#             self.choose6D.SetValue(False)
#             self.choosejikai.SetValue(False)
#             print("请先输入票号!")
#
#     # 显示二维码图片
#     def displayImage(self):
#         self.image1 = wx.Image('./' + code + '.bmp', wx.BITMAP_TYPE_ANY)
#         # print('图片的尺寸为{0}x{1}'.format(self.image1.GetWidth(), self.image1.GetHeight()))
#         w = self.image1.GetWidth() * 0.5
#         h = self.image1.GetHeight() * 0.5
#         self.image1.Rescale(w, h)
#         mypic = self.image1.ConvertToBitmap()
#         self.mypic = wx.StaticBitmap(self.panel0, -1, mypic, pos=(20, 150))
#
#     # 复制二维码图片
#     def copyImage(self, aString):
#         aString = windll.user32.LoadImageW(0, "./" + code + ".bmp", win32con.IMAGE_BITMAP, 0, 0,
#                                            win32con.LR_LOADFROMFILE)
#         print(aString)
#         if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
#             win32clipboard.OpenClipboard()
#             win32clipboard.EmptyClipboard()
#             win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
#             win32clipboard.CloseClipboard()
#             print('复制二维码成功!')
#             self.copyText = wx.StaticText(self.panel0, -1, u'复制成功!', pos=(270, 410))
#             self.copyText.SetForegroundColour('red')
#
#
# # 生成二维码图片
# def printCode(finalCode):
#     codes = encode(finalCode, columns=6, security_level=6)
#     pdf417ma = render_image(codes)
#     img1 = pdf417ma.size
#     codeBar = pdf417ma.resize((img1[0] * 2, trunc(img1[0] / 5) * 2))
#     # 文字背景
#     background = Image.new("RGB", [1190, 150], "white")
#     draw = ImageDraw.Draw(background)
#     font_path = r'C:/Windows/Fonts/msyh.ttc'
#     myfont = ImageFont.truetype(font_path, size=32)
#     if finalCode[0:2] == '5D' or finalCode[0:2] == '6D':
#         fticketNum = finalCode[0:2] + '购彩票号:            ' + code
#     else:
#         fticketNum = '即开票ID:\n' + code
#     draw.text((15 * 2, 5 * 2), fticketNum, font=myfont, fill='#FF0000')
#     size1, size2 = codeBar.size, background.size
#     joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
#     loc1, loc2 = (0, 0), (0, size1[1])
#     joint.paste(codeBar, loc1)
#     joint.paste(background, loc2)
#     # joint.show()
#     jointname = './' + code + '.bmp'
#     joint.save(jointname)
#
#
# if __name__ == "__main__":
#     app = wx.App()
#     testFrame().Show()
#     app.MainLoop()

import xlrd, xlwt
import pandas as pd

import requests
import unittest
from common import Log as Log
import json
import aes_com


def Loginin(phone,pwd):
    log = Log.MyLog.get_log()
    logger = log.get_logger()
    get_url = 'http://61.14.255.62/api/login_login?KEYDATA='
    data = '{"phoneNo":"13168320227","password":"670b14728ad9902aecba32e22fa4f6bd","phoneInfo":"HUAWEI MLA-AL10","phoneSn":"4ccc6ab8a9fd2544","longitude":106.56358166666665,"latitude":39.00125,"loginType":2}'
    print(data)
    data = json.dumps(data)
    data1 = aes_com.encrypt(data)
    url1 = (get_url + data1).replace('\n', '').replace('\r', '')
    headers = {'Charset': 'UTF-8',
               'User-Agent': 'Mozilla/5.0 (Linux; U; Mobile; Android 5.1.1;OPPO R11 Build/FRF91)',
               'Accept': '*/*', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip, deflate',
               'Host': '61.14.255.62'}
    url = url1
    headers = headers
    res = requests.get(url=url, headers=headers)
    result = res.json()
    # self.assertEqual(self.result['result'], 101)
    # self.assertEqual(self.result['msg'], '登录成功')
    # self.tearDown()
    print(res.status_code)
    # print(res.text)


if __name__ == '__main__':
    df = pd.read_excel('./testFile/properties.xlsx',converters={u'pwd': str})  # converters={u'pwd': str}表示将字段pwd内容读取为str;可以通过sheet_name来指定读取的表单
    phone = format(df.iloc[0, 0])
    pwd = format(df.iloc[0, 1])
    Loginin(phone,pwd)
    print(phone)  # 格式化输出
    print(pwd)  # 格式化输出

