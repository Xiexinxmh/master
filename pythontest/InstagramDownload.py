# -*- coding:utf-8 -*-
# @Time      :2019-09-23 17:30
# @Author    :xiexin
# @File      :InstagramDownload.py

import os


def Save():
    global path
    path = ("F:\InstagramDownload")
    if not os.path.exists(path):
        os.makedirs(path)


def Download(Name):
    os.chdir(path)
    os.system("instagram-scraper " + Name)


if __name__ == '__main__':
    Save()
    Name = input('请输入需要下载的帐号：')
    Download(Name)
