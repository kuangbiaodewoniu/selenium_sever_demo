# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: t.py.py 
@time: 2018/04/23 
"""

from selenium.webdriver import Remote
from time import sleep


def do():
    driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities={'platform': 'ANY', 'browserName': 'chrome','version':'', 'javascriptEnabled': True})
    driver.get('https://www.baidu.com')
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    do()