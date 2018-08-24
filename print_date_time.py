#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author beichenwenxin https://github.com/beichenwenxin/Python/edit/master/print_date_time.py
Created on Fri Aug 24 10:01:07 2018 
"""
import time

def work_out(str):
    #2018-08-24 09:54:44 Test string. 
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),str
    
    #20180824100107 Test string.
    print time.strftime("%Y%m%d%H%M%S", time.localtime()),str
    
    #2018/08/24 10:01:07 Test string.
    print time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()),str
    
    #2018年08月24日 10:01:07 Test string.
    print time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()),str
    
    #Fri Aug 24 10:01:07 2018 Test string.
    print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()),str

if __name__ == '__main__':
    str="Test string. "
    work_out(str)
    
    work_out("")
    
